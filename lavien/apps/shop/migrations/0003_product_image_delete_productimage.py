# Generated by Django 4.1.5 on 2023-02-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product/images/', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]