from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
from django.db import models

admin.site.unregister(User)
admin.site.unregister(Group)


class ClubInline(admin.StackedInline):
    model = Club  # Fix typo here
    extra = 1


class PlayerInline(admin.StackedInline):
    model = Player
    extra = 1


class TransferInline(admin.StackedInline):
    model = Transfer
    extra = 1


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = (ClubInline,)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'president', 'coach', 'found_date', 'country')
    search_fields = ('name', 'president',)
    list_filter = ('country',)
    inlines = (PlayerInline,)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'age', 'price', 'number', 'club',)
    search_fields = ('name', 'position', 'number',)
    list_filter = ('club', 'country',)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = (TransferInline,)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('club_old', 'club_new', 'player', 'price', 'price_tft', 'season',)
    search_fields = ('player__name', 'club_old__name', 'club_new__name', 'season__name',)
    list_filter = ('club_old', 'club_new', 'season', 'player')
