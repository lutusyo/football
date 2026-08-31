from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.football.models import Team
from ..serializers.teams import TeamSerializer

class TeamViewSet(ReadOnlyModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Team.objects.filter(
            organization__memberships__user=self.request.user,
            organization__memberships__is_active = True
        ).distinct()

