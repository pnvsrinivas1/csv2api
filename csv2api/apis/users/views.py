from rest_framework import viewsets
from django.contrib.auth.models import User

from csv2api.apis.users.serializers import UserSerializer
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer