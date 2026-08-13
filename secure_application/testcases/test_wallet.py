from wallet_service import WalletService


def main():
    service = WalletService()

    print("===== CREATE WALLET =====")

    wallet = service.create_wallet(
        "W001",
        "Abhishek",
        "abhishek@example.com"
    )

    if wallet:
        print("Wallet created successfully!")
    else:
        print("Wallet creation failed!")

    print("\n===== INITIAL BALANCE =====")

    balance = service.get_balance("W001")
    print("Balance:", balance)

    print("\n===== DEPOSIT =====")

    if service.deposit("W001", 1000):
        print("Deposit successful!")

    print("Balance:", service.get_balance("W001"))

    print("\n===== WITHDRAW =====")

    if service.withdraw("W001", 250):
        print("Withdrawal successful!")
    else:
        print("Withdrawal failed!")

    print("Balance:", service.get_balance("W001"))

    print("\n===== TRANSACTION HISTORY =====")

    history = service.get_transaction_history("W001")

    for transaction in history:
        print(transaction)


if __name__ == "__main__":
    main()
