# Generated by Django 5.0.2 on 2024-04-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0042_propertydetails_property_description_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='property_map_location',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]