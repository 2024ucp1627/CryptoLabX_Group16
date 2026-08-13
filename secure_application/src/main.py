from menu import Menu
  from wallet_service import WalletService
if __name__ == "__main__":
    menu = Menu()
    menu.start()
    
  


def display_menu():
    print("\n" + "=" * 45)
    print("        CRYPTOCURRENCY WALLET")
    print("=" * 45)
    print("1. Create Wallet")
    print("2. View Wallet")
    print("3. Balance Inquiry")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transaction History")
    print("0. Exit")
    print("=" * 45)


def create_wallet(service):
    print("\n===== CREATE WALLET =====")

    wallet_id = input("Enter Wallet ID: ").strip()
    owner_name = input("Enter Owner Name: ").strip()
    email = input("Enter Email: ").strip()

    if not wallet_id or not owner_name or not email:
        print("All fields are required.")
        return

    wallet = service.create_wallet(
        wallet_id,
        owner_name,
        email
    )

    if wallet is None:
        print("Wallet ID already exists.")
    else:
        print("Wallet created successfully!")


def view_wallet(service):
    print("\n===== VIEW WALLET =====")

    wallet_id = input("Enter Wallet ID: ").strip()

    service.display_wallet(wallet_id)


def show_balance(service):
    print("\n===== BALANCE INQUIRY =====")

    wallet_id = input("Enter Wallet ID: ").strip()

    balance = service.get_balance(wallet_id)

    if balance is None:
        print("Wallet not found.")
    else:
        print(f"Current Balance: {balance}")


def deposit(service):
    print("\n===== DEPOSIT =====")

    wallet_id = input("Enter Wallet ID: ").strip()

    try:
        amount = float(input("Enter deposit amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if service.deposit(wallet_id, amount):
        print("Deposit successful!")
        print(f"Current Balance: {service.get_balance(wallet_id)}")
    else:
        print("Deposit failed.")


def withdraw(service):
    print("\n===== WITHDRAW =====")

    wallet_id = input("Enter Wallet ID: ").strip()

    try:
        amount = float(input("Enter withdrawal amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if service.withdraw(wallet_id, amount):
        print("Withdrawal successful!")
        print(f"Current Balance: {service.get_balance(wallet_id)}")
    else:
        print("Withdrawal failed. Check wallet or balance.")


def transaction_history(service):
    print("\n===== TRANSACTION HISTORY =====")

    wallet_id = input("Enter Wallet ID: ").strip()

    history = service.get_transaction_history(wallet_id)

    if history is None:
        print("Wallet not found.")
        return

    if not history:
        print("No transactions found.")
        return

    for transaction in history:
        print(transaction)


def main():
    service = WalletService()

    print("\nWelcome to the Cryptocurrency Wallet!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_wallet(service)

        elif choice == "2":
            view_wallet(service)

        elif choice == "3":
            show_balance(service)

        elif choice == "4":
            deposit(service)

        elif choice == "5":
            withdraw(service)

        elif choice == "6":
            transaction_history(service)

        elif choice == "0":
            print("\nThank you for using Cryptocurrency Wallet.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
