# Generated by Django 5.0.6 on 2024-07-01 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0021_product_inserted_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date_added',
        ),
    ]
