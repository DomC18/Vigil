from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('MembersApp.urls'))
]