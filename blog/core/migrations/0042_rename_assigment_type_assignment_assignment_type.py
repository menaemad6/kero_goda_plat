# Generated by Django 4.1.7 on 2023-03-11 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_rename_assigment_name_assignment_assignment_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assigment_type',
            new_name='assignment_type',
        ),
    ]
