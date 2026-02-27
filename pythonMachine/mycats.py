cats = ['Cleo', 'Mia', 'Santa', 'Fatboi', 'Jero']

def add_cat():
    number = 1
    while True:
        try:
            question = int(input("Do you want to add a cat? 1 for yes, 2 for no.\n")).strip()
            if question == 1 or question == 2:
                break
            else:
                print("Select 1 or 2.")
        except ValueError:
            print("You did not enter a number. Please enter a number:")
            
    if question == 1:
        while True:
            try:
                ammount = int(input("How many cats do you want to add?\n")).strip()
                if ammount > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
            except ValueError:
                print("You did not enter a number. Please enter a number:")
        
        while ammount > 0:
            
            cat_name = input(f"Write the name of the cat number {number} and press enter:" ).strip().capitalize()

            if cat_name:
                cats.append(cat_name)
                ammount -= 1
                number += 1
            else:
                print("Error: The name cannot be empty or just spaces.")
        show_cat()

    elif question == 2:
        show_cat()

def remove_cat():
    target_index = crazy_search()

    if target_index is None:
        return

    while True:
        
        try:
            confirm = int(input(f"Are you sure you want to remove {cats[target_index]}? 1. for yes, 2. for no.")).strip()
            if confirm == 1:
                removed = cats.pop(target_index)
                print(f"{removed} was removed")
                break
            else:
                print("Action canceled.")
                break
        except ValueError:
            print("Error: select 1. or 2.")
            continue

def show_cat():
    print("The cat names are:")
    for i in range(len(cats)):
        print(f" {i}. {cats[i]}")
    
def search_cat_names():
    index = None

    while True:
        selector = input("Select the way you want to search a cat from list cats. By index press 1. By name press 2. To cancel the search press 3.").strip()
    
        if selector == "1":
                try:
                    user_input_index = input("Enter an index number: ").strip()
                    index = int(user_input_index)

                    name = cats[index]
                    print(f"{index} is registered! Name is: {name}")
                    return index
                except IndexError:
                    print(f"{user_input_index} is not in cats list! Sorry!")
                except ValueError:
                    print(f"{user_input_index} is not valid! Try again: ")
                    continue

        elif selector == "2":
            name = input("Enter a pet name:").capitalize().strip()
            if name not in cats:
                print(f"{name} is not in cats list! Sorry!")
            else:
                index = cats.index(name)
                print(f"{name} is registered! Index is: {index}")
                return index
        elif selector == "3":
            print("Search canceled.")
            return None
        else:
            print("Error: select 1. or 2. or 3 to exit.")
            continue
        
def crazy_search():
    index = None
    if not cats: # Si la lista está vacía []
        print("The list is empty! No cats to search.")
        return None
    while True:
        selector = input("Select the way you want to search a cat from list cats. By index press 1. By name press 2. To cancel the search press 3.").strip()

        if selector == "1":
            try:
                user_input_index = input("Enter an index number: ").strip()
                index = int(user_input_index)
                name = cats[index]
                print(f"{index} is registered! Name is: {name}")
                return index

            except IndexError:
                print(f"{user_input_index} is not in cats list! Sorry!")
            except ValueError:
                print(f"{user_input_index} is not valid! Try again: ")
                continue

        elif selector == "2":
            name = input("Enter a pet name:").capitalize().strip()
            try:
                index = cats.index(name)
                print(f"{name} is registered! Index is: {index}")
                return index
            except ValueError:
                print(f"{name} is not in cats list! Sorry!")

        elif selector == "3":
            print("Search canceled.")
            return None

        else:
            print("Error: select 1. or 2. or 3 to exit.")
            continue
        
def menu():
    print("\n" + "="*20)
    print("CAT MANAGER")
    print("="*20)
    print("1. Add Cats")
    print("2. Show Cats")
    print("3. Search Cats Names")
    print("4. Crazy Search")
    print("5. Remove Cat")
    print("0. Exit")
    print("="*20)

    selector = input("Select a tool: \n").strip()

    if selector == "1":
        add_cat()
        return True
    elif selector == "2":
        show_cat()
        return True
    elif selector == "3":
        search_cat_names()
        return True
    elif selector == "4":
        crazy_search()
        return True
    elif selector == "5":
        remove_cat()
        return True
    elif selector == "0":
        print("Goodbye!")
        return False
    else:
        print("Invalid option, try again.")
        return True

while True:
    if not menu():
        break
