from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.matches.models import Match
from ..serializers.matches import MatchSerializer

class MatchViewSet(ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer