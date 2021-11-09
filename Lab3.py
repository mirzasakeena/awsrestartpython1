"""
Your module description
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is the data type of " + str(type(myString)))
firstString =  "Water"
secondString = "Fall"
f = " "
thirdString = firstString + f + secondString
print(thirdString)
"""
name = input("What is your name?")
print("Hello, Welcome" name)
age = int(input("What is your age?"))
color = input("What is your favourite color?")
animal = input("What is your favourite animal?")
print("{}, you like a {} {}!" .format(name, color, animal))