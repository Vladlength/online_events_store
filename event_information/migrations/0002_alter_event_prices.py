# Generated by Django 4.2.2 on 2023-08-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='prices',
            field=models.ManyToManyField(blank=True, to='event_information.eventprice'),
        ),
    ]
