# Generated by Django 5.0.6 on 2024-05-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlforms', '0002_product_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fname', models.CharField(max_length=32)),
                ('lname', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('rePassword', models.CharField(max_length=32)),
            ],
        ),
    ]
