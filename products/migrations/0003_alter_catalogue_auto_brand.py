# Generated by Django 3.2.20 on 2023-12-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='auto_brand',
            field=models.CharField(blank=True, choices=[('Audi', 'Audi'), ('Volkswagen', 'Volkswagen'), ('Mercedes', 'Mercedes'), ('Toyota', 'Toyota'), ('Hyundai', 'Hyundai'), ('Citroen', 'Citroen')], max_length=24, null=True),
        ),
    ]
