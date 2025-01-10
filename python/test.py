# variables
patientFirstName = "John"
patientLastName = "Smith"
patientAge = 20
patientIsNew = True

# print, terminal input
print(patientAge)
print(50)
name = input("What is your name ")
print("Hello " + name)

# conversion
age = input("How old are you? ")
ageText = str(age)
ageInt = int(ageText)


# Operators
# > < == != <= >=
# AND OR NOT

# if
temperature = 20
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
elif temperature < 10:
    print("It's a cold day")
print("Done")

# lists
names = ["John","Bob",'Mosh']
print(names[-1])
print(names[0:2])

numbers = [1,2,3,4,5,6]
numbers.insert(0, -1)
hasOne = 1 in numbers



# function
def sing_happy_birthday():
    for x in range(3):
        print("happy birthday!")