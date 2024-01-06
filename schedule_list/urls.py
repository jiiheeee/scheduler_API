from django.urls import path
from .views import ScheduleAddView, ScheduleListView

urlpatterns = [
    path("add/", ScheduleAddView.as_view()),
    path("<int:user_id>", ScheduleListView.as_view())
]