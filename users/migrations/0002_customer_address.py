# Generated by Django 4.0.1 on 2022-07-18 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Address',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
