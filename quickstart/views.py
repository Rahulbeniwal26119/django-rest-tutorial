from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    End point that allow user to be viewed and edited"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSets(viewsets.ModelViewSet):
    """
    End that allow a group be viewed and edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]