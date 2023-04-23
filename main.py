from ingredient import Ingredient

def display_menu(self):
    print("===================================")
    print("          INGREDIENT MENU          ")
    print("===================================")
    print("1. Restock")
    print("2. Check Stock")
    print("3. Use Ingredient")
    print("4. Delete Ingredient")
    print("5. Exit")
    print("===================================")

    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            amount = int(input("Enter amount to restock: "))
            self.restock(amount)

        elif choice == "2":
            self.check()

        elif choice == "3":
            amount = int(input("Enter amount to use: "))
            self.use(amount)

        elif choice == "4":
            print(f"You are deleting {self.name}. Are you sure? ")
            print("Select 1 to Delete")
            delete_confirm = input("> ")
            if delete_confirm == "1":
                self.delete_ingredient(self.name)
                viewall()
                break
            else:
                print("Operation Cancelled")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    while True: 
        print("===================================")
        print("          RESTAURANT MENU          ")
        print("===================================")
        print("1. Add new ingredient to Inventory")
        print("2. Edit an existing Ingredient")
        print("3. View Inventory")
        print("4. Exit")
        print("===================================")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            try:
                name = input("Enter ingredient name: ")
                stock_quantity = int(input("Enter stock quantity: "))
                threshold = int(input("Enter threshold: "))
                ingredient = Ingredient(name, stock_quantity, threshold)
                ingredient.add(name, stock_quantity, threshold)
                viewall()
            except ValueError as e:
                print(f"Error! Invalid entry. Enter a number.")

        elif choice == "2":
            viewall()
            print("Please input the name of the ingredient you wish to modify: ")
            enter = input("> ")
            try:
                with open('ingredients.txt', 'r') as f:
                    lines = f.readlines()
                    ingredient_found = False
                    for line in lines:
                        name, stock_quantity, threshold = line.strip().split(',')
                        if enter == name:
                            ingredient = Ingredient(name, stock_quantity, threshold)
                            display_menu(ingredient)
                            ingredient_found = True
                            break
                    if not ingredient_found:
                        print(f"Alert: {enter} does not exist in the Inventory!")
            except FileNotFoundError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            viewall()

        elif choice == "4":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


def viewall():
    print("===================================")
    print("            INVENTORY              ")
    print("===================================")
    print("NAME       QUANTITY       THRESHOLD")
    print(" \n ")

    try:
        with open('ingredients.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(',')
                print(f"{line[0]}\t\t{line[1]}\t\t{line[2]}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

main()
            