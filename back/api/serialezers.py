from django.forms import ValidationError
from rest_framework import serializers
from .models import Team, Match
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model,authenticate


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']

class MatchSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['id', 
                  'date', 
                  'home_team',
                   'away_team', 
                  'goal_score_home_team', 
                  'goal_score_away_team', 
                  'name_of_referee']

class MatchSearchSerializer(serializers.Serializer):
    home_team_name = serializers.CharField()
    away_team_name = serializers.CharField()
