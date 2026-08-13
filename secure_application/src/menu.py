from login import Login
from wallet_service import WalletService
from wallet_manager import WalletManager
from transaction_request import TransactionRequest


class Menu:
    def __init__(self):
        self.login = Login()
        self.wallet_service = WalletService()
        self.wallet_manager = WalletManager(self.wallet_service)
        self.transaction_request = TransactionRequest(self.wallet_service)

    def start(self):

        if not self.login.login():
            return

        while True:

            print("\n========== CRYPTOCURRENCY WALLET ==========")
            print("1. Create Wallet")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Search Wallet")
            print("7. Update Wallet")
            print("8. Delete Wallet")
            print("9. Display All Wallets")
            print("10. Transfer Money")
            print("11. Logout")
            print("12. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":

                wallet_id = input("Wallet ID: ")
                owner = input("Owner Name: ")
                email = input("Email: ")

                wallet = self.wallet_service.create_wallet(
                    wallet_id,
                    owner,
                    email
                )

                if wallet:
                    print("Wallet Created Successfully.")
                else:
                    print("Wallet ID already exists.")

            elif choice == "2":

                wallet_id = input("Wallet ID: ")
                amount = float(input("Amount: "))

                if self.wallet_service.deposit(wallet_id, amount):
                    print("Deposit Successful.")
                else:
                    print("Deposit Failed.")

            elif choice == "3":

                wallet_id = input("Wallet ID: ")
                amount = float(input("Amount: "))

                if self.wallet_service.withdraw(wallet_id, amount):
                    print("Withdrawal Successful.")
                else:
                    print("Withdrawal Failed.")

            elif choice == "4":

                wallet_id = input("Wallet ID: ")

                balance = self.wallet_service.get_balance(wallet_id)

                if balance is None:
                    print("Wallet not found.")
                else:
                    print(f"Current Balance : {balance}")

            elif choice == "5":

                wallet_id = input("Wallet ID: ")

                history = self.wallet_service.get_transaction_history(wallet_id)

                if history is None:
                    print("Wallet not found.")
                else:
                    if len(history) == 0:
                        print("No Transactions.")
                    else:
                        for transaction in history:
                            print(transaction)

            elif choice == "6":

                self.wallet_manager.search_wallet()

            elif choice == "7":

                self.wallet_manager.update_wallet()

            elif choice == "8":

                self.wallet_manager.delete_wallet()

            elif choice == "9":

                self.wallet_manager.display_all_wallets()

            elif choice == "10":

                self.transaction_request.transfer()

            elif choice == "11":

                self.login.logout()

                if self.login.login():
                    continue
                else:
                    break

            elif choice == "12":

                print("Thank you for using Cryptocurrency Wallet.")
                break

            else:

                print("Invalid Choice.")