# Generated by Django 4.0.1 on 2022-07-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_remove_custom_orders_custom_alt_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_orders',
            name='quantity_in_kg',
            field=models.IntegerField(default=2),
        ),
    ]