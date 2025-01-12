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
            item = input("Enter the item to add:")
            shopping_list.append(item)
            # Prompt for and add an item
            pass
        elif choice == '2':
            if choice in shopping_list:
                item = input("Enter the item to add:")
                shopping_list.remove(item)
            else:
                print("The item to be removed is not in the shopping list")

            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()