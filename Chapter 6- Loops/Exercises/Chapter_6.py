# This is the solution to Excercise 1

print("\tWelcome to freddie's pizzaria")
print("\nadd as many toppings as you want. \nWhen it's enough type\n\t 'QUIT'")

while 1:
    topping = input("Insert Topping: ")
    if topping == 'quit' : break
    print("\nadding {0} to your pizza".format(topping))


print("\nSufficient toppings succesfully added<3")

# This is the solution to Excercise 2
print("Welcome to the theatre house")
print("please confirm your age for movie ticket pricings<3")

while 1:
    age = int(input("How old are you?: "))
    if age < 3:
        print("You can have a free ticket!")
    elif age >= 3 and age <= 12:
        print("Your ticket will cost you $10")
    elif age > 12:
        print("Your ticket will cost you $15")
    else:
        print("You have entered an invalid input")
        print("Please try again,,,")

# This is the solution to Excercise 2

while 1:
    print("This is an infinite loop")