'''Build an expense tracker application that helps users manage their finances. 
Users can add expenses, categorize them, set budgets, and generate text file
to track their spending habits'''
class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def generate_text_report(self):
        report = "Date\tAmount\tCategory\tDescription\n"
        for expense in self.expenses:
            report += f"{expense.date}\t{expense.amount}\t{expense.category}\t{expense.description}\n"
        return report

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Mennu:")
        print("1. Add Expense")
        print("2. Generate Text Report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (DD-MM-YYYY): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            expense = Expense(date, amount, category, description)
            tracker.add_expense(expense)
            print("Expense added ")

        elif choice == "2":
            if tracker.expenses:
                text_report = tracker.generate_text_report()
                with open("expense_report.txt", "w") as file:
                    file.write(text_report)
                print("Expense report generated as expense_report.txt")
            else:
                print("No expenses to generate a report.")

        elif choice == "3":
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()



