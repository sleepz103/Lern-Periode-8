# function
def sing_happy_birthday(name):
    for x in range(3):
        print(f"happy birthday {name}!")
    return name


name = sing_happy_birthday("roblin")
print(name)
