# Generated by Django 5.0.2 on 2024-04-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0037_propertydetails_property_carousel_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='property_carousel_3',
            field=models.ImageField(default='agent', upload_to='properties-img'),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_carousel_4',
            field=models.ImageField(default='agent', upload_to='properties-img'),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_carousel_5',
            field=models.ImageField(default='agent', upload_to='properties-img'),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_carousel_6',
            field=models.ImageField(default='agent', upload_to='properties-img'),
        ),
    ]
