# Generated by Django 4.1.7 on 2023-05-22 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0100_buylesson_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buylesson',
            old_name='subject',
            new_name='method',
        ),
    ]