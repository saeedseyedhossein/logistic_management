import datetime
import hashlib
import jwt
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializer import CompanySerializer
from logistic import settings

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        serializer = CompanySerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'ok' : False, 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        try:
            password = hashlib.md5(password.encode()).hexdigest()
            instance = Company.objects.get(username=username, password=password)
        except Company.DoesNotExist:
            return Response({'ok' : False, 'error' : 'Password or Username is incorrect.' }, status=status.HTTP_401_UNAUTHORIZED)
        
        token = jwt.encode(
            key=settings.JWT_KEY,
            algorithm='HS256',
            payload={'com_id' : instance.id,
                     'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                     'iat' : datetime.datetime.utcnow()}
        )
        response = Response(status=status.HTTP_200_OK)
        response.data = {'ok' : True, 'token' : token}
        response.set_cookie(key='token', value=token, httponly=True)

        return response
    
class Test(ModelViewSet):
    def test(self, request):
        return Response({'test passed. you are logged in.'})