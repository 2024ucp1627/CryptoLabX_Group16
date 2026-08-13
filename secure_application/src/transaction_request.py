from wallet_service import WalletService


class TransactionRequest:
    def __init__(self, wallet_service: WalletService):
        self.wallet_service = wallet_service

    def transfer(self):
        print("\n===== MONEY TRANSFER =====")

        from_wallet = input("Sender Wallet ID: ")
        to_wallet = input("Receiver Wallet ID: ")

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        sender = self.wallet_service.get_wallet(from_wallet)
        receiver = self.wallet_service.get_wallet(to_wallet)

        if sender is None:
            print("Sender wallet not found.")
            return

        if receiver is None:
            print("Receiver wallet not found.")
            return

        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("\nTransfer Successful!")
        else:
            print("\nTransfer Failed!")