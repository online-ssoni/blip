# Generated by Django 2.1.5 on 2019-02-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blip_core', '0003_auto_20190204_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendees',
            name='attended_status',
            field=models.BooleanField(default=False),
        ),
    ]