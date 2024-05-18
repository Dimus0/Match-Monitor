from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
router = DefaultRouter()
router.register('matches', MatchesViewset, basename='matches')

urlpatterns = [
    path('search/',MatchesViewset.as_view({'post':'search'}),name='search'),
    path('matches/', MatchesViewset.as_view({'get': 'list'}), name='matches'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls