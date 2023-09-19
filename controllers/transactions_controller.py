from controllers.base_controller import BaseController
from services import transaction as transaction_service


class Transactions(BaseController):
    def get(self):
        input = BaseController.get_request_input()
        return transaction_service.Transaction().fetch_transactions(input)


class Withdrawals(BaseController):
    def post(self):
        input = BaseController.get_request_input()
        return transaction_service.Transaction().withdrawal(input)


class Deposits(BaseController):
    def post(self):
        input = BaseController.get_request_input()
        return transaction_service.Transaction().deposit(input)

