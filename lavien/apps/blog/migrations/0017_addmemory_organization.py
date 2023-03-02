# Generated by Django 4.1.5 on 2023-02-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_addmemory'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmemory',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to='blog.organization'),
        ),
    ]