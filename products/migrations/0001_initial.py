# Generated by Django 3.1.5 on 2021-02-15 11:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=255)),
                ('Name', models.CharField(blank=True, max_length=255)),
                ('Brand', models.CharField(blank=True, max_length=255)),
                ('Size', models.CharField(blank=True, max_length=100)),
                ('has_weight', models.BooleanField(blank=True, default=False, null=True)),
                ('Flavor', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, size=None)),
                ('Serving', models.DecimalField(blank=True, decimal_places=0, max_digits=2)),
                ('FlavorRating', models.CharField(blank=True, max_length=3)),
                ('Reviews', models.DecimalField(blank=True, decimal_places=0, max_digits=8)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('product_description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]