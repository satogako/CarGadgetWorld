# Generated by Django 5.0 on 2024-04-13 15:20

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_purchase_original_cart_purchase_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]