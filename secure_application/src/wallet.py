from transaction import Transaction


class Wallet:
    def __init__(self, wallet_id, owner_name, email):
        self.wallet_id = wallet_id
        self.owner_name = owner_name
        self.email = email
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount

        transaction = Transaction(
            "DEPOSIT",
            amount,
            "EXTERNAL",
            self.wallet_id
        )

        self.transactions.append(transaction)
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount

        transaction = Transaction(
            "WITHDRAW",
            amount,
            self.wallet_id,
            "EXTERNAL"
        )

        self.transactions.append(transaction)
        return True

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def display_wallet(self):
        print("\n===== WALLET DETAILS =====")
        print(f"Wallet ID : {self.wallet_id}")
        print(f"Owner     : {self.owner_name}")
        print(f"Email     : {self.email}")
        print(f"Balance   : {self.balance}")
