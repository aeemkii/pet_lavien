# Generated by Django 4.1.5 on 2023-02-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialnetworks',
            options={'verbose_name': 'Социальная сеть', 'verbose_name_plural': 'Социальные сети'},
        ),
    ]