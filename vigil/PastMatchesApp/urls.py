from django.urls import path
from . import views

urlpatterns = [
    path("pastmatches/", views.pastmatches, name="pastmatches")
]