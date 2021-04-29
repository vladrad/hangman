from django.http import JsonResponse
from rest_framework.decorators import api_view

from hangman.api.logic.hangman_logic import process_hangman_logic, check_game_status
from hangman.serializers import HangManGameSerializer, HangManGameCreateSerializer, GuessSerializer
from hangman.api.exceptions.api_errors import IncorrectField
from hangman.utils.hangman_utils import get_hangman_model, create_hangman_model


@api_view(["POST"])
def create_game(request):
    """Creates game model with a random word"""
    hangman = create_hangman_model()
    hs = HangManGameCreateSerializer(hangman)
    return JsonResponse(hs.data, status=201)

@api_view(["GET"])
def get_game(request, id):
    """Grab status of on going game, used for freshing"""
    hangman = get_hangman_model(id) #grab model from db
    hs = HangManGameSerializer(hangman)
    return JsonResponse(hs.data, status=200)

@api_view(["POST"])
def update_game(request,id):
    """Updates game with guesses, process validation, guesses"""
    validator = GuessSerializer(data=request.data)
    if not validator.is_valid(): #check validity
        raise IncorrectField(detail=validator.errors)

    hangman = get_hangman_model(id) #grab model from db
    check_game_status(hangman) #check the status of the game
    process_hangman_logic(hangman, validator) #process the guess logic

    hs = HangManGameSerializer(hangman) #serialize and return
    return JsonResponse(hs.data, status=200)
