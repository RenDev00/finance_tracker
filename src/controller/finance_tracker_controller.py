from model.finance_tracker import FinanceTracker
from view.finance_tracker_view import FinanceTrackerView


class FinanceTrackerController:
    def __init__(self, view: FinanceTrackerView, model: FinanceTracker):
        self.view = view
        self.model = model

        # Signals
