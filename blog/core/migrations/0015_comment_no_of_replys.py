# Generated by Django 4.1.7 on 2023-03-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='no_of_replys',
            field=models.IntegerField(default=0),
        ),
    ]