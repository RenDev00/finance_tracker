from view.new_transaction_dialog_view import NewTransactionDialogView


class EditTransactionDialogView(NewTransactionDialogView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Finance Tracker | Edit")
