from rest_framework.response import Response
from user.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer

class UserDetailView(APIView):
    def get(self, request, user_id:int):
        user_detail = User.objects.get(id=user_id)
        serializer = UserSerializer(user_detail)
        return Response(serializer.data)
