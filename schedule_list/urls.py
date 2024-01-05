from django.urls import path
from .views import ScheduleAddView

urlpatterns = [
    path("add/", ScheduleAddView.as_view()),
]