from django.db import models
from datetime import datetime

class Subsystem(models.Model):
    name = models.CharField(name="Subsystem Name", max_length=50)
    image = models.ImageField(name="Subsystem Image", blank=True, null=True)

    def __str__(self):
        return super().__str__()

class Configuration(models.Model):
    name = models.CharField(name="Robot Name", default="NewRobot", max_length=50, blank=False)
    image = models.ImageField(name="Robot Image", blank=True, null=True)
    year = models.IntegerField(name="FRC Year", default=datetime.now().year, blank=True)
    team_number = models.IntegerField(name="Team Number", default=0, blank=True)
    drivetrain_type = models.CharField(name="DriveTrain Type", default="Tank Drive", max_length=50, blank=True)
    subsystems = models.ManyToManyField(Subsystem, blank=True)

    def __str__(self):
        return super().__str__()