def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item_name = input("Enter the item to add: ")
            shopping_list.append(item_name)
        elif choice == '2':
            # Prompt for and remove an item
            item_name = input("Enter the name of item to remove: ")
            if item_name == shopping_list:
                shopping_list.remove(item_name)
            else:
                print("please enter the write item from the list to remove.")
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()