from controllers.base_controller import BaseController
from services import wallet as wallet_service


class Wallet(BaseController):
    def get(self):
        input = BaseController.get_request_input()
        return wallet_service.Wallet().fetch_wallet(input)

    def post(self):
        input = BaseController.get_request_input()
        return wallet_service.Wallet().enable_wallet(input)

    def patch(self):
        input = BaseController.get_request_input()
        return wallet_service.Wallet().disable_wallet(input)


class InitializeWallet(BaseController):
    method_decorators = []

    def post(self):
        input = BaseController.get_request_input(get_wallet=False)
        return wallet_service.Wallet().initialize_wallet(input)
