# Generated by Django 5.0.2 on 2024-03-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_alter_teamdetails_team_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_img', models.ImageField(upload_to='properties')),
                ('property_agent_img', models.ImageField(upload_to='propertyagent')),
                ('property_type', models.CharField(max_length=30)),
                ('property_name', models.CharField(max_length=30)),
                ('property_location', models.CharField(max_length=30)),
                ('amenities', models.CharField(max_length=30)),
                ('property_price', models.CharField(max_length=10)),
            ],
        ),
    ]
