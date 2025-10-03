from model.finance_tracker import FinanceTracker
from model.transaction import Transaction
from view.finance_tracker_view import FinanceTrackerView

from PySide6.QtWidgets import QTableWidgetItem


class FinanceTrackerController:
    def __init__(self, view: FinanceTrackerView, model: FinanceTracker):
        self.view = view
        self.model = model
        self.populate_transaction_table(self.model.transactions)

        # Signals

    def populate_transaction_table(self, transactions: list[Transaction]):
        self.view.table_transactions.clearContents()
        for row, t in enumerate(transactions):
            self.view.table_transactions.insertRow(row)
            for col, data in enumerate(
                [
                    t.transaction_date,
                    t.transaction_type.name,
                    round(t.amount, 2),
                    t.transaction_category.capitalize(),
                ]
            ):
                item = QTableWidgetItem(str(data))
                self.view.table_transactions.setItem(row, col, item)

        self.view.table_transactions.resizeColumnToContents(0)
