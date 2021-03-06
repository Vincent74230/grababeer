# Generated by Django 3.2.7 on 2021-09-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beers',
            fields=[
                ('barcode', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('img_url', models.URLField()),
                ('description', models.TextField()),
                ('IBU', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Malts',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('malts_in_that_beer', models.ManyToManyField(to='home.Beers')),
            ],
        ),
        migrations.CreateModel(
            name='Hops',
            fields=[
                ('name', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('hops_in_that_beer', models.ManyToManyField(to='home.Beers')),
            ],
        ),
    ]
