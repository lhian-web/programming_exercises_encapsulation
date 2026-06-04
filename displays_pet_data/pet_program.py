from pet import Pet

pet = Pet()

print("PET REGISTRATION")

name = input("Enter pet name: ").strip()
pet.set_name(name)

animal_type = input("Enter animal type: ").strip()
pet.animal_type(animal_type)

while True:
    try:
        age = int(input("Enter pet age: "))
        if age < 0:
            print("Age cannot be zero or less than zero. Try again")
            continue
        pet.set_age(age)
        break
    except ValueError:
        print("Please enter a valid integer.")
    