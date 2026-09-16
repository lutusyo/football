from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from apps.organizations.models import Organization, Country
from apps.accounts.models import Membership
from apps.football.models import Team
from apps.core.choices import TeamCategoryChoices, AgeGroupChoices

User = get_user_model()

class TenantIsolationTests(APITestCase):

    def setUp(self):
        country = Country.objects.create(name="Tanzania")

        self.club_a = Organization.objects.create(name="Club A", short_name="CLA", slug = "club-a", country = country,)
        self.club_b = Organization.objects.create(name="Club B", short_name="CLB", slug = "club-b", country = country,)

        Team.objects.create(
            organization=self.club_a,
            name="Club A U17",
            short_name="A U17",
            category = TeamCategoryChoices.YOUTH,
            age_group = AgeGroupChoices.U17,
        )

        Team.objects.create(
            organization = self.club_b,
            name = "Club B U17",
            short_name = "B U17",
            category = TeamCategoryChoices.YOUTH,
            age_group = AgeGroupChoices.U17,
        )

        self.user = User.objects.create_user(
            email="analyst@cuba.com",
            password="TestPass123",
        )

        Membership.objects.create(
            user = self.user,
            organization = self.club_a,
            role = Membership.RoleChoices.ANALYST,
        )

        self.client.force_authenticate(user=self.user)

    def test_user_only_sees_own_organization_teams(self):
        response = self.client.get("/api/teams/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Club A U17")