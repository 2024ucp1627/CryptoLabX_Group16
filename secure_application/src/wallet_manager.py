from wallet_service import WalletService


class WalletManager:
    def __init__(self, wallet_service: WalletService):
        self.wallet_service = wallet_service

    def search_wallet(self):
        wallet_id = input("Enter Wallet ID: ")

        wallet = self.wallet_service.get_wallet(wallet_id)

        if wallet:
            wallet.display_wallet()
        else:
            print("Wallet not found.")

    def update_wallet(self):
        wallet_id = input("Enter Wallet ID: ")

        wallet = self.wallet_service.get_wallet(wallet_id)

        if wallet is None:
            print("Wallet not found.")
            return

        print("\nLeave blank to keep existing value.")

        owner = input(f"Owner Name ({wallet.owner_name}): ")
        email = input(f"Email ({wallet.email}): ")

        if owner != "":
            wallet.owner_name = owner

        if email != "":
            wallet.email = email

        print("\nWallet updated successfully.")

    def delete_wallet(self):
        wallet_id = input("Enter Wallet ID to delete: ")

        if wallet_id in self.wallet_service.wallets:
            del self.wallet_service.wallets[wallet_id]
            print("Wallet deleted successfully.")
        else:
            print("Wallet not found.")

    def display_all_wallets(self):
        if len(self.wallet_service.wallets) == 0:
            print("No wallets available.")
            return

        print("\n===== ALL WALLETS =====")

        for wallet in self.wallet_service.wallets.values():
            wallet.display_wallet()