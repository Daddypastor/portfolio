# Generated by Django 4.2.3 on 2023-07-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
