# Generated by Django 4.0.1 on 2022-06-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_orders',
            name='quantity_in_kg',
            field=models.IntegerField(blank=True),
        ),
    ]