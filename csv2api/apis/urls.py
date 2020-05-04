from django.urls import include
from django.conf.urls import url
from rest_framework import routers

from csv2api.apis.users.views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls), name='api_index'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]