# Generated by Django 5.0.6 on 2024-07-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsystem',
            name='Subsystem Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]