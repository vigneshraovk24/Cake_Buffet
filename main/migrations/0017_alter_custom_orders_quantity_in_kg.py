# Generated by Django 4.0.1 on 2022-06-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_custom_orders_quantity_in_kg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_orders',
            name='quantity_in_kg',
            field=models.IntegerField(default=1),
        ),
    ]
