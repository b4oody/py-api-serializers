from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
