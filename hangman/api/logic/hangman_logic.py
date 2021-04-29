from hangman.api.exceptions.api_errors import GameStatusException
from hangman.models import GameStatus
from hangman.utils.hangman_utils import find_characters_in_string

def check_game_status(hangman_model):
    if not hangman_model.game_status == GameStatus.IN_PROGRESS:
        raise GameStatusException(f"Game cannot be updated due to status: {hangman_model.game_status}")

def process_correct_guess(hangman, guess, secret):
    """Find the locations of all guesses (multiple), loop through the """
    location = find_characters_in_string(secret, guess) # returns locations of guesses
    correct_guess = hangman.correct_guesses #grab current state of guesses ex: _ur_le
    guess_chars = list(correct_guess)

    for c in location:
        guess_chars[c] = guess # fill in the locations of missing correct guesses
    hangman.correct_guesses = "".join(guess_chars) #join to create for example from: _ur_le to turtle

    if not '_' in hangman.correct_guesses:# if no _ are found game is over
        hangman.game_status = GameStatus.WIN

    hangman.save()

def process_incorrect_guess(hangman, guess):
    """Process incorrect guesses"""
    incorrect_guess = hangman.incorrect_guesses
    if not guess in incorrect_guess: # check if already guessed, otherwise continue
        hangman.incorrect_guesses += guess #add new guess ex: ab => abf
        if len(hangman.incorrect_guesses) == 8: #if its 8 guesses game is over
            hangman.game_status = GameStatus.LOSS
        hangman.save()

def process_hangman_logic(hangman, validator):
    """Main body for processing game logic, check if correct/incorrect process function"""
    secret = hangman.secret_word
    guess = validator.data['guess'].lower()

    if guess in secret: #check if inside of guess
        process_correct_guess(hangman, guess, secret)
    else:
        process_incorrect_guess(hangman, guess)