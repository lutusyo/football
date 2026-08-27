# apps/api/urls.py

from rest_framework.routers import DefaultRouter
from .views.teams import TeamViewSet

router = DefaultRouter()
router.register("teams", TeamViewSet, basename="teams")

urlpatterns = router.urls
