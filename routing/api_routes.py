from controllers.transactions_controller import Transactions, Withdrawals, Deposits
from controllers.wallet_controller import InitializeWallet, Wallet

# Routes which are to be accessed with API credentials only.
api_routes = {
    '/init': InitializeWallet,
    '/wallet': Wallet,
    '/wallet/transactions': Transactions,
    '/wallet/deposits': Deposits,
    '/wallet/withdrawals': Withdrawals,
}
