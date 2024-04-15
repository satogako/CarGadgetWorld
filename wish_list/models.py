from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish_list')
    products = models.ManyToManyField(Product, related_name='wish_lists')

    def __str__(self):
        return f'{self.user.username}\'s Wish List'
