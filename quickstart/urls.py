from django.urls import path, include
from rest_framework import routers
from .views import GroupViewSets, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSets)

urlpatterns = [
    path('rest/',include(router.urls)),
]