from django.core.validators import RegexValidator
from rest_framework import serializers

from hangman import models
from hangman.models import HangManGame


class HangManGameCreateSerializer(serializers.ModelSerializer):
    """When creating object in DB only return id"""
    class Meta:
        model = HangManGame
        fields = ['id']

class HangManGameSerializer(serializers.ModelSerializer):
    """When posting updates to object return everything except secret_word"""
    class Meta:
        model = HangManGame
        exclude = ['secret_word']

class GuessSerializer(serializers.Serializer):
    """This serializer makes sure that only guesses are processed with the requirments below"""
    char_validator = RegexValidator(r'^[a-zA-Z]*$', 'Only a-z and A-Z characters are allowed.')
    guess = serializers.CharField(max_length=1, required=True, allow_null=False, validators=[char_validator])