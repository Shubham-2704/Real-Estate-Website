# Generated by Django 5.0.2 on 2024-04-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0050_commercialdetails_commercial_premium_brandedfitting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertydetails',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='property_carousel_1',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='property_carousel_2',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='property_carousel_3',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='property_carousel_4',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='property_carousel_5',
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_videos',
            field=models.ImageField(max_length=2000, null=True, upload_to=''),
        ),
    ]
