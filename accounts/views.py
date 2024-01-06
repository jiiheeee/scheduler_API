from django.http import HttpResponse
from user.models import User
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response
 
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
        
class LoginView(APIView):
    def post(self, request):
        user_email = request.data.get("email")
        user_password = request.data.get("password")

        try:
            login_data = User.objects.get(mail=user_email, password=user_password)
            if login_data:
                serializers = UserSerializer(login_data)
                return Response(serializers.data)
        except User.DoesNotExist:
            return HttpResponse("이메일 혹은 비밀번호를 확인해주세요.", status=400)