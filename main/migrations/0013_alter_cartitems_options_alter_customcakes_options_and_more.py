# Generated by Django 4.0.1 on 2022-06-27 21:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_cartitems_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitems',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='customcakes',
            options={'verbose_name': 'Custom Cake', 'verbose_name_plural': 'Custom Cakes'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Cake', 'verbose_name_plural': 'Cakes'},
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='delivery_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_alt_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Alternate Name'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_alt_phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Alternate Phone'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_delivery_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_instructions',
            field=models.CharField(blank=True, max_length=400, verbose_name='Instructions'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_ordered',
            field=models.BooleanField(default=False, verbose_name='Ordered'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_ordered_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Ordered on'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_status',
            field=models.CharField(choices=[('Ordered', 'Ordered'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Waiting for confirmation', 'Waiting for confirmation')], default='Waiting for confirmation', max_length=40, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='custom_orders',
            name='custom_total',
            field=models.IntegerField(default=0, verbose_name='Total Price'),
        ),
        migrations.AlterField(
            model_name='customcakes',
            name='custom_description',
            field=models.CharField(blank=True, max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='customcakes',
            name='custom_price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='customcakes',
            name='custom_slug',
            field=models.SlugField(default='custom-cakes', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='customcakes',
            name='custom_title',
            field=models.CharField(max_length=150, verbose_name='Cake Name'),
        ),
    ]