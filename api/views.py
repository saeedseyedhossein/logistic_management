from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializer import CompanySerializer

from .models import Company
# Create your views here.
class RegisterView(ModelViewSet):
    def register_company(self, request):
        serializer = CompanySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'ok' : False, 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'ok' : True, 'company' : serializer.data}, status=status.HTTP_201_CREATED)

        # return Response({'yo'},status=status.HTTP_508_LOOP_DETECTED)

class LoginView(ModelViewSet):
    def login_company(self, request):
        pass

