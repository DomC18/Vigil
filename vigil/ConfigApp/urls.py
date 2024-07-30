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
]