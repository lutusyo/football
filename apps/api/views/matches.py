from django.db import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.matches.models import Match
from ..serializers.matches import MatchSerializer

class MatchViewSet(ReadOnlyModelViewSet):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Match.objects.filter(
            models.Q(
                home_team__organization__memberships__user=self.request.user,
                home_team__organization__memberships__is_active=True,
            ) |
            models.Q(
                away_team__organization__memberships__user=self.request.user,
                away_team__organization__memberships__is_active=True,
            )
        ).distinct()