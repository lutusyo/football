from rest_framework.test import APITestCase
from rest_framework import status

class TeamAPITests(APITestCase):

    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)