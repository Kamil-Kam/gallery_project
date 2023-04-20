from django.test import TestCase, Client
from django.urls import reverse
from . models import Category, Gallery
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
import os

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
        self.assertEqual(str(gallery), 'Test Category /media/test.jpg Test Gallery')


class TestGalleryViewsAddPhoto(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(category_name='Visitors photos')
        self.gallery = Gallery.objects.create(
            category=self.category,
            description='Test Gallery',
            image='test.jpg'
        )

    def test_add_photo_view(self):
        image_data = BytesIO()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(image_data, format='JPEG')
        image_data.seek(0)

        uploaded_file = SimpleUploadedFile('image.jpg', content=image_data.read(), content_type='image/jpeg')

        response = self.client.post(reverse('add_photo'), {
            'description': 'Test photo',
            'image': uploaded_file,
        })

        self.assertEqual(response.status_code, 200)

        gallery = Gallery.objects.last()
        self.assertEqual(gallery.description, 'Test photo')
        self.assertEqual(gallery.category.category_name, 'Visitors photos')
        self.assertEqual(gallery.image.url.split('/')[-1], 'image.jpg')

        os.remove(gallery.image.path)

