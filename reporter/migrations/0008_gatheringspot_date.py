# Generated by Django 2.2.12 on 2020-05-02 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0007_auto_20200425_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatheringspot',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
