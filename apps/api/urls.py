# apps/api/urls.py

from rest_framework.routers import DefaultRouter
from .views.teams import TeamViewSet
from .views.players import PlayerViewSet
from .views.matches import MatchViewSet
from .views.organizations import OrganizationViewSet
from django.urls import path, include
from .views.me import MeView

router = DefaultRouter()
router.register("teams", TeamViewSet, basename="teams")
router.register("players", PlayerViewSet, basename="players")
router.register("matches", MatchViewSet, basename="matches")
router.register("organizations", OrganizationViewSet, basename="organizations")


urlpatterns = [
    path("auth/", include("apps.api.auth_urls")),
    path("auth/me/", MeView.as_view(), name="me"),
    *router.urls,
]
