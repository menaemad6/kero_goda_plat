# Generated by Django 4.1.7 on 2023-04-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_alter_part_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
