from rest_framework.views import APIView
from django.http import HttpResponse
from schedule_list.models import Schedule, GuestSpace
from user.models import User
from django.db.models import Q
from .serializers import ScheduleListSerializer
from rest_framework.response import Response
from schedule_list.models import Schedule,ScheduleLike

class ScheduleAddView(APIView):
    def post(self, request):
        invite_name = request.data.get("host_name")
        invited_name = request.data.get("guest_name")
        date = request.data.get("date")
        memo = request.data.get("memo")
        
        invite_id = User.objects.get(username=invite_name)

        schedule_obj = Schedule.objects.create(
            host_id=invite_id.pk,
            date=date,
            memo=memo
        )
        invited_user = User.objects.get(username=invited_name)
        GuestSpace.objects.create(
            schedule=schedule_obj,
            user=invited_user
        )
        return HttpResponse('일정이 등록되었습니다.')

class ScheduledeleteView(APIView):
    def get(self, request, schedule_id: int):
        delete_schedule = Schedule.objects.get(id=schedule_id)
        delete_guest = GuestSpace.objects.get(schedule_id=schedule_id)
        
class GuestDeleteView(APIView):
    def get(self, request, schedule_id: int, user_id: int):
        try:
            guestspace_delete = GuestSpace.objects.get(schedule_id=schedule_id, user_id=user_id)
        except Exception as e:
            return HttpResponse("삭제를 실패했습니다.", status=400)
        guestspace_delete.delete()
        return HttpResponse("일정을 삭제하였습니다.", status=200)
    
class GuestAddView(APIView):
    def post(self, request):
        schedule_id = request.data.get("schedule_id")
        guest_id = request.data.get("guest_id")
        existing_schedule = Schedule.objects.filter(id=schedule_id)

        if existing_schedule:
            GuestSpace.objects.create(
                schedule_id=schedule_id,
                user_id=guest_id
            )
            return HttpResponse("인원을 추가하였습니다.")
        else:
            return HttpResponse("존재하지 않는 일정입니다.")
    
class ScheduleListView(APIView):
    def get(self, request, user_id: int):
        guest_space_list = GuestSpace.objects.filter(Q(user_id=user_id) | Q(schedule__host_id=user_id))
        serializers = ScheduleListSerializer(guest_space_list, many=True)
        return Response(serializers.data)

class ScheduleDetailView(APIView):
    def get(self, request, schedule_id: int):
        schedule_detail = Schedule.objects.get(id=schedule_id)
        serializers = ScheduleListSerializer(schedule_detail)
        return Response(serializers.data)

class ScheduleLikeView(APIView):
    def post(self, request):
        schedule_id = request.data.get("schedule_id")
        user_id = request.data.get("user_id")
        ScheduleLike.objects.create(
            schedule_id=schedule_id,
            user_id=user_id
        )
        return HttpResponse("좋아요.")