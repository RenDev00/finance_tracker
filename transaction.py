from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    INCOME = 0
    EXPENSE = 1


class Transaction:
    def __init__(
        self,
        amount: float,
        transaction_type: TransactionType,
        transaction_category: str,
        transaction_date: datetime = None,
    ):
        self.amount = amount
        self.transaction_type = transaction_type
        self.transaction_category = transaction_category
        self.transaction_date = (
            transaction_date
            if transaction_date
            else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
