# Generated by Django 5.0.2 on 2024-03-15 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0021_alter_newsdetails_news_paragraph_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_2',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_3',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_4',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_5',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_6',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='newsdetails',
            name='News_paragraph_7',
            field=models.CharField(max_length=1500),
        ),
    ]
