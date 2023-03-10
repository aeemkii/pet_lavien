# Generated by Django 4.1.5 on 2023-02-17 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0015_remove_organization_image_organization_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='memory/images/', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
