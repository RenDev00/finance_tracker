# Finance Tracker
A simple CLI tool to keep track of finances. Users can add, categorize and view information about transactions.

# Features
- Add expese or income transactions with categories (e.g. Utility, Rent, Groceries, etc...).
- Show the sum of expense or income transactions.
- Show the current balance.
- Show transactions filtered by category.
- Persistant storage using a JSON file for reuse across sessions.
- Exception handling for invalid inputs.

# Technologies
- Python 3.8+
- JSON for data storage
- Built-in libraries: datetime, enum, json, os

# Setup
1. Clone the repository:
```
git clone https://github.com/RenDev00/finance_tracker.git
```

2. Navigate to the cloned repository:
```
cd finance_tracker
```

3. Run the application:
```
python ./src/main.py
```

# Usage
Run the program and follow the menu prompts.

Example commands:

- Add a transaction: Choose option 1, enter amount, type [expense / income], and category.
- Filter by category: Choose option 5, enter category.

# License
MIT License
