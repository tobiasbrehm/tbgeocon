# Generated by Django 4.2.1 on 2023-05-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_section_logos_section_logos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sub_section',
            options={'verbose_name': 'Sub section', 'verbose_name_plural': 'Sub sections'},
        ),
        migrations.AddField(
            model_name='logo',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sub_section',
            name='title_de',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
