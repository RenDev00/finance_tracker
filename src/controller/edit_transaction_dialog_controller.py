from model.finance_tracker import FinanceTracker
from model.transaction import Transaction, TransactionType
from view.edit_transaction_dialog_view import EditTransactionDialogView

from PySide6.QtWidgets import QMessageBox, QDialog
from PySide6.QtCore import QDateTime


class EditTransactionDialogController:
    def __init__(
        self,
        view: EditTransactionDialogView,
        model: FinanceTracker,
        transaction: Transaction,
    ):
        self.view = view
        self.model = model
        self.transaction = transaction

        # Setup
        self.view.spin_box_amount.setValue(self.transaction.amount)
        self.view.date_time_edit.setDateTime(
            QDateTime.fromString(
                self.transaction.transaction_date, "yyyy-MM-dd HH:mm:ss"
            )
        )
        self.view.combo_box_type.setCurrentText(
            self.transaction.transaction_type.name.capitalize()
        )
        self.view.line_edit_category.setText(
            self.transaction.transaction_category.capitalize()
        )

        # Signals
        self.view.button_ok.clicked.connect(self.validate_input)
        self.view.button_cancel.clicked.connect(self.view.reject)

    def validate_input(self):
        if self.view.line_edit_category.text().strip().lower() == "":
            dialog = QMessageBox(self.view)
            dialog.setWindowTitle("Finance Tracker | Error")
            dialog.setText("Please provide a category")
            dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
            dialog.setIcon(QMessageBox.Icon.Warning)
            dialog.exec()
            return

        self.view.accept()

    def execute(self) -> bool:
        if self.view.exec_() == QDialog.Rejected:
            return False

        amount = self.view.spin_box_amount.value()
        t_type = TransactionType[self.view.combo_box_type.currentText().upper()]
        t_category = self.view.line_edit_category.text().strip().lower()
        t_date = self.view.date_time_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.model.edit_transaction_by_uuid(
            self.transaction.uuid, amount, t_type, t_category, t_date
        )
        return True
