# Generated by Django 2.1.5 on 2019-02-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blip_core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
        migrations.RemoveField(
            model_name='eventattendees',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventattendees',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventAttendees',
        ),
    ]
