import random
from hangman.api.exceptions.api_errors import GameNotFound, GameStatusException
from hangman.models import HangManGame, GameStatus
from django.conf import settings

def find_characters_in_string(secret_word, guess):
    return [i for i, ltr in enumerate(secret_word) if ltr == guess]

def load_words():
    with open(settings.WORD_FILE) as f:
        lines = [line.rstrip() for line in f]
        return lines

def get_hangman_model(id):
    try:
        return HangManGame.objects.get(id=id)
    except HangManGame.DoesNotExist:
        raise GameNotFound()

def create_hangman_model():
    random_words = load_words()  # load random words
    secret_word = random.choice(random_words)  # get random word
    hangman = HangManGame()
    hangman.secret_word = secret_word  # set secret word
    hangman.correct_guesses = "".join(list('_' * len(secret_word)))  # on default set all chars to _
    hangman.save()
    return hangman