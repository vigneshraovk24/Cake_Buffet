# Generated by Django 4.0.1 on 2022-06-25 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_rename_customorder_customcakes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcakes',
            name='custom_instructions',
        ),
        migrations.CreateModel(
            name='Custom_Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_ordered', models.BooleanField(default=False)),
                ('quantity_in_kg', models.IntegerField(default=1)),
                ('delivery_address', models.CharField(blank=True, max_length=400)),
                ('custom_alt_phone', models.CharField(blank=True, max_length=10)),
                ('custom_alt_name', models.CharField(blank=True, max_length=100)),
                ('custom_instructions', models.CharField(blank=True, max_length=400)),
                ('custom_ordered_date', models.DateField(default=django.utils.timezone.now)),
                ('custom_status', models.CharField(choices=[('Ordered', 'Ordered'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled'), ('Waiting for confirmation', 'Waiting for confirmation')], default='Waiting for confirmation', max_length=40)),
                ('custom_delivery_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('custom_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customcakes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Custom Order',
                'verbose_name_plural': 'Custom Orders',
            },
        ),
    ]
