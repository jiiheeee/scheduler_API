from django.urls import path
from .views import ScheduleAddView, ScheduleListView, GuestDeleteView, GuestAddView, ScheduleLikeView, ScheduleDetailView

urlpatterns = [
    path("add/", ScheduleAddView.as_view()),
    path("<int:user_id>", ScheduleListView.as_view()),
    path("guest/delete/<int:schedule_id>/<int:user_id>", GuestDeleteView.as_view()),
    path("guest/add/", GuestAddView.as_view()),
    path("detail/", ScheduleDetailView.as_view()),
    path("like/", ScheduleLikeView.as_view())
]