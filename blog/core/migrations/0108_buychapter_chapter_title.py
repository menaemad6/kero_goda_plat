# Generated by Django 4.1.7 on 2023-06-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0107_buylesson_lecture_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='buychapter',
            name='chapter_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
