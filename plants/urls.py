from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('rooms', views.RoomViewSet, basename='room')
router.register('plants', views.PlantViewSet, basename='plant')
router.register('userplants',
                views.UserPlantViewSet, basename='userplant')


urlpatterns = [
    path('profile/', views.ProfileRetrieveView.as_view(), name='profile'),
    path('', include(router.urls)),
]
