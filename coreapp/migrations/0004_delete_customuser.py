# Generated by Django 5.0.2 on 2024-03-03 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0003_customuser_delete_all_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]