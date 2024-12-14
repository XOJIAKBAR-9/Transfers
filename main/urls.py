from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('tryouts/', TryoutView.as_view(), name='tryouts'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:club_id>/', ClubsDetailsView.as_view(), name='clubs'),
    path('players/', PlayerView.as_view(), name='players'),
    path('latest_transfers/', LatestTransfersView.as_view(), name='latest_transfers'),
    path('u20_players/', U20PlayersView.as_view(), name='u20_players'),
]
