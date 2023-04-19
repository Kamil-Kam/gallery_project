from django.test import TestCase, Client
from django.urls import reverse
from . models import Category, Gallery

# Create your tests here.


class TestGalleryViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(category_name='Test Category')
        self.gallery = Gallery.objects.create(
            category=self.category,
            description='Test Gallery',
            image='test.jpg'
        )

    def test_gallery(self):
        response = self.client.get(reverse('gallery', args=[self.category.category_name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        self.assertContains(response, 'Test Gallery')

    def test_photo(self):
        response = self.client.get(reverse('photo', args=[self.category.category_name, self.gallery.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/photo.html')
        self.assertContains(response, 'Test Gallery')

    def test_add_photo(self):
        with open('test.jpg', 'rb') as img:
            response = self.client.post(reverse('add_photo'), {'description': 'Test Description', 'image': img})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'gallery/add_photo.html')
            self.assertContains(response, 'Photo uploaded successfully!')

    def test_main_website(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/main.html')
        self.assertContains(response, 'Test Category')

    def test_milky_way_carousel(self):
        response = self.client.get(reverse('milky_way_carousel', args=['active', 'next', 'next_next']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/milky_way_carousel.html')
        self.assertContains(response, 'active')
        self.assertContains(response, 'next')
        self.assertContains(response, 'next_next')

    def test_see_photo(self):
        response = self.client.get(reverse('see_photo', args=['the_photo']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/the_photo.html')
        self.assertContains(response, 'the_photo')


class TestGalleryModels(TestCase):

    def test_category_str_method(self):
        category = Category.objects.create(category_name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_gallery_str_method(self):
        category = Category.objects.create(category_name='Test Category')
        gallery = Gallery.objects.create(
            category=category,
            description='Test Gallery',
            image='test.jpg'
        )
        self.assertEqual(str(gallery), 'Test Category /static/Test Category/test.jpg Test Gallery')