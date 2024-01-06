from rest_framework.views import APIView
from django.http import HttpResponse
from schedule_list.models import Schedule, GuestSpace
from user.models import User
from django.db.models import Q
from .serializers import ScheduleListSerializer
from rest_framework.response import Response

# ToDo: 약속에서 사람빠지기, 사람 추가, 좋아요
class ScheduleAddView(APIView):
    
    def post(self, request):
        invite_name = request.data.get("host_name")
        invited_name = request.data.get("guest_name")
        date = request.data.get("date")
        memo = request.data.get("memo")
        
        invite_id = User.objects.get(username=invite_name)
        invited_id = User.objects.get(username=invited_name)

        schedule_obj = Schedule.objects.create(
            host_id=invite_id.pk,
            guest_id=invited_id.pk,
            date=date,
            memo=memo
        )

        try:
            invited_user = User.objects.get(username=invited_name)
        except User.DoesNotExist:
            return HttpResponse('초대받은 사람이 존재하지 않습니다.', status=400)
        GuestSpace.objects.create(
            schedule=schedule_obj,
            user=invited_user
        )
        return HttpResponse('일정이 등록되었습니다.')

class ScheduleListView(APIView):
    def get(self, request, user_id: int):

        guest_space_list = GuestSpace.objects.filter(Q(user_id=user_id) | Q(schedule__host_id=user_id))
        serializers = ScheduleListSerializer(guest_space_list, many=True)
        return Response(serializers.data)