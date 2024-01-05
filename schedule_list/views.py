from rest_framework.views import APIView
from django.http import HttpResponse
from schedule_list.models import Schedule

class ScheduleAddView(APIView):
    
    def post(self, request):
        host_name = request.data.get("host_name")
        guest_name = request.data.get("guest_name")
        date = request.data.get("date")
        memo = request.data.get("memo")
        
        Schedule.objects.create(
            host_name=host_name,
            guest_name=guest_name,
            date=date,
            memo=memo
            
        )
        return HttpResponse('일정이 등록되었습니다.')
