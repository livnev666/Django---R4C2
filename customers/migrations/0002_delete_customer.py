# Generated by Django 4.2.6 on 2023-10-08 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_delete_order'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
