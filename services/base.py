from http import HTTPStatus

import constants
import datastore

class Base(object):

    @staticmethod
    def success_api_response(data=None, status_code=HTTPStatus.OK):
        data = {
            constants.STATUS: 'success',
            constants.DATA: data,
        }
        return data, status_code

    @staticmethod
    def failure_api_response(message=None, status_code=HTTPStatus.BAD_REQUEST):
        data = {
            constants.STATUS: constants.FAIL,
            constants.DATA: {
                constants.ERROR: message
            }
        }
        return data, status_code

    @staticmethod
    def validate_input(input, wallet_enabled_check=True):
        wallet_id = input.get(constants.WALLET_ID, None)
        if not wallet_id:
            return None, "Invalid Wallet ID"
        wallet = datastore.get_wallet(wallet_id)
        if not wallet:
            return None, "Wallet cannot be located"

        if wallet_enabled_check and wallet.is_enabled is False:
            return None, constants.WALLET_DISABLED

        return wallet, None
