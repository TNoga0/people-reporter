# Generated by Django 2.2.12 on 2020-04-25 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_auto_20200421_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatheringspot',
            name='geom',
        ),
    ]
