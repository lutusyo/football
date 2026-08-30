from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.football.models import PlayerProfile
from ..serializers.players import PlayerSerializer

class PlayerViewSet(ReadOnlyModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerSerializer