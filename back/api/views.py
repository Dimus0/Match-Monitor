from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from rest_framework import viewsets, permissions,status
from .models import *
from .serialezers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model,login,logout
from rest_framework import generics
from django.db.models import Q
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MatchesViewset(viewsets.ViewSet):
    permissions_classes = [permissions.AllowAny]
    queryset = Match.objects.all()
    serializers_class = MatchSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializers_class(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
    
    @action(detail=False, methods=['post'])
    def search(self, request):
        serializer = MatchSearchSerializer(data=request.data)
        if serializer.is_valid():
            home_team_name = serializer.validated_data.get('home_team_name')
            away_team_name = serializer.validated_data.get('away_team_name')
            date = serializer.validated_data.get('date')
            stadium = serializer.validated_data.get('stadium')
            home_team_obj = Team.objects.filter(team_name__icontains=home_team_name).first()
            away_team_obj = Team.objects.filter(team_name__icontains=away_team_name).first()
            if home_team_obj and away_team_obj:
                matches = Match.objects.filter(
                    Q(home_team=home_team_obj, away_team=away_team_obj) |
                    Q(home_team=away_team_obj, away_team=home_team_obj),
                    date=date,  # Додано фільтрацію за датою
                    stadium=stadium
                )
                serialized_matches = MatchSerializer(matches, many=True)
                return Response(serialized_matches.data)
            else:
                return Response({'error': 'Teams not found'}, status=404)
        else:
            return Response(serializer.errors, status=400)

        
    def retrieve(self, request, pk=None):
        match = self.queryset.get(pk=pk)
        serializer = self.serializers_class(match)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        match = self.queryset.get(pk=pk)
        serializers = self.serializers_class(match,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=400)
        
    def destroy(self, request, pk=None):
        match = self.queryset.get(pk=pk)
        match.delete()
        return Response(status=204)
    
class TeamsViewset(viewsets.ViewSet):
    permissions_classes = [permissions.AllowAny]
    queryset = Team.objects.all()
    serializers_class = TeamSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializers_class(queryset, many=True)
        return Response(serializer.data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)