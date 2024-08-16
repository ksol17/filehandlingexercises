def read_finances(filename):
    try:
        with open(filename, 'r') as file:
            records = []
            for line in file:
                date, record_type, category, amount = line.strip().split(',')
                records.append({'date': date, 'type': record_type, 'category': category, 'amount': float(amount)})
            return records
    except FileNotFoundError:
        return []
    
def analyze_total_expenses(records):
    total_expenses = sum(record['amount'] for record in records if record['type'] == 'Expense')
    print(f"Total Expenses: ${total_expenses:.2f}")

def analyze_total_income(records):
    total_income = sum(record['amount'] for record in records if record['type'] == 'Income')
    print(f"Total Income: ${total_income:.2f}")

def analyze_spending_by_category(records):
    expenses_by_category = {}
    for record in records:
        if record['type'] == 'Expense':
            if record['category'] not in expenses_by_category:
                expenses_by_category[record['category']] = record['amount']
            else:
                expenses_by_category[record['category']] += record['amount']

    print("Spending by Category:")
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount:.2f}")


def main():
    finances = read_finances('finance_records.txt')

    while True:
        print("\n1. Analyze Total Expenses\n2. Analyze Total Income\n3. Spending by Category\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            analyze_total_expenses(finances)
        elif choice == '2':
            analyze_total_income(finances)
        elif choice == '3':
            analyze_spending_by_category(finances)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()