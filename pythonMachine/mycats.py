import random
cats = ['Cleo', 'Mia', 'Santa', 'Fatboi', 'Jero']

dogs = ['Rex', 'Whiskers', 'Buddy', 'Max', 'Charlie', 'Puffy', 'Fluffy', 'Milo', 'Daisy', 'Luna']

def add_item(lista, tipo):
    number = 1
    while True:
        try:
            question = int(input(f"Do you want to add a {tipo.lower()}? 1 for yes, 2 for no.\n"))
            if question == 1 or question == 2:
                break
            else:
                print("Select 1 or 2.")
        except ValueError:
            print("You did not enter a number. Please enter a number:")
            
    if question == 1:
        while True:
            try:
                ammount = int(input(f"How many {tipo.lower()}s do you want to add?\n"))
                if ammount > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
            except ValueError:
                print("You did not enter a number. Please enter a number:")
        
        while ammount > 0:
            
            name = input(f"Write the name of the {tipo.lower()} number {number} and press enter:" ).strip().capitalize()

            if name:
                lista.append(name)
                ammount -= 1
                number += 1
            else:
                print("Error: The name cannot be empty or just spaces.")
        show_item(lista, tipo)

    elif question == 2:
        show_item(lista, tipo)

def remove_item(lista):
    target_index = search_item_names(lista)

    if target_index is None:
        return

    while True:
        
        try:
            confirm = int(input(f"Are you sure you want to remove {lista[target_index]}? 1. for yes, 2. for no."))
            if confirm == 1:
                removed = lista.pop(target_index)
                print(f"{removed} was removed")
                break
            elif confirm == 2:
                print("Action canceled.")
                break
        except ValueError:
            print("Error: select 1. or 2.")
            continue

def show_item(lista, tipo):
    print(f"The {tipo.lower()} names are:")
    for i in range(len(lista)):
        print(f" {i}. {lista[i]}")
           
def search_item_names(lista, tipo):
    index = None
    if not lista: # Si la lista está vacía []
        print("The list is empty! No cats to search.")
        return None
    while True:
        selector = input(f"Select the way you want to search a {tipo.lower()} from list {tipo.lower()}s. By index press 1. By name press 2. To cancel the search press 3.").strip()

        if selector == "1":
            try:
                user_input_index = input("Enter an index number: ").strip()
                index = int(user_input_index)
                name = lista[index]
                print(f"{index} is registered! Name is: {name}")
                return index

            except IndexError:
                print(f"{user_input_index} is not in {tipo.lower()}s list! Sorry!")
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
                print(f"{name} is not in {tipo.lower()}s list! Sorry!")

        elif selector == "3":
            print("Search canceled.")
            return None

        else:
            print("Error: select 1. or 2. or 3 to exit.")
            continue

def sorting_item_names(lista, tipo):
    lista.sort()
    show_item(lista, tipo)    

def random_item_message(animal):
    if animal == "CAT":
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
    elif animal == "DOG":
        messages = [
            "Woof! 🐕",
            "Bark bark...",
            "The dog is adorable!",
            "Dogs rule the world",
            "Paws are precious",
            "Buddy and cuddles",
            "Dog lovers unite!",
            "Woof means hello",
            "Dogs are the best",
            "Bark perfect"
            ]
        print(random.choice(messages))

def pretty_item_name(lista):
    target_index = search_item_names(lista)

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
            add_item(lista_activa, nombre_animal)
            continue
        elif selector == "2":
            show_item(lista_activa, nombre_animal)
            continue
        elif selector == "3":
            search_item_names(lista_activa, nombre_animal)
            continue
        elif selector == "4":
            remove_item(lista_activa)
            continue
        elif selector == "5":
            sorting_item_names(lista_activa, nombre_animal)
            continue
        elif selector == "6":
            random_item_message(nombre_animal)
            continue
        elif selector == "7":
            pretty_item_name(lista_activa)
            continue
        elif selector == "0":
            print("Goodbye!")
            return False
        else:
            print("Invalid option, try again.")

while True:
    if not menu():
        break
