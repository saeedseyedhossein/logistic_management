from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from logistic import settings
import jwt


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # print('before view')
        if '/login' in request.path or '/register' in request.path or '/api-docs' in request.path:
            response = self.get_response(request)
        # print('after view')
            return response 
        
        token = request.headers.get('Authorization')
        try:
            payload = jwt.decode(
                jwt=token,
                algorithms=['HS256'],
                key=settings.JWT_KEY
            )
        except jwt.DecodeError:
            return JsonResponse({'ok':'False', 'error': 'Not authorized'}, safe=False, status=401)
            # return Response({
            #     'ok' : False,
            #     'error' : 'you are not authorized'
            # }, status=status.HTTP_401_UNAUTHORIZED)
        request.username = payload['username']
        request.com_id = payload['com_id']
        response = self.get_response(request)
        # print('after view')
        return response