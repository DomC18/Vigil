from django.urls import path
from . import views

urlpatterns = [
    path("config/", views.config, name="config"),
    path("robotconfigs/", views.config, name="robotconfigs"),
    path("subsystemconfigs/", views.subsystemconfigs, name="subsystemconfigs"),
    path("subsystems/", views.subsystems, name="subsystems"),
    path("newcurrentconfig/", views.newcurrentconfig, name="newcurrentconfig"),
    path("newrobotconfig/", views.newrobotconfig, name="newrobotconfig"),
    path("newsubsystemconfig/", views.newsubsystemconfig, name="newsubsystemconfig"),
    path("newsubsystem/", views.newsubsystem, name="newsubsystem"),
    path("deleterobotconfig/<robotconfig_id>", views.deleterobotconfig, name="deleterobotconfig"),
    path("deletesubsystemconfig/<subconfig_id>", views.deletesubsystemconfig, name="deletesubsystemconfig"),
    path("deletesubsystem/<sub_id>", views.deletesubsystem, name="deletesubsystem"),
    path("editrobotconfig/<robotconfig_id>", views.editrobotconfig, name="editrobotconfig"),
    path("editsubsystemconfig/<subconfig_id>", views.editsubsystemconfig, name="editsubsystemconfig"),
    path("editsubsystem/<sub_id>", views.editsubsystem, name="editsubsystem"),
    path("activaterobotconfig/<robotconfig_id>", views.activaterobotconfig, name="activaterobotconfig"),
    path("activatesubsystemconfig/<subconfig_id>", views.activatesubsystemconfig, name="activatesubsystemconfig")
]