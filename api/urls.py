from django.urls import path
from api.views import LoginView, RegisterView, Test

urlpatterns = [
    path('register/',RegisterView.as_view({'post' : 'register_company'})),
    path('login/',LoginView.as_view({'post' : 'login_company'})),
    path('test/',Test.as_view({'get' : 'test'})),
]