# Generated by Django 4.1.5 on 2023-02-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_organization_email_organization_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='mobile',
            field=models.CharField(max_length=10, null=True, verbose_name='Номер телефона'),
        ),
    ]
