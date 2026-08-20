from django.shortcuts import render


NAV_ITEMS = [
    ('Home', 'home'), ('Matches', 'matches'), ('Teams', 'teams'),
    ('Leagues', 'leagues'), ('Tables', 'tables'), ('Reports', 'reports'),
    ('Organization', 'organization'),
]

TEAMS = [
    {'name': 'Azam FC', 'short': 'AZM', 'form': 'WWDWW', 'points': 52, 'played': 24, 'logo': 'A'},
    {'name': 'Simba SC', 'short': 'SIM', 'form': 'WWWLW', 'points': 50, 'played': 24, 'logo': 'S'},
    {'name': 'Young Africans', 'short': 'YGA', 'form': 'WDWWW', 'points': 47, 'played': 24, 'logo': 'Y'},
    {'name': 'Singida Black Stars', 'short': 'SBS', 'form': 'LDWDW', 'points': 39, 'played': 24, 'logo': 'B'},
]

MATCHES = [
    {'id': 1, 'date': 'Today · 18:00', 'competition': 'NBC Premier League', 'home': 'Azam FC', 'away': 'Simba SC', 'score': '—', 'status': 'UPCOMING'},
    {'id': 2, 'date': 'Yesterday', 'competition': 'NBC Premier League', 'home': 'Young Africans', 'away': 'Azam FC', 'score': '1 — 2', 'status': 'FINISHED'},
    {'id': 3, 'date': '16 Aug 2026', 'competition': 'Federation Cup', 'home': 'Azam FC', 'away': 'Singida Black Stars', 'score': '3 — 0', 'status': 'FINISHED'},
]

PLAYERS = [
    {'id': 1, 'name': 'Feisal Salum', 'position': 'Midfielder', 'number': 10, 'goals': 9, 'assists': 7, 'apps': 22},
    {'id': 2, 'name': 'Prince Dube', 'position': 'Forward', 'number': 9, 'goals': 12, 'assists': 4, 'apps': 23},
    {'id': 3, 'name': 'Mamadou Doumbia', 'position': 'Defender', 'number': 5, 'goals': 2, 'assists': 3, 'apps': 21},
]


def base_context(active):
    return {
        'nav_items': NAV_ITEMS, 'active': active, 'teams': TEAMS,
        'matches_list': MATCHES, 'players': PLAYERS,
        'organization': {'name': 'Azam Football Club', 'short_name': 'AZAM FC', 'city': 'Dar es Salaam', 'founded': '2004'},
    }


def home(request):
    context = base_context('home')
    context['page_title'] = 'Club dashboard'
    return render(request, 'portal/home.html', context)


def matches(request):
    context = base_context('matches')
    context['page_title'] = 'Matches'
    return render(request, 'portal/matches.html', context)


def teams(request):
    context = base_context('teams')
    context['page_title'] = 'Teams'
    return render(request, 'portal/teams.html', context)


def leagues(request):
    context = base_context('leagues')
    context['page_title'] = 'Leagues & competitions'
    context['leagues'] = [
        {'name': 'NBC Premier League', 'type': 'League', 'country': 'Tanzania', 'clubs': 16},
        {'name': 'Federation Cup', 'type': 'Cup', 'country': 'Tanzania', 'clubs': 32},
        {'name': 'CAF Champions League', 'type': 'Tournament', 'country': 'Africa', 'clubs': 16},
    ]
    return render(request, 'portal/leagues.html', context)


def tables(request):
    context = base_context('tables')
    context['page_title'] = 'League table'
    return render(request, 'portal/tables.html', context)


def player_profile(request, player_id):
    context = base_context('teams')
    context['player'] = next((player for player in PLAYERS if player['id'] == player_id), PLAYERS[0])
    context['page_title'] = context['player']['name']
    return render(request, 'portal/player_profile.html', context)


def match_report(request, match_id):
    context = base_context('matches')
    context['match'] = next((item for item in MATCHES if item['id'] == match_id), MATCHES[1])
    context['page_title'] = 'Match report'
    return render(request, 'portal/match_report.html', context)


def reports(request):
    context = base_context('reports')
    context['page_title'] = 'Reports centre'
    return render(request, 'portal/reports.html', context)


def organization(request):
    context = base_context('organization')
    context['page_title'] = 'Organization'
    return render(request, 'portal/organization.html', context)
