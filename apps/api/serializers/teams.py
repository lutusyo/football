from rest_framework import serializers
from apps.football.models.team import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"