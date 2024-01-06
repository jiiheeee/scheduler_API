from django.http import HttpResponse
from user.models import User
from rest_framework.views import APIView
from user.models import User

# ToDo: 로그인
# 
class SignUpView(APIView):
    def post(self, request):
        name = request.data.get("name")
        password = request.data.get('password')
        mail = request.data.get('mail')

        existing_user = User.objects.filter(mail=mail).first()

        if existing_user:
            return HttpResponse("이미 존재하는 이메일입니다.")
        else:
            User.objects.create(
                username=name, 
                password=password, 
                mail=mail, 
                is_active=True
            )
            return HttpResponse('회원가입이 완료되었습니다.')