# Generated by Django 4.1.7 on 2023-08-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0111_post_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='video_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
