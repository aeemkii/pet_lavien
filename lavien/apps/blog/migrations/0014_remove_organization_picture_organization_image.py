# Generated by Django 4.1.5 on 2023-02-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_organization_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='picture',
        ),
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.ImageField(null=True, upload_to='organization/images/', verbose_name='Изображение'),
        ),
    ]
