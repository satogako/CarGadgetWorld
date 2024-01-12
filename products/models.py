from django.db import models
from django.contrib.auth.models import User
from car_gadget_world.settings import AWS_STORAGE_BUCKET_NAME
import os

class Category(models.Model):
    name = models.CharField(max_length=25)
    display_name = models.CharField(max_length=25, null=True, blank=True)

    class Meta(object):
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def get_display_name(self):
        return f'{self.display_name}'


class Brand(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_display_name(self):
        return self.display_name


class Catalogue(models.Model):

    class Meta(object):
        verbose_name_plural = 'Catalogue'

    CAR_BRAND = (
        ('Audi', 'Audi'),
        ('Volkswagen', 'Volkswagen'),
        ('Mercedes', 'Mercedes'),
        ('Toyota', 'Toyota'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Citroen', 'Citroen'),
    )

    auto_brand = models.CharField(
        max_length=24, null=True, blank=True, choices=CAR_BRAND
    )

    def __str__(self):
        return f'{self.auto_brand}'



class Product(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    visible_to_customers = models.BooleanField(default=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    auto_brand = models.ForeignKey('Catalogue', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(
        upload_to='accessories_photo/', blank=True, null=True)
    stock = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def image_link(self):
        if self.image:
            return self.image.url
        else:
            if 'USE_AWS' in os.environ:
                return (f'https://{AWS_STORAGE_BUCKET_NAME}.'
                        f's3.amazonaws.com/media/'
                        f'accessories_photo/no_image.jpg')
            else:
                return '/media/accessories_photo/no_image.jpg'

    def __str__(self):
        return f'{self.name}'

