import random
cats = ['Cleo', 'Mia', 'Santa', 'Fatboi', 'Jero']

dogs = ['Rex', 'Whiskers', 'Buddy', 'Max', 'Charlie', 'Puffy', 'Fluffy', 'Milo', 'Daisy', 'Luna']

def add_cat(lista):
    number = 1
    while True:
        try:
            question = int(input("Do you want to add a cat? 1 for yes, 2 for no.\n"))
            if question == 1 or question == 2:
                break
            else:
                print("Select 1 or 2.")
        except ValueError:
            print("You did not enter a number. Please enter a number:")
            
    if question == 1:
        while True:
            try:
                ammount = int(input("How many cats do you want to add?\n"))
                if ammount > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
            except ValueError:
                print("You did not enter a number. Please enter a number:")
        
        while ammount > 0:
            
            name = input(f"Write the name of the cat number {number} and press enter:" ).strip().capitalize()

            if name:
                lista.append(name)
                ammount -= 1
                number += 1
            else:
                print("Error: The name cannot be empty or just spaces.")
        show_cat(lista)

    elif question == 2:
        show_cat(lista)

def remove_cat(lista):
    target_index = search_cat_names(lista)

    if target_index is None:
        return

    while True:
        
        try:
            confirm = int(input(f"Are you sure you want to remove {lista[target_index]}? 1. for yes, 2. for no."))
            if confirm == 1:
                removed = lista.pop(target_index)
                print(f"{removed} was removed")
                break
            else:
                print("Action canceled.")
                break
        except ValueError:
            print("Error: select 1. or 2.")
            continue

def show_cat(lista):
    print("The cat names are:")
    for i in range(len(lista)):
        print(f" {i}. {lista[i]}")
           
def search_cat_names(lista):
    index = None
    if not lista: # Si la lista está vacía []
        print("The list is empty! No cats to search.")
        return None
    while True:
        selector = input("Select the way you want to search a cat from list cats. By index press 1. By name press 2. To cancel the search press 3.").strip()

        if selector == "1":
            try:
                user_input_index = input("Enter an index number: ").strip()
                index = int(user_input_index)
                name = lista[index]
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
                index = lista.index(name)
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

def sorting_cats_names(lista):
    lista.sort()
    show_cat(lista)    

def random_cat_message():
    messages = [
        "Meow! 🐱",
        "Purr purr...",
        "The cat is adorable!",
        "Cats rule the world",
        "Paws are precious",
        "Whiskers and cuddles",
        "Cat lovers unite!",
        "Meow means hello",
        "Cats are the best",
        "Purrfectly amazing"
        ]
    print(random.choice(messages))
    #print(messages[random.randint(0, len(messages) - 1)])

def pretty_cat_name(lista):
    target_index = search_cat_names(lista)

    if target_index is None:
        return
    for i in lista[target_index]:
        print("* * *", i , "* * *")

def menu_selector():
    while True:
        tipo = input("Para gestionar Gatos presione 1. \n Para gestionar Perros presione 2. \n Para salir presione 3.")

        if tipo == "1":
            return cats, "CAT"
        elif tipo == "2":
            return dogs, "DOG"
        elif tipo == "3":
            print("Goodbye!")
            return None, None
        else:
            print("Invalid option, try again.")
            return True

def menu():
    lista_activa, nombre_animal = menu_selector()

    if lista_activa is None:
        return False

    while True:
        print("\n" + "="*20)
        print(f"{nombre_animal} MANAGER")
        print("="*20)
        print(f"1. Add {nombre_animal}")
        print(f"2. Show {nombre_animal}")
        print(f"3. Search {nombre_animal} Names")
        print(f"4. Remove {nombre_animal}")
        print(f"5. Sorting {nombre_animal} Names")
        print(f"6. Random {nombre_animal} Message")
        print(f"7. Show Pretty {nombre_animal}")
        print("0. Exit")
        print("="*20)

        selector = input("Select a tool: \n").strip()

        if selector == "1":
            add_cat(lista_activa)
            return True
        elif selector == "2":
            show_cat(lista_activa)
            return True
        elif selector == "3":
            search_cat_names(lista_activa)
            return True
        elif selector == "4":
            remove_cat(lista_activa)
            return True
        elif selector == "5":
            sorting_cats_names(lista_activa)
            return True
        elif selector == "6":
            random_cat_message()
            return True
        elif selector == "7":
            pretty_cat_name(lista_activa)
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
