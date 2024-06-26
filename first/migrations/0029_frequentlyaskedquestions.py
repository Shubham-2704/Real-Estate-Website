# Generated by Django 5.0.2 on 2024-03-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0028_commercialdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequentlyaskedquestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faq_question', models.CharField(max_length=300)),
                ('Faq_description', models.CharField(max_length=3000, null=True)),
                ('faq_help', models.CharField(max_length=300)),
                ('faq_contact', models.CharField(max_length=13)),
                ('faq_image', models.ImageField(default='faq', upload_to='Faq-images')),
                ('faq_total_area_sq', models.CharField(default='560+', max_length=20, null=True)),
                ('faq_apartment_sold', models.CharField(default='197K+', max_length=20, null=True)),
                ('faq_constrution', models.CharField(default='200+', max_length=30, null=True)),
                ('faq_rooms', models.CharField(default='250+', max_length=20, null=True)),
            ],
        ),
    ]
