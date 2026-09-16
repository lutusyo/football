from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from apps.organizations.models import Country, Organization
from apps.accounts.models import Membership
from apps.football.models import ( Person, PlayerProfile, PlayerRegistration, Season, Team,)
from apps.core.choices import (FootChoices, GenderChoices, RegistrationStatusChoices,
    RegistrationTypeChoices, TeamCategoryChoices, AgeGroupChoices,
)

User = get_user_model()


class PlayerIsolationTests(APITestCase):

    def setUp(self):
        country = Country.objects.create(name="Tanzania")

        self.club_a = Organization.objects.create(name="Club A", short_name="CLA", slug = "club-a", country = country,)
        self.club_b = Organization.objects.create(name="Club B", short_name="CLB", slug = "club-b", country = country,)

        self.team_a = Team.objects.create(organization=self.club_a,
            name="Club A U17", short_name="A U17",
            category=TeamCategoryChoices.YOUTH, age_group=AgeGroupChoices.U17,
        )

        self.team_b = Team.objects.create(organization=self.club_b,
            name="Club B U17", short_name="B U17",
            category=TeamCategoryChoices.YOUTH, age_group=AgeGroupChoices.U17,
        )

        self.season = Season.objects.create(
            name="2026/27",
            start_date=date(2026, 7, 1),
            end_date=date(2027, 6, 30),
        )

        person_a = Person.objects.create(
            first_name="Player", last_name="A",
            gender=GenderChoices.MALE,
            date_of_birth=date(2009, 1, 1),
            nationality=country,
        )

        person_b = Person.objects.create(
            first_name="Player", last_name="B",
            gender=GenderChoices.MALE,
            date_of_birth=date(2009, 2, 1),
            nationality=country,
        )

        player_a = PlayerProfile.objects.create(person=person_a,preferred_foot=FootChoices.RIGHT,)
        player_b = PlayerProfile.objects.create(person=person_b, preferred_foot=FootChoices.RIGHT,)

        PlayerRegistration.objects.create(
            player=player_a,
            organization=self.club_a,
            team=self.team_a,
            season=self.season,
            start_date=date(2026, 7, 1),
            registration_type=RegistrationTypeChoices.PERMANENT,
            status=RegistrationStatusChoices.ACTIVE,
            is_current=True,
        )

        PlayerRegistration.objects.create(
            player=player_b,
            organization=self.club_b,
            team=self.team_b,
            season=self.season,
            start_date=date(2026, 7, 1),
            registration_type=RegistrationTypeChoices.PERMANENT,
            status=RegistrationStatusChoices.ACTIVE,
            is_current=True,
        )

        self.user = User.objects.create_user(
            email="analyst@cluba.com",
            password="TestPass123",
        )

        Membership.objects.create(
            user=self.user,
            organization=self.club_a,
            role=Membership.RoleChoices.ANALYST,
        )

        self.client.force_authenticate(user=self.user)

    def test_user_only_sees_own_organization_players(self):
        response = self.client.get("/api/players/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        player = PlayerProfile.objects.get(
            registrations__organization=self.club_a
        )

        self.assertEqual(response.data[0]["id"], str(player.id))