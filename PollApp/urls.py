from django.urls import path
from . import views

app_name = "PollApp"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("poll/<int:poll_id>/", views.poll_view, name="poll"),
    path("poll_result/<int:poll_id>/", views.poll_result_view, name="poll_result"),
]
