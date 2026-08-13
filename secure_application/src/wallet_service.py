from wallet import Wallet


class WalletService:
    def __init__(self):
        self.wallets = {}

    def create_wallet(self, wallet_id, owner_name, email):
        if wallet_id in self.wallets:
            return None

        wallet = Wallet(
            wallet_id,
            owner_name,
            email
        )

        self.wallets[wallet_id] = wallet

        return wallet

    def get_wallet(self, wallet_id):
        return self.wallets.get(wallet_id)

    def deposit(self, wallet_id, amount):
        wallet = self.get_wallet(wallet_id)

        if wallet is None:
            return False

        return wallet.deposit(amount)

    def withdraw(self, wallet_id, amount):
        wallet = self.get_wallet(wallet_id)

        if wallet is None:
            return False

        return wallet.withdraw(amount)

    def get_balance(self, wallet_id):
        wallet = self.get_wallet(wallet_id)

        if wallet is None:
            return None

        return wallet.get_balance()

    def get_transaction_history(self, wallet_id):
        wallet = self.get_wallet(wallet_id)

        if wallet is None:
            return None

        return wallet.get_transaction_history()

    def display_wallet(self, wallet_id):
        wallet = self.get_wallet(wallet_id)

        if wallet is None:
            print("Wallet not found.")
            return

        wallet.display_wallet()
