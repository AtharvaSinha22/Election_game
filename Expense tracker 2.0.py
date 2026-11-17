class Expense:
    def _init_(self,date,amount,category,description):
     self.date = date
     self.amount = amount
     self.category = category
     self.description = description
    
class Tracker:
    def _init_(self):
        self.expense = []
    self.expense.append(expense)
    
while True:
    print("1.Add expense")
    print("2.Set budget")
    print("3.Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        date = input("Enter the date:")
        amonut = int("Enter the amount:")
        category = input("Enter the category:")
        description = input("Enter the discription:")
        expense = (date,amount,category,description)
        Tracker.add(expense)
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
                     
    
     

