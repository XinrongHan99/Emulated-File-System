# Generated by Django 3.2.16 on 2022-11-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realData', '0002_auto_20221122_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest0',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rest0',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rest1',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rest1',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rest2',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rest2',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
