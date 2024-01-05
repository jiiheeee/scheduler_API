from django.http import HttpResponse
from user.models import User
from rest_framework.views import APIView
from user.models import User


class SignUpView(APIView):
    def post(self, request):
        name = request.data.get("name")
        password = request.data.get('password')
        mail = request.data.get('mail')

        User.objects.create(
            user_name=name, 
            password=password, 
            mail=mail, 
            is_active=True
        )
        return HttpResponse('회원가입이 완료되었습니다.')
    



    
