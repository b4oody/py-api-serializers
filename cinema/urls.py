from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
