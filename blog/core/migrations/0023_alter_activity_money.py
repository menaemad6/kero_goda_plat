# Generated by Django 4.1.7 on 2023-03-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_activity_activity_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='money',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]