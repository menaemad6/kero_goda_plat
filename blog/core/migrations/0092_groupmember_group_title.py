# Generated by Django 4.1.7 on 2023-05-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_group_groupmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='group_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]