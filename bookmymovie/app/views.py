from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from bookmymovie.app.models import Screen
from bookmymovie.app.serializers import UserSerializer, ScreenSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ScreenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Screen.objects.all().order_by('-name')
    serializer_class = ScreenSerializer
