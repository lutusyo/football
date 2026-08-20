from django.db import models

class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class FootChoices(models.TextChoices):
    RIGHT = "RIGHT", "Right"
    LEFT = "LEFT", "Left"
    BOTH = "BOTH", "Both"

class TeamCategoryChoices(models.TextChoices):
    SENIOR = "SENIOR", "Senior"
    RESERVE = "RESERVE", "Reserve"
    YOUTH = "YOUTH", "Youth"
    WOMEN = "WOMEN", "Women"

class AgeGroupChoices(models.TextChoices):
    NONE = "", "Senior"
    U7 = "U7", "Under 7"
    U9 = "U9", "Under 9"
    U11 = "U11", "Under 11"
    U13 = "U13", "Under 13"
    U15 = "U15", "Under 15"
    U17 = "U17", "Under 17"
    U20 = "U20", "Under 20"
    U23 = "U23", "Under 23"
    DEVELOPMENT = "DEVELOPMENT", "Development"

class CompetitionTypeChoices(models.TextChoices):
    LEAGUE = "LEAGUE", "League"
    CUP = "CUP", "Cup"
    FRIENDLY = "FRIENDLY", "Friendly"
    TOURNAMENT = "TOURNAMENT", "Tournament"

class PositionLineChoices(models.TextChoices):
    GOALKEEPER = "GOALKEEPER", "Goalkeeper"
    DEFENSE = "DEFENSE", "Defense"
    MIDFIELD = "MIDFIELD", "Midfield"
    ATTACK = "ATTACK", "Attack"

class PositionSideChoices(models.TextChoices):
    LEFT = "LEFT", "Left"
    CENTER = "CENTER", "Center"
    RIGHT = "RIGHT", "Right"

class RegistrationTypeChoices(models.TextChoices):
    PERMANENT = "PERMANENT", "Permanent"
    LOAN = "LOAN", "Loan"
    TRIAL = "TRIAL", "Trial"
    ACADEMY = "ACADEMY", "Academy"

class RegistrationStatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INJURED = "INJURED", "Injured"
    SUSPENDED = "SUSPENDED", "Suspended"
    RELEASED = "RELEASED", "Released"

class MatchStatusChoices(models.TextChoices):
    SCHEDULED = "SCHEDULED", "Scheduled"
    LIVE = "LIVE", "Live"
    FINISHED = "FINISHED", "Finished"
    POSTPONED = "POSTPONED", "Postponed"
    CANCELLED = "CANCELLED", "Cancelled"

class SquadSelectionChoices(models.TextChoices):
    STARTING = "STARTING", "Starting XI"
    SUBSTITUTE = "SUBSTITUTE", "Substitute"
    RESERVE = "RESERVE", "Reserve"

class MatchPeriodChoices(models.TextChoices):
    FIRST_HALF = "1H", "First Half"
    SECOND_HALF = "2H", "Second Half"
    EXTRA_FIRST = "ET1", "Extra Time First Half"
    EXTRA_SECOND = "ET2", "Extra Time Second Half"
    PENALTIES = "PEN", "Penalty Shootout"