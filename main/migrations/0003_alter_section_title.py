# Generated by Django 4.2.1 on 2023-05-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_section_logos_remove_section_sub_sections_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(choices=[('about', 'About'), ('mining', 'Mining & Geology'), ('polar', 'Polar Expeditions'), ('photo', 'Photography'), ('translations', 'Translations')], max_length=50),
        ),
    ]
