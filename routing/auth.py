from functools import wraps
from http import HTTPStatus
from flask import request, abort
import constants
import datastore

# Define valid credentials
api_credentials = {constants.USERNAME: constants.TOKEN, constants.PASSWORD: 'password'}


def is_user_authorized(auth):
    """
    Validates user credentials for a given route.
    """
    auth_list = str(auth).split()
    if len(auth_list) != 2:
        abort(HTTPStatus.UNAUTHORIZED)

    token = auth_list[1]
    return token in datastore.token_mapping


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization

        if not auth or not is_user_authorized(auth):
            abort(HTTPStatus.UNAUTHORIZED)
        return func(*args, **kwargs)

    return wrapper
