from finance_tracker import FinanceTracker
from transaction import TransactionType


def add_transaction_cli(tracker: FinanceTracker):
    amount = input("Amount: ")
    transaction_type = input("Transaction type [expense / income]: ")
    transaction_category = input("Transaction category: ")

    try:
        amount = float(amount)
    except ValueError:
        print(f"Error, {amount} is not a number")
        return

    try:
        transaction_type = TransactionType[transaction_type.upper()]
    except KeyError:
        print(f"Error, invalid transaction type {transaction_type}")
        return

    try:
        tracker.add_transaction(amount, transaction_type, transaction_category)
    except ValueError as e:
        print(f"Error, {e}")


def print_transactions_by_category_cli(tracker: FinanceTracker):
    category = input("Category: ")
    transactions = tracker.get_transactions_by_category(category)
    for t in transactions:
        print(t)


def main():
    tracker = FinanceTracker("./data/sample_data.json")

    cont = True
    while cont:
        print("\nFinance Tracker")
        print("1. Add Transaction")
        print("2. Show Total Income")
        print("3. Show Total Expenses")
        print("4. Show Balance")
        print("5. Show by Category")
        print("6. Exit")

        choice = input("Choose from action 1 - 6: ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"Error, {choice} is not a number")
            continue

        if not 0 < choice < 7:
            print(f"Error, invalid action {choice}")
            continue

        match (choice):
            case 1:
                add_transaction_cli(tracker)
            case 2:
                print(f"Your total income is {tracker.get_total_income()}")
            case 3:
                print(f"Your total expenses are {tracker.get_total_expenses()}")
            case 4:
                print(f"Your balance is {tracker.get_balance()}")
            case 5:
                print_transactions_by_category_cli(tracker)
            case 6:
                cont = False

    else:
        print("Finance Tracker exited")


if __name__ == "__main__":
    main()
