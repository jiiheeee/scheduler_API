from rest_framework.views import APIView
from django.http import HttpResponse
from schedule_list.models import Schedule, GuestSpace
from user.models import User

class ScheduleAddView(APIView):
    
    def post(self, request):
        invite_name = request.data.get("host_name")
        invited_name = request.data.get("guest_name")
        date = request.data.get("date")
        memo = request.data.get("memo")
        
        schedule_obj = Schedule.objects.create(
            host_name=invite_name,
            guest_name=invited_name,
            date=date,
            memo=memo
        )
        schedule_id = schedule_obj.pk
        try:
            invited_user = User.objects.get(username=invited_name)
        except User.DoesNotExist:
            return HttpResponse('초대받은 사람이 존재하지 않습니다.', status=400)
        
        GuestSpace.objects.create(
            schedule_number=schedule_obj,
            user_id=invited_user
        )

        return HttpResponse('일정이 등록되었습니다.')
    
