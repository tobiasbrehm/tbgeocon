# Generated by Django 4.2.1 on 2023-05-19 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='uploads')),
                ('img_alt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sub_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='uploads')),
                ('img_alt', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('text_de', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('img_alt', models.CharField(blank=True, max_length=50, null=True)),
                ('text', models.TextField()),
                ('text_de', models.TextField(blank=True)),
                ('logos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.logo')),
                ('sub_sections', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.sub_section')),
            ],
        ),
    ]
