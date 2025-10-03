import sys
from PySide6.QtWidgets import QApplication

from controller.finance_tracker_controller import FinanceTrackerController
from model.finance_tracker import FinanceTracker
from view.finance_tracker_view import FinanceTrackerView


if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = FinanceTrackerView()
    model = FinanceTracker("./data/sample_data.json")
    control = FinanceTrackerController(view, model)
    view.show()

    sys.exit(app.exec())
