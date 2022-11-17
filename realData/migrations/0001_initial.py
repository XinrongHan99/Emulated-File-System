# Generated by Django 4.1.3 on 2022-11-16 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
        ('home','0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('rank', models.IntegerField(default=-1)),
                ('population', models.IntegerField()),
            ],
            options={
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('busniss_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('rate', models.IntegerField()),
                ('review_cnt', models.IntegerField()),
                ('city', models.CharField(max_length=10)),
                ('latitude', models.FloatField()),
                ('longitude', models.CharField(max_length=10)),
                ('categories', models.JSONField()),
            ],
            options={
                'db_table': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='RestUser',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'RestUser',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('restId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bussiness_id', to='realData.restaurants')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_id', to='realData.restuser')),
            ],
            options={
                'db_table': 'Rate',
            },
        ),
    ]