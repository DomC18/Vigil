from django.db import models
from datetime import datetime
import globalvariables as gv

class Subsystem(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="Subsystem Name", max_length=50)
    image = models.ImageField(name="Subsystem Image", blank=True, null=True)

    def __str__(self):
        return super().__str__()

class SubsystemConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="SubConfigName", max_length=50)
    subsystems = models.ManyToManyField(name="Subsystems", to=Subsystem, blank=True)

    def __str__(self):
        return super().__str__()



class RobotConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="Robot Name", default="NewRobot", max_length=50, blank=False)
    image = models.ImageField(name="Robot Image", blank=True, null=True)
    year = models.IntegerField(name="FRC Year", default=datetime.now().year, blank=True)
    team_number = models.IntegerField(name="Team Number", default=0, blank=True)
    drivetrain_type = models.CharField(name="DriveTrain Type", default="Tank Drive", max_length=50, blank=True)

    def __str__(self):
        return super().__str__()



class CurrentConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    subsystem_configuration = models.ForeignKey(name="SubsystemConfig", to=SubsystemConfiguration, blank=True, null=True, on_delete=models.CASCADE)
    robot_configuration = models.ForeignKey(name="RobotConfig", to=RobotConfiguration, blank=True, null=True, on_delete=models.CASCADE)