# Generated by Django 4.2.1 on 2023-05-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='logos',
        ),
        migrations.RemoveField(
            model_name='section',
            name='sub_sections',
        ),
        migrations.AddField(
            model_name='section',
            name='logos',
            field=models.ManyToManyField(blank=True, null=True, to='main.logo'),
        ),
        migrations.AddField(
            model_name='section',
            name='sub_sections',
            field=models.ManyToManyField(blank=True, null=True, to='main.sub_section'),
        ),
    ]
