# Generated by Django 3.1.5 on 2021-03-12 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210312_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_cart',
        ),
    ]
