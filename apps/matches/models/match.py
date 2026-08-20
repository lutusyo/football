from django.db import models
from apps.core.base_models import ActiveModel
from apps.core.choices import MatchStatusChoices
from apps.football.models.team import Team
from apps.football.models.venue import Venue
from apps.football.models.competition import CompetitionSeason

class Match(ActiveModel):
    """
    Represents one football match.
    """

    competition_season = models.ForeignKey(CompetitionSeason,on_delete=models.PROTECT,related_name="matches",)
    home_team = models.ForeignKey(Team,on_delete=models.PROTECT,related_name="home_matches",)
    away_team = models.ForeignKey(Team,on_delete=models.PROTECT,related_name="away_matches",)
    venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,null=True,blank=True,related_name="matches",)
    matchday = models.PositiveSmallIntegerField(blank=True,null=True,)
    kickoff = models.DateTimeField()
    status = models.CharField(max_length=20,choices=MatchStatusChoices.choices,default=MatchStatusChoices.SCHEDULED,)
    home_score = models.PositiveSmallIntegerField(default=0,)
    away_score = models.PositiveSmallIntegerField(default=0,)
    attendance = models.PositiveIntegerField(blank=True,null=True,)
    notes = models.TextField(blank=True,)

    class Meta:
        ordering = ["-kickoff"]

    def __str__(self):
        return (
            f"{self.home_team} "
            f"{self.home_score}-{self.away_score} "
            f"{self.away_team}"
        )
    