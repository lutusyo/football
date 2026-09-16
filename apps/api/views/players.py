from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.football.models import PlayerProfile
from ..serializers.players import PlayerSerializer
from rest_framework.permissions import IsAuthenticated

class PlayerViewSet(ReadOnlyModelViewSet):
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlayerProfile.objects.filter(
            registrations__organization__memberships__user = self.request.user,
            registrations__organization__memberships__is_active = True,
            registrations__is_current = True,
        ).distinct()