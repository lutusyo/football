# apps/api/urls.py

from rest_framework.routers import DefaultRouter
from .views.teams import TeamViewSet
from .views.players import PlayerViewSet
from .views.matches import MatchViewSet

router = DefaultRouter()
router.register("teams", TeamViewSet, basename="teams")
router.register("players", PlayerViewSet, basename="players")
router.register("matches", MatchViewSet, basename="matches")


urlpatterns = router.urls
