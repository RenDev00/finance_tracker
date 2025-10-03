from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QTableWidget,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QComboBox,
)


class FinanceTrackerView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance Tracker")
        self.setMinimumSize(560, 440)
        self.init_ui()

    def init_ui(self):
        # Widgets
        central_widget = QWidget()

        group_box_filter = QGroupBox("Filter")
        self.combo_box_filter = QComboBox()
        self.button_apply_filter = QPushButton("Apply")

        group_box_search = QGroupBox("Search")
        self.line_edit_search_term = QLineEdit(placeholderText="Enter a search term")
        self.button_search = QPushButton("Search")

        group_box_transactions = QGroupBox("Transactions")
        self.table_transactions = QTableWidget(0, 4)
        self.table_transactions.setHorizontalHeaderLabels(
            ["Date", "Type", "Amount", "Category"]
        )
        self.table_transactions.horizontalHeader().setStretchLastSection(True)
        self.table_transactions.verticalHeader().setVisible(False)

        # Layout
        h_layout_filter = QHBoxLayout()
        h_layout_filter.addWidget(self.combo_box_filter)
        h_layout_filter.addWidget(self.button_apply_filter)
        group_box_filter.setLayout(h_layout_filter)

        h_layout_search = QHBoxLayout()
        h_layout_search.addWidget(self.line_edit_search_term)
        h_layout_search.addWidget(self.button_search)
        group_box_search.setLayout(h_layout_search)

        h_layout_filter_search = QHBoxLayout()
        h_layout_filter_search.addWidget(group_box_filter)
        h_layout_filter_search.addWidget(group_box_search)

        v_layout_transactions = QVBoxLayout()
        v_layout_transactions.addWidget(self.table_transactions)
        group_box_transactions.setLayout(v_layout_transactions)

        v_layout_main = QVBoxLayout()
        v_layout_main.addLayout(h_layout_filter_search)
        v_layout_main.addWidget(group_box_transactions)

        central_widget.setLayout(v_layout_main)
        self.setCentralWidget(central_widget)
