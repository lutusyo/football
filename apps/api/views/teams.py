from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.football.models.team import Team
from ..serializers.teams import TeamSerializer

class TeamViewSet(ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer