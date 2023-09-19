import constants


class WalletStore:
    def __init__(self, id, owned_by, is_enabled=False, status=constants.DISABLED, enabled_at=None, balance=0):
        self.id = id
        self.owned_by = owned_by
        self.status = status
        self.is_enabled = is_enabled
        self.enabled_at = enabled_at
        self.disabled_at = None
        self.balance = balance
        self.transactions = []
        self.token = None

    def get_wallet_data(self, disabled_flag=False):
        """
        Get wallet data in the specified format.
        """
        response = {
            constants.ID: self.id,
            constants.OWNED_BY: self.owned_by,
            constants.STATUS: self.status,
            constants.BALANCE: self.balance
        }

        if disabled_flag is False:
            response[constants.ENABLED_AT] = self.enabled_at
        else:
            response[constants.DISABLED_AT] = self.disabled_at

        return response
