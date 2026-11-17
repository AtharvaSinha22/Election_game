class Expense:
    def _init_(self,date,amount,category,description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
    
class ExpenseTracker:
    def _init_(self):
        self.expense = []
    def add_expense(self,expense,amount, category):
        self.expense.append(expense)

def main():
    tracker = ExpenseTracker()
    while True:
        print("1.Add expense")
        print("2.Set budget")
        print("3.Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            date = eval(input("Enter the date: "))
            amount = float(input("Enter the amount:"))  
            category = eval(input("Enter the category:"))
            description = eval(input("Enter the discription:"))
            tracker.expense.append(date,amount,category,description)
            tracker.add_expense(expense)
            print("Expense added")
        elif choice == "2":
            budget = int(input("Enter the budget:"))
            print("budget set")
            if expense > budget:
               print("expense is going out of budget:")
        elif choice == "3":
            print("Exiting tracker goodbye")
            break
        else:
            print("Invalid choice. Please choose a valid option.")




     

