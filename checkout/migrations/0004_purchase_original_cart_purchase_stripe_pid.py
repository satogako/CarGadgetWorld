# Generated by Django 5.0 on 2024-04-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_purchase_order_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='purchase',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
