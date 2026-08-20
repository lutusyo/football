from django.db import models
from apps.core.base_models import ActiveModel
from apps.football.models.season import Season
from apps.football.models.team import Team
from apps.core.choices import CompetitionTypeChoices

class Competition(ActiveModel):
    """
    A global football competition.

    Examples:
    - NBC Premier League
    - CAF Champions League
    - Tanzania Federation Cup
    """

    name = models.CharField(max_length=150,)
    short_name = models.CharField(max_length=50,blank=True,)
    country = models.CharField(max_length=100,blank=True,)
    competition_type= models.CharField(max_length=50,choices=CompetitionTypeChoices.choices,)

    class Meta:
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(fields=["name", "country"],name="unique_competition_per_country",)
        ]

    def __str__(self):
        return self.name


class CompetitionSeason(ActiveModel):
    """
    One edition of a competition during a global season.

    Example:
    NBC Premier League - 2025/2026
    """
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE,related_name="competition_seasons",)
    season = models.ForeignKey(Season,on_delete=models.CASCADE,related_name="competition_seasons",)

    class Meta:
        ordering = ["-season__start_date","competition__name",]

        constraints = [
            models.UniqueConstraint(fields=["competition","season",],name="unique_competition_season",
            )]

    def __str__(self):
        return (
            f"{self.competition.name} - "
            f"{self.season.name}"
        )


class TeamCompetitionEntry(ActiveModel):
    """
    A team participating in a particular competition season.

    Example:
    Azam FC → NBC Premier League → 2025/2026
    """
    competition_season = models.ForeignKey(CompetitionSeason,on_delete=models.CASCADE,related_name="participations",)
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="competition_participations",)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["competition_season","team",],name="unique_team_per_competition_season",)
        ]

    def __str__(self):
        return (
            f"{self.team} | "
            f"{self.competition_season}"
        )