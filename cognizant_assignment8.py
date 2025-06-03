# Inventory Manager Program (No functions)

# Step 1: Create the inventory
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

print("Welcome to the Inventory Manager!")

# Step 2–4: Main loop for interaction
while True:
    print("\nChoose an option:")
    print("1. Display inventory")
    print("2. Add item")
    print("3. Remove item")
    print("4. Update item")
    print("5. Show total value")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\nCurrent inventory:")
        for item in inventory:
            quantity, price = inventory[item]
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    
    elif choice == "2":
        item = input("Enter the name of the item to add: ").lower()
        if item in inventory:
            print("Item already exists. Use option 4 to update it.")
        else:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory[item] = (quantity, price)
            print(f"{item} added to inventory.")

    elif choice == "3":
        item = input("Enter the name of the item to remove: ").lower()
        if item in inventory:
            del inventory[item]
            print(f"{item} removed from inventory.")
        else:
            print("Item not found.")

    elif choice == "4":
        item = input("Enter the name of the item to update: ").lower()
        if item in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f"{item} updated.")
        else:
            print("Item not found.")

    elif choice == "5":
        total = 0
        for item in inventory:
            quantity, price = inventory[item]
            total += quantity * price
        print(f"Total value of inventory: ${total:.2f}")
    
    elif choice == "6":
        print("Exiting Inventory Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
