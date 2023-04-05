from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.category_name


def get_image_path(instance, filename):
    category_name_path = instance.category.category_name
    return f"{category_name_path}/{filename}"


class Gallery(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = ResizedImageField(size=[1920, 1920], upload_to=get_image_path)

    def __str__(self):
        return '%s %s %s' % (self.category, self.image.url, self.description)
