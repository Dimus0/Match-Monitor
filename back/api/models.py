from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    coach = models.CharField(max_length=100)
    stadium_into_training = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name

class Match(models.Model):
    date = models.DateTimeField()
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    goal_score_home_team = models.IntegerField()
    goal_score_away_team = models.IntegerField()
    name_of_referee = models.CharField(max_length=100)
    stadium = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.home_team.team_name} vs {self.away_team.team_name}"