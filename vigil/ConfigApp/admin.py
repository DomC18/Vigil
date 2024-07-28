from django.contrib import admin
from .models import Subsystem, SubsystemConfiguration, RobotConfiguration, CurrentConfiguration

admin.site.register(Subsystem)
admin.site.register(SubsystemConfiguration)
admin.site.register(RobotConfiguration)
admin.site.register(CurrentConfiguration)