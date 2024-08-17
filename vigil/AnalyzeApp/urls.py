from django.urls import path
from . import views

urlpatterns = [
    path("analyze/", views.analyze, name="analyze"),
    path("analyzematch/", views.analyzematch, name="analyzematch"),
    path("analyzematch/<str:subsystem>/<str:fault_idx>/", views.analyzematchswitch, name="analyzematchswitch"),
    path("pastmatches/", views.pastmatches, name="pastmatches"),
    path("editmatch/<match_id>", views.editmatch, name="editmatch"),
    path("deletematch/<match_id>", views.deletematch, name="deletematch"),
    path("openmatch/<match_id>", views.openmatch, name="openmatch")
]