from datetime import date
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from apps.organizations.models import Country, Organization
from apps.accounts.models import  Membership
from apps.football.models import ( Competition, CompetitionSeason, Season, Team, Venue)
from apps.matches.models import Match
from apps.core.choices import TeamCategoryChoices, AgeGroupChoices

User = get_user_model()


class MatchIsolationTests(APITestCase):

    def setUp(self):
        country = Country.objects.create(name="Tanzania")

        self.club_a = Organization.objects.create(name="Club A", short_name = "CLA", slug = "club-a", country = country,)
        self.club_b = Organization.objects.create(name="Club B", short_name = "CLB", slug = "club-b", country = country,)

        self.team_a = Team.objects.create(organization = self.club_a, name = "Club A U17", short_name ="A U17", category = TeamCategoryChoices.YOUTH, age_group = AgeGroupChoices.U17,)
        self.team_b = Team.objects.create(organization = self.club_b, name = "Club B U17", short_name ="B U17", category = TeamCategoryChoices.YOUTH, age_group = AgeGroupChoices.U17,)

       
        self.season = Season.objects.create(name="2026/27", start_date=date(2026, 7, 1),end_date=date(2027, 6, 30),)
        competition = Competition.objects.create(name="Test League", short_name="TL",)
        competition_season = CompetitionSeason.objects.create(competition=competition, season=self.season,)

        Match.objects.create(competition_season=competition_season, home_team=self.team_a, away_team=self.team_b, kickoff=timezone.now(),)

        self.user = User.objects.create_user(email="analyst@cluba.com",password="TestPass123",)

        Membership.objects.create(user=self.user, organization=self.club_a, role=Membership.RoleChoices.ANALYST,)
        self.client.force_authenticate(user=self.user)

    def test_user_can_see_match_involving_own_organization(self):
        response = self.client.get("/api/matches/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
              