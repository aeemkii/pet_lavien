# Generated by Django 4.1.5 on 2023-02-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_tags_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oraganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60)),
                ('icon', models.ImageField(upload_to='oraganization/icons/')),
                ('description', models.TextField(null=True, verbose_name='Описание организации')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
