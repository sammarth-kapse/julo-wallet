import constants
from utils import get_formatted_time
from datastore.wallet_store import WalletStore

# Following are in memory datastore.
# wallets will store dictionary/ store mapping from id to class object
# token mappings will map token to wallet id
wallets = {}  # id: Wallet()
token_mapping = {}  # token : wallet_id


def add_wallet(id, token, wallet):
    token_mapping[token] = id
    wallets[id] = wallet


def get_wallet(id):
    return wallets.get(id)


def enable_wallet(wallet):
    wallet.is_enabled = True
    wallet.status = constants.ENABLED
    wallet.enabled_at = get_formatted_time()


def disable_wallet(wallet):
    wallet.is_enabled = False
    wallet.status = constants.DISABLED
    wallet.enabled_at = None
    wallet.disabled_at = get_formatted_time()


def get_transactions(wallet):
    return wallet.transactions


def withdraw(wallet, amount, transaction):
    wallet.balance -= amount
    wallet.transactions.append(transaction)


def deposit(wallet, amount, transaction):
    wallet.balance += amount
    wallet.transactions.append(transaction)
