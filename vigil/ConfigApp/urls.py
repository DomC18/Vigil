from django.urls import path
from . import views

urlpatterns = [
    path("config/", views.config, name="config"),
    # path("selectcurrentconfig/", views.selectcurrentconfig, name="selectcurrentconfig"),
    path("newrobotconfig/", views.newrobotconfig, name="newrobotconfig"),
    path("newsubsystemconfig/", views.newsubsystemconfig, name="newsubsystemconfig"),
    path("newsubsystem/", views.newsubsystem, name="newsubsystem"),
]