# Generated by Django 3.2.5 on 2021-10-05 20:08

import dap.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default=None, max_length=255)),
                ('product_price', models.FloatField(default=True)),
                ('is_discount_price', models.BooleanField(default=False)),
                ('product_discount_price', models.FloatField(default=True)),
                ('product_description', models.TextField(help_text='Input some information', max_length=255, verbose_name='Product Detail')),
                ('product_local_image', models.FileField(default=False, max_length=300, upload_to=dap.models.Upload_Product.get_product_uploaded_image_filepath)),
                ('product_categories', models.CharField(choices=[('technology', 'Technology'), ('fashion', 'Fashion'), ('accessory', 'Accessory')], default=True, max_length=150)),
                ('product_size', models.CharField(choices=[('small', 'Small'), ('normal', 'Normal'), ('large', 'Large')], default='normal', max_length=25)),
                ('product_color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], default='red', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Reg_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('hide_email', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
