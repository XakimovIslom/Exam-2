from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="team_logos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    age = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="player_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="home_matches"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="away_matches"
    )
    date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"


class MatchStatistic(models.Model):
    match = models.ForeignKey(
        Match, on_delete=models.CASCADE, related_name="statistics"
    )
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="match_statistics"
    )
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    # Add more statistics as needed

    class Meta:
        verbose_name = _("Match Statistic")
        verbose_name_plural = _("Match Statistics")

    def __str__(self):
        return f"{self.player} - Goals: {self.goals}, Assists: {self.assists}, Yellows: {self.yellow_cards}, Reds: {self.red_cards}"


class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, related_name="leagues")
    matches = models.ManyToManyField(Match, related_name="leagues")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
