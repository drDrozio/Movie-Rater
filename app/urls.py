from app.views import MovieViewSet, RatingViewSet, UserViewSet
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('movies',MovieViewSet)
router.register('ratings',RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
