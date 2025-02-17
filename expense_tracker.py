import csv
import matplotlib.pyplot as plt

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
            
def calculate_total_expense():
    total = 0.00
    with open('expense.csv', mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row['amount'])
    print(f"Total expense: ${total:.2f}")

def expense_by_category():
    categories = {"Food": 0, "Entertainment" : 0, "Transport": 0, "Bills" : 0, "Others": 0 }
    with open('expense.csv', mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories[row['category']] += float(row['amount'])
    
    for category, amount in categories.items():
        print(f"{category} : ${amount:.2f}")

def plot_expense_by_category():
    categories = {"Food": 0, "Entertainment" : 0, "Transport": 0, "Bills" : 0, "Others": 0 }
    with open('expense.csv', mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories[row['category']] += float(row['amount'])
    
    labels = list(categories.keys())
    sizes = list(categories.values())
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Expense by Category")
    plt.show()

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
        elif choice == "3":
            calculate_total_expense()
        elif choice == "4":
            expense_by_category()
        elif choice == "5":
            plot_expense_by_category()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    