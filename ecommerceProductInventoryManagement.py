def read_inventory(filename):
    try:
        with open(filename, 'r') as file:
            inventory = {}
            for line in file:
                product, quantity, price = line.strip().split(',')
                inventory[product] = (int(quantity), float(price))
            return inventory
    except FileNotFoundError:
        return {}
    
def add_product(inventory):
    product = input("Enter product name: ")
    if product in inventory:
        print("Product already exists.")
    else:
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter price: "))
        inventory[product] = (quantity, price)

def update_product(inventory):
    product = input("Enter product name: ")
    if product not in inventory:
        print("Product not found.")
    else:
        quantity = int(input("Enter new quantity: ")) 
        price = float(input("Enter new price: "))
        inventory[product] = (quantity, price)


def display_inventory(inventory):
    for product, details in inventory.items():
        print(f"{product}: Quantity - {details[0]}, Price - {details[1]}")

def check_stock(inventory):
    product = input("Enter product name to check stock: ")
    if product in inventory:
        print(f"{product}: Quantity - {inventory[product][0]}, Price - {inventory[product][1]}")
    else:
        print("Product not found.")

def write_inventory(filename, inventory):
    with open(filename, 'w') as file:
        for product, details in inventory.items():
            file.write(f"{product}, {details[0]}, {details[1]}")




def main():
    inventory = read_inventory('inventory.txt')

    while True:
        print("\n1. Add a Product\n2. Update a Product\n3. Display Inventory\n4. Check Stock\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_product(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            check_stock(inventory)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
        
        write_inventory('inventory.txt', inventory)


if __name__ == "__main__":
    main()