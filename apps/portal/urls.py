from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('matches/', views.matches, name='matches'),
    path('teams/', views.teams, name='teams'),
    path('leagues/', views.leagues, name='leagues'),
    path('tables/', views.tables, name='tables'),
    path('players/<int:player_id>/', views.player_profile, name='player-profile'),
    path('match-report/<int:match_id>/', views.match_report, name='match-report'),
    path('reports/', views.reports, name='reports'),
    path('organization/', views.organization, name='organization'),
]
