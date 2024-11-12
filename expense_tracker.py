import csv

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Entertainment, Transport, Bills, Others): ")
    amount = float(input("Enter amount: "))
    description = input("Description: ")
    
    expense = {"date" : date, "category" : category, "amount" : amount, "description" : description}
    
    with open("expense.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=expense.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expense)
    
    print("Expense added successfully")

def view_expense():
    with open('expense.csv', mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def main():
    while True:
        print("\n--- Personal Expense Tracker Visualization ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. View Expenses by Category")
        print("5. Plot Expenses by Category")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    