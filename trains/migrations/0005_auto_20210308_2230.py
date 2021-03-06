# Generated by Django 3.1.7 on 2021-03-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0004_route_route_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '列車', 'verbose_name_plural': '列車'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name': '路線', 'verbose_name_plural': '路線'},
        ),
        migrations.AlterField(
            model_name='item',
            name='sex',
            field=models.ManyToManyField(default=1, to='trains.Route', verbose_name='所属路線'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.IntegerField(verbose_name='路線ID'),
        ),
    ]
