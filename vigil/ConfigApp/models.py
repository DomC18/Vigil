from django.db import models
from datetime import datetime
import globalvariables as gv

class Subsystem(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="SubsystemName", max_length=50)
    image = models.ImageField(name="SubsystemImage", blank=True, null=True)

    def __str__(self):
        return f"{self.SubsystemName}"

class SubsystemConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="SubConfigName", max_length=50)
    subsystems = models.ManyToManyField(name="Subsystems", to=Subsystem, blank=True)

    def __str__(self):
        return f"{self.SubConfigName}"



class RobotConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    name = models.CharField(name="RobotName", default="NewRobot", max_length=50, blank=False)
    image = models.ImageField(name="RobotImage", blank=True, null=True)
    year = models.IntegerField(name="FRCYear", default=datetime.now().year, blank=True)
    team_number = models.IntegerField(name="TeamNumber", default=0, blank=True)
    drivetrain_type = models.CharField(name="DriveTrainType", default="Tank Drive", max_length=50, blank=True)

    def __str__(self):
        return f"{self.RobotName}"



class CurrentConfiguration(models.Model):
    created_by = models.CharField(name="CreatedBy", max_length=50, default="dmac")
    subsystem_configuration = models.ForeignKey(name="SubsystemConfig", to=SubsystemConfiguration, blank=True, null=True, on_delete=models.CASCADE)
    robot_configuration = models.ForeignKey(name="RobotConfig", to=RobotConfiguration, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.CreatedBy} current configuration"