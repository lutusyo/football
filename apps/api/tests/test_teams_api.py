from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()

class TeamAPITests(APITestCase):

    def test_teams_require_authentication(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_access_teams(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="TestPass123"
        )
        self.client.force_authenticate(user=user)
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)



