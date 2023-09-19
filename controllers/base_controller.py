import http
import json
from flask import request, Response
from flask_restx import Resource

import constants
import datastore
from routing.auth import authenticate


class BaseController(Resource):
    method_decorators = [authenticate]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_headers():
        return request.headers

    @staticmethod
    def get_json_request():
        return request.json

    @staticmethod
    def set_response(response, status_code=http.HTTPStatus.OK):
        return Response(json.dumps(response), status=status_code, mimetype=u'application/json')

    @staticmethod
    def get_wallet_id(auth):
        token = str(auth).split()[1]
        return datastore.token_mapping.get(token)

    @staticmethod
    def get_request_input(get_wallet=True):
        """
        :return: Various Requests-Inputs
        """
        request_input = {}
        request_json = request.get_json(silent=True)
        if request_json:
            request_input.update(request_json)

        request_values = request.values
        if request_values:
            request_input.update(request_values)

        request_args = request.view_args
        if request_args:
            request_input.update(request_args)

        if get_wallet:
            wallet_id = BaseController.get_wallet_id(request.authorization)
            request_input[constants.WALLET_ID] = wallet_id

        return request_input
