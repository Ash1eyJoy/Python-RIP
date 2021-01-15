from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Club


class FootballView(View):
    def get(self, request):
        clubs = Club.objects.all()
        return render(request, "footballs/football_list.html", {"club_list": clubs})