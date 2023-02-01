from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet.as_view({'get': 'list'}))
router.register(r'groups', views.GroupViewSet.as_view({'get': 'list'}))
router.register(r'country', views.CountryViewSet.as_view({'get': 'list'}))


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
