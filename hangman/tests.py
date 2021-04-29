import json
import string

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
# Create your tests here.
from hangman.utils.hangman_utils import get_hangman_model


class HangmanAPITest(TestCase):

    def setUp(self):
        self.api_client = APIClient()

    def testCreate(self):
        response = self.api_client.post('/create_game/')
        result = json.loads(response.content)
        self.assertEqual(1, result['id'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        self.api_client.post('/create_game/')
        response = self.api_client.get('/get_game/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_win(self):
        self.api_client.post('/create_game/')
        hangman_model = get_hangman_model(1)
        result = None
        for c in ''.join(set(hangman_model.secret_word)):
            req = self.api_client.post('/update_game/1/', {'guess': c})

        result = json.loads(req.content)
        self.assertEqual(result['game_status'], "WIN")
        self.assertEqual(req.status_code, status.HTTP_200_OK)
        req = self.api_client.post('/update_game/1/', {'guess': c})
        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST) # test after game

    def test_loss(self):
        self.api_client.post('/create_game/')
        hangman_model = get_hangman_model(1)
        result = None
        all_chars = set(list(string.ascii_lowercase))
        unused_chars = all_chars - set(hangman_model.secret_word)

        for c in ''.join(set(unused_chars))[:8]:
            req = self.api_client.post('/update_game/1/', {'guess': c})

        result = json.loads(req.content)
        self.assertEqual(result['game_status'], "LOSS")
        self.assertEqual(req.status_code, status.HTTP_200_OK)
        req = self.api_client.post('/update_game/1/', {'guess': c})
        self.assertEqual(req.status_code, status.HTTP_400_BAD_REQUEST) # test after game