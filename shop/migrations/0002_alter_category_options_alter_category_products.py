# Generated by Django 5.1.5 on 2025-01-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='categories', to='shop.product'),
        ),
    ]
