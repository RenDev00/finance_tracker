from controller.new_transaction_dialog_controller import NewTransactionDialogController
from model.finance_tracker import FinanceTracker
from model.transaction import Transaction
from view.finance_tracker_view import FinanceTrackerView

from PySide6.QtWidgets import QTableWidgetItem

from view.new_transaction_dialog_view import NewTransactionDialogView


class FinanceTrackerController:
    def __init__(self, view: FinanceTrackerView, model: FinanceTracker):
        self.view = view
        self.model = model
        self.populate_transaction_table()

        # Signals
        self.view.button_new.clicked.connect(self.handle_new)
        self.view.button_edit.clicked.connect(self.handle_edit)
        self.view.button_delete.clicked.connect(self.handle_delete)

    def populate_transaction_table(self, transactions: list[Transaction] = None):
        if transactions == None:
            transactions = self.model.transactions

        for _ in range(self.view.table_transactions.rowCount()):
            self.view.table_transactions.removeRow(0)

        for row, t in enumerate(transactions):
            self.view.table_transactions.insertRow(row)
            for col, data in enumerate(
                [
                    t.transaction_date,
                    t.transaction_type.name,
                    f"{round(t.amount, 2):.2f}",
                    t.transaction_category.capitalize(),
                ]
            ):
                item = QTableWidgetItem(data)
                self.view.table_transactions.setItem(row, col, item)

        self.view.table_transactions.resizeColumnToContents(0)

    def handle_new(self):
        dialog_view = NewTransactionDialogView(self.view)
        dialog_controller = NewTransactionDialogController(dialog_view, self.model)
        if dialog_controller.execute():
            self.populate_transaction_table()

    def handle_edit(self):
        pass

    def handle_delete(self):
        pass
