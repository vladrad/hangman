from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """Cutsom exception handler to include default defined codes"""
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    if response is not None:
        if 'code' in exc.get_full_details():
            response.data['code'] = exc.get_full_details()['code']

    return response

class GameNotFound(APIException):
    """"When id is not found in the database"""
    status_code = 404
    default_detail = 'Game has not been found.'
    default_code = 'game_not_found'

class IncorrectField(APIException):
    """Exception for incorrect fields"""
    status_code = 400
    default_code = 'incorrect_field'

class GameStatusException(APIException):
    """Exception for incorrect fields"""
    status_code = 400
    default_code = 'game_finished'