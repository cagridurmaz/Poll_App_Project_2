from django.urls import path
from . import views

app_name = "PollApp"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("poll/<int:poll_id>/", views.poll_view, name="poll"),
]
