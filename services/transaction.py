import constants
import datastore
from utils import get_formatted_time, generate_unique_id
from services.base import Base


class Transaction(Base):
    def fetch_transactions(self, input):
        wallet, error = self.validate_input(input)
        if error:
            return self.failure_api_response(message=error)

        transactions = datastore.get_transactions(wallet)

        return self.success_api_response(transactions)

    def deposit(self, input):
        wallet, error = self.validate_input(input)
        if error:
            return self.failure_api_response(message=error)

        amount = input.get(constants.AMOUNT)
        reference_id = input.get(constants.REFERENCE_ID)
        deposited_by = input.get(constants.DEPOSITED_BY, wallet.owned_by)
        if not amount or not reference_id:
            return self.failure_api_response(message="Invalid Input")

        id = generate_unique_id()
        time = get_formatted_time()
        amount = int(amount)

        transaction = {
            constants.DEPOSIT: {
                constants.ID: id,
                constants.DEPOSITED_BY: deposited_by,
                constants.STATUS: constants.SUCCESS,
                constants.DEPOSITED_AT: time,
                constants.AMOUNT: amount,
                constants.REFERENCE_ID: reference_id
            }
        }

        datastore.deposit(wallet, amount, transaction)
        return self.success_api_response(transaction)

    def withdrawal(self, input):
        wallet, error = self.validate_input(input)
        if error:
            return self.failure_api_response(message=error)

        amount = input.get(constants.AMOUNT)
        reference_id = input.get(constants.REFERENCE_ID)
        if not amount or not reference_id:
            return self.failure_api_response(message="Invalid Input")

        amount = int(amount)
        if amount > wallet.balance:
            return self.failure_api_response(message="Balance less than amount to be withdrawn.")

        withdrawn_by = input.get(constants.WITHDRAWN_BY, wallet.owned_by)
        id = generate_unique_id()
        time = get_formatted_time()

        transaction = {
            constants.WITHDRAWAL: {
                constants.ID: id,
                constants.WITHDRAWN_BY: withdrawn_by,
                constants.STATUS: constants.SUCCESS,
                constants.WITHDRAWN_AT: time,
                constants.AMOUNT: amount,
                constants.REFERENCE_ID: reference_id
            }
        }

        datastore.withdraw(wallet, amount, transaction)
        return self.success_api_response(transaction)

