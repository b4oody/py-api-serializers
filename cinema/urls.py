from django.urls import include, path
from rest_framework import routers

from cinema.views import (
    GenreViewSet,

)

router = routers.DefaultRouter()
router.register(r"genres", GenreViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
