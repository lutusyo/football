from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.matches.models import (
    Match,
    MatchLineup,
    MatchAppearance,
)

from apps.reference.models.position import Position

from apps.football.models.team import Team
from apps.football.models.player_registration import PlayerRegistration
from apps.football.models.person import Person
from apps.football.models.player_profile import PlayerProfile
from apps.football.models.competition import (
    CompetitionSeason,
    Competition,
)
from apps.football.models.season import Season

from apps.organizations.models import Country, Organization

from apps.core.choices import (
    CompetitionTypeChoices,
    TeamCategoryChoices,
    PositionLineChoices,
    PositionSideChoices,
    GenderChoices,
    FootChoices,
    MatchPeriodChoices,
)


class MatchModelTests(TestCase):

    def setUp(self):

        self.country = Country.objects.create(
            name="Tanzania",
            code="TZ",
        )

        self.organization = Organization.objects.create(
            name="Test Organization",
            short_name="TEST",
            slug="test-organization",
            country=self.country,
        )

        self.competition = Competition.objects.create(
            name="Test League",
            country="Tanzania",
            competition_type=CompetitionTypeChoices.LEAGUE,
        )

        self.team = Team.objects.create(
            organization=self.organization,
            name="Test FC",
            short_name="TFC",
            category=TeamCategoryChoices.SENIOR,
        )

        self.season = Season.objects.create(
            name="2026/2027",
            start_date="2026-08-01",
            end_date="2027-07-31",
        )

        self.competition_season = CompetitionSeason.objects.create(
            competition=self.competition,
            season=self.season,
        )

        self.opponent = Team.objects.create(
            organization=self.organization,
            name="Opponent FC",
            short_name="OFC",
            category=TeamCategoryChoices.SENIOR,
        )

        self.person = Person.objects.create(
            first_name="Test",
            last_name="Player",
            gender=GenderChoices.MALE,
            date_of_birth="2005-01-01",
            nationality=self.country,
        )

        self.player_profile = PlayerProfile.objects.create(
            person=self.person,
            preferred_foot=FootChoices.RIGHT,
        )

        self.registration = PlayerRegistration.objects.create(
            player=self.player_profile,
            organization=self.organization,
            team=self.team,
            season=self.season,
            start_date="2026-08-01",
        )

        self.match = Match.objects.create(
            competition_season=self.competition_season,
            home_team=self.team,
            away_team=self.opponent,
            kickoff="2026-08-10T15:00:00Z",
        )

        self.lineup = MatchLineup.objects.create(
            match=self.match,
            player_registration=self.registration,
            shirt_number=10,
        )

        self.position = Position.objects.create(
            name="Central Midfielder",
            short_name="CM",
            line=PositionLineChoices.MIDFIELD,
            side=PositionSideChoices.CENTER,
        )

        self.appearance = MatchAppearance.objects.create(
            lineup=self.lineup,
            position=self.position,
            entered_period=MatchPeriodChoices.FIRST_HALF,
            entered_second=0,
        )

    def test_match_created(self):
        self.assertEqual(self.match.home_team, self.team)
        self.assertEqual(self.match.away_team, self.opponent)

    def test_match_lineup_belongs_to_match(self):
        self.assertEqual(self.match.lineups.count(), 1)
        self.assertEqual(self.match.lineups.first(), self.lineup)

    def test_event_relationship_exists(self):
        self.assertEqual(self.appearance.events.count(), 0)

    def test_exit_time_cannot_be_before_entry_time(self):
        appearance = MatchAppearance(
            lineup=self.lineup,
            position=self.position,
            entered_period=MatchPeriodChoices.FIRST_HALF,
            entered_second=3600,
            exited_period=MatchPeriodChoices.FIRST_HALF,
            exited_second=3000,
        )

        with self.assertRaises(ValidationError):
            appearance.full_clean()