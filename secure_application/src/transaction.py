from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount, from_wallet=None, to_wallet=None):
        self.transaction_type = transaction_type
        self.amount = amount
        self.from_wallet = from_wallet
        self.to_wallet = to_wallet
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"{self.timestamp} | "
            f"{self.transaction_type} | "
            f"Amount: {self.amount} | "
            f"From: {self.from_wallet} | "
            f"To: {self.to_wallet}"
        )
