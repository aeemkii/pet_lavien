# Generated by Django 4.1.5 on 2023-02-13 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag_alter_oraganization_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='blog.tag'),
        ),
    ]
