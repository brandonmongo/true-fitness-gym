# Generated by Django 3.1.5 on 2021-02-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210215_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Reviews',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Servings',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
