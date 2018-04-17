from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.conf.urls import url, include
from .viewsets import PostViewSet, LikeViewSet, UserViewSet

# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)
schema_view = get_schema_view()

# URLs настраиваются автоматически роутером
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^schema/$', schema_view)
]
