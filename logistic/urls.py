
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title = "Logistic Management API",
        default_version= "v1",
        # description= "Test swagger first blog",
        # terms_of_service= "localhost",
        # contact=openapi.Contact(email='ff@hotmail.com'),
    ),
    # public=True,
    # permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-docs/', schema_view.with_ui()),
]
