# Generated by Django 4.0.1 on 2022-06-25 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_quantity_cartitems_quantity_in_kg_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='quantity_in_kg',
            new_name='quantity',
        ),
    ]
