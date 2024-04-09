# Generated by Django 4.1.7 on 2023-05-19 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_group_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(blank=True, max_length=100)),
                ('lecture_id', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(default='none.jpeg', upload_to='post_images')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('teacher_name', models.CharField(blank=True, max_length=100, null=True)),
                ('teacher_img', models.ImageField(blank=True, null=True, upload_to='teacher_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]