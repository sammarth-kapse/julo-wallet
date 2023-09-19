import constants
import datastore
from services.base import Base
from utils import generate_token, generate_unique_id
from datastore import WalletStore


class Wallet(Base):

    def initialize_wallet(self, input):
        customer_id = input.get(constants.CUSTOMER_ID, None)
        if not customer_id:
            return self.failure_api_response("Customer ID missing in input")

        id = generate_unique_id()
        token = generate_token()

        wallet = WalletStore(id=id, owned_by=customer_id)
        wallet.token = token
        datastore.add_wallet(id, token, wallet)

        return self.success_api_response(data={constants.TOKEN: token})

    def fetch_wallet(self, input):
        wallet, error = self.validate_input(input)

        if error:
            return self.failure_api_response(message=error)

        return self.success_api_response(wallet.get_wallet_data())

    def enable_wallet(self, input):
        wallet, error = self.validate_input(input, wallet_enabled_check=False)

        if error:
            return self.failure_api_response(message=error)

        if wallet.is_enabled:
            return self.failure_api_response(message="Wallet Already Enabled")

        datastore.enable_wallet(wallet)

        return self.success_api_response(wallet.get_wallet_data())

    def disable_wallet(self, input):
        wallet, error = self.validate_input(input, wallet_enabled_check=False)

        if error:
            return self.failure_api_response(message=error)

        if wallet.is_enabled is False:
            return self.failure_api_response(message="Wallet Already Disabled")

        if input.get(constants.IS_DISABLED, None) not in (True, "True", "true"):
            return self.failure_api_response(message="is_disabled Flag not passed correctly")

        datastore.disable_wallet(wallet)
        return self.success_api_response(wallet.get_wallet_data(disabled_flag=True))
