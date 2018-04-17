from django.urls import include
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/token/obtain/', obtain_jwt_token),
    path('api/v1/', include('tcase.api.urls')),
]
