# Generated by Django 4.1.5 on 2023-02-04 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_oraganization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oraganization',
            old_name='name',
            new_name='org_name',
        ),
        migrations.RenameField(
            model_name='oraganization',
            old_name='icon',
            new_name='picture',
        ),
    ]