from rest_framework import serializers
from apps.football.models import PlayerProfile

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = "__all__"