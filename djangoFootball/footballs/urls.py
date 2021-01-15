from django.urls import path

from . import views

urlpatterns = [
    path("", views.FootballView.as_view())
]