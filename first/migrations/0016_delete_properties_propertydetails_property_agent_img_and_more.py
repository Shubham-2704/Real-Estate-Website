# Generated by Django 5.0.2 on 2024-03-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0015_alter_propertydetails_property_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='properties',
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_agent_img',
            field=models.ImageField(default='agent', upload_to='propertyagent'),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='property_img',
            field=models.ImageField(default='agent', upload_to='properties-img'),
        ),
    ]
