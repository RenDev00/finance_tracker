from model.finance_tracker import FinanceTracker
from model.transaction import Transaction, TransactionType
from view.new_transaction_dialog_view import NewTransactionDialogView
from PySide6.QtWidgets import QDialog, QMessageBox


class NewTransactionDialogController:
    def __init__(self, view: NewTransactionDialogView, model: FinanceTracker):
        self.view = view
        self.model = model

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
        self.model.add_transaction(amount, t_type, t_category, t_date)
        return True
