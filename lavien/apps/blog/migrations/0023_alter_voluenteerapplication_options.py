# Generated by Django 4.1.5 on 2023-02-20 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_organization_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voluenteerapplication',
            options={'verbose_name': 'Заявка волонтера', 'verbose_name_plural': 'Заявки волонтеров'},
        ),
    ]
