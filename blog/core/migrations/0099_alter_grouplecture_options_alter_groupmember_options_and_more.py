# Generated by Django 4.1.7 on 2023-05-22 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_groupmember_group_image_alter_group_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grouplecture',
            options={'verbose_name': 'Group Lecture', 'verbose_name_plural': 'Group Lectures'},
        ),
        migrations.AlterModelOptions(
            name='groupmember',
            options={'verbose_name': 'Group Member', 'verbose_name_plural': 'Group Members'},
        ),
        migrations.AddField(
            model_name='buylesson',
            name='image',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='buylesson',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]