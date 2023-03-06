import json

# 1. Läs in befintliga hundar från filen "kennel.json"
try:
    with open('kennel.json', 'r') as f:
        kennel = json.load(f)
except FileNotFoundError:
    kennel = []

# 2. Skapa funktioner för att lägga till, lista, ta bort och spara hundar
def add_dog():
    name = input("Namn: ")
    breed = input("Ras: ")
    age = int(input("Ålder: "))
    weight = int(input("Vikt: "))
    if breed == "Tax":
        tail_length = 3.7
    else:
        tail_length = age * weight / 10
    dog = {"name": name, "breed": breed, "age": age, "weight": weight, "tail_length": tail_length}
    kennel.append(dog)
    print("Hunden har registrerats.")

def list_dogs():
    min_tail_length = float(input("Minsta svanslängd: "))
    for dog in kennel:
        if dog["tail_length"] >= min_tail_length:
            print(f'{dog["name"]} {dog["breed"]} {dog["age"]} år {dog["weight"]} kg svans={dog["tail_length"]:.1f}')

def remove_dog():
    name = input("Namn: ")
    for dog in kennel:
        if dog["name"] == name:
            kennel.remove(dog)
            print("Hunden är borttagen.")
            return
    print("Hund med det namnet fanns ej i registret.")

def save_dogs():
    with open('kennel.json', 'w') as f:
        json.dump(kennel, f)

# 3. Huvudprogrammet
while True:
    print("\n1. Registrera hund")
    print("2. Lista hundar")
    print("3. Ta bort hund")
    print("4. Avsluta")
    choice = input("Välj ett alternativ: ")
    if choice == "1":
        add_dog()
    elif choice == "2":
        list_dogs()
    elif choice == "3":
        remove_dog()
    elif choice == "4":
        save_dogs()
        break
    else:
        print("Ogiltigt val. Försök igen.")
