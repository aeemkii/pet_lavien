# Generated by Django 4.1.5 on 2023-02-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='dop_dscr',
            field=models.TextField(null=True, verbose_name='Дополнительное описание'),
        ),
    ]