from django.shortcuts import render, get_object_or_404
from django.views import View

from main.models import *


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class TryoutView(View):
    def get(self, request):
        return render(request, 'tryouts.html')


class ClubsView(View):
    def get(self, request):
        context = {
            'clubs': Club.objects.all()
        }
        return render(request, 'clubs.html', context)


class PlayerView(View):
    def get(self, request):
        context = {
            'players': Player.objects.all()
        }
        return render(request, 'players.html', context)


class LatestTransfersView(View):
    def get(self, request):
        context = {
            'latest_transfers': Transfer.objects.order_by('-created_at')
        }
        return render(request, "latest-transfers.html", context)


class U20PlayersView(View):
    def get(self, request):
        context = {
            'u20_players': Player.objects.filter(age__lte=20).order_by('-price')
        }
        return render(request, "U-20players.html", context)


class ClubsDetailsView(View):
    def get(self, request, club_id):
        club = get_object_or_404(Club, id=club_id)
        players=Player.objects.filter(club=club)
        context={
            'players':players,
            'club':club
        }
        return render(request, 'club_details.html', context)
