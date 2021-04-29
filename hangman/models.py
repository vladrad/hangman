from django.db import models


class GameStatus(models.TextChoices):
    "Holds status for games"
    IN_PROGRESS = 'IN_PROGRESS'
    WIN = 'WIN'
    LOSS = 'LOSS'

class HangManGame(models.Model):
    """Primary Game Model that holds state, secret word"""
    id = models.AutoField(primary_key=True)
    secret_word = models.CharField(max_length=255) #according to google the longest english word in the world is 45 characters long, padding wont hurt
    correct_guesses = models.CharField(max_length=255) #holds current guess
    incorrect_guesses = models.CharField(max_length=8, default="") #total number of guesses before losing
    game_status = models.CharField(max_length=11, choices=GameStatus.choices, default=GameStatus.IN_PROGRESS)  #when a game is created it is in progress

