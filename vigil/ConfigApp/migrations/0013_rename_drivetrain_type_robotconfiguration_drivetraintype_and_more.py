# Generated by Django 5.0.6 on 2024-07-30 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigApp', '0012_subsystem_createdby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robotconfiguration',
            old_name='DriveTrain Type',
            new_name='DriveTrainType',
        ),
        migrations.RenameField(
            model_name='robotconfiguration',
            old_name='FRC Year',
            new_name='FRCYear',
        ),
        migrations.RenameField(
            model_name='robotconfiguration',
            old_name='Robot Image',
            new_name='RobotImage',
        ),
        migrations.RenameField(
            model_name='robotconfiguration',
            old_name='Robot Name',
            new_name='RobotName',
        ),
        migrations.RenameField(
            model_name='robotconfiguration',
            old_name='Team Number',
            new_name='TeamNumber',
        ),
    ]
