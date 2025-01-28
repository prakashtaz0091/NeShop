# Generated by Django 5.1.5 on 2025-01-28 15:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_district_state_municipality_municipality'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_address', models.TextField(max_length=500)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_adresses', to='cart.district')),
                ('municipality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_adresses', to='cart.municipality')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_adresses', to='cart.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_adresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
