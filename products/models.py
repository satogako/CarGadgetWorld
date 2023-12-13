from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta(object):
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return f'{self.friendly_name}'


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return self.friendly_name


class Catalogue(models.Model):

    class Meta(object):
        verbose_name_plural = 'Catalogue'

    CAR_BRAND = (
        ('Audi', 'Audi'),
        ('Volkswagen', 'Volkswagen'),
        ('Mercedes', 'Mercedes'),
        ('Toyota', 'Toyota'),
        ('Hyundai', 'Hyundai'),
        ('Citroen', 'Citroen'),
    )

    auto_brand = models.CharField(
        max_length=24, null=True, blank=True, choices=CAR_BRAND
    )

    def __str__(self):
        return f'{self.auto_brand}'


class Image(models.Model):
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.image_url}'


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
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ManyToManyField(Image, blank=True)
    stock = models.PositiveSmallIntegerField()
    wish_lists = models.ManyToManyField(User, related_name='wish_list', blank=True)

    def __str__(self):
        return f'{self.name}'
