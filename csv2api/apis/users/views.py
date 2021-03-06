from rest_framework import viewsets
from django.contrib.auth.models import User

from csv2api.apis.users.serializers import UserSerializer
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer