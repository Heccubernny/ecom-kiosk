# Generated by Django 3.2.5 on 2021-11-05 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dap', '0008_auto_20211105_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userregistration',
            name='last_name',
        ),
    ]
