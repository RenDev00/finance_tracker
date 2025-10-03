import uuid
from controller.edit_transaction_dialog_controller import (
    EditTransactionDialogController,
)
from controller.new_transaction_dialog_controller import NewTransactionDialogController
from model.finance_tracker import FinanceTracker
from model.transaction import Transaction
from view.edit_transaction_dialog_view import EditTransactionDialogView
from view.finance_tracker_view import FinanceTrackerView

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

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
        self.view.line_edit_search_term.textChanged.connect(self.handle_search)
        self.view.combo_box_filter.currentTextChanged.connect(self.handle_search)

    def populate_transaction_table(self, transactions: list[Transaction] = None):
        if transactions == None:
            transactions = self.model.transactions

        for _ in range(self.view.table_transactions.rowCount()):
            self.view.table_transactions.removeRow(0)

        for row, t in enumerate(transactions):
            self.view.table_transactions.insertRow(row)
            for col, data in enumerate(
                [
                    str(t.uuid),
                    t.transaction_date,
                    t.transaction_type.name,
                    f"{round(t.amount, 2):.2f}",
                    t.transaction_category.capitalize(),
                ]
            ):
                item = QTableWidgetItem(data)
                self.view.table_transactions.setItem(row, col, item)

        self.view.table_transactions.resizeColumnToContents(1)

    def handle_new(self):
        dialog_view = NewTransactionDialogView(self.view)
        dialog_controller = NewTransactionDialogController(dialog_view, self.model)
        if dialog_controller.execute():
            self.handle_search()

    def handle_edit(self):
        current_table_row_index = self.view.table_transactions.currentRow()
        uuid_item = self.view.table_transactions.item(current_table_row_index, 0)
        id = uuid.UUID(uuid_item.text())
        transaction = self.model.get_transaction_by_uuid(id)

        dialog_view = EditTransactionDialogView(self.view)
        dialog_controller = EditTransactionDialogController(
            dialog_view, self.model, transaction
        )

        if dialog_controller.execute():
            self.handle_search()

    def handle_delete(self):
        current_table_row_index = self.view.table_transactions.currentRow()
        uuid_item = self.view.table_transactions.item(current_table_row_index, 0)
        id = uuid.UUID(uuid_item.text())

        dialog = QMessageBox(self.view)
        dialog.setWindowTitle("Finance Tracker | Delete")
        dialog.setText(
            f"Delete the following transaction?\n\n{self.model.get_transaction_by_uuid(id)}"
        )
        dialog.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        dialog.setIcon(QMessageBox.Icon.Question)

        if dialog.exec() == QMessageBox.StandardButton.Yes:
            self.model.delete_transaction_by_uuid(id)
            self.handle_search()

    def handle_search(self):
        search_term = self.view.line_edit_search_term.text().lower()
        search_filter = self.view.combo_box_filter.currentText().strip().upper()

        # No searchterm and filter is all
        if search_term == "" and search_filter == "ALL":
            transactions = self.model.transactions

        # No Searchterm and filter is not all
        if search_term == "" and search_filter != "ALL":
            transactions = [
                t
                for t in self.model.transactions
                if t.transaction_type.name == search_filter
            ]

        # Searchterm entered and filter is all
        if search_term != "" and search_filter == "ALL":
            transactions = [
                t
                for t in self.model.transactions
                if search_term in t.transaction_category
            ]

        # Searchterm entered and filter not all
        if search_term != "" and search_filter != "ALL":
            transactions = [
                t
                for t in self.model.transactions
                if (search_term in t.transaction_category)
                and (t.transaction_type.name == search_filter)
            ]

        self.populate_transaction_table(transactions)
