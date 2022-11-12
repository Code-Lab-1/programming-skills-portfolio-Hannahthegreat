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

# This is the solution to Excercise 3

while 1:
    print("This is an infinite loop")

# This is the solution to Excercise 4

sandwhich_orders = ["egg sandwhich","hotdog sandwhich","steak sandwhich"] #sandwhich orders list 
finished_sandwhiches = [] # empty finished sandwhiches list


for x in sandwhich_orders : #for loop: print sandwhiches and append each variable x in finished sandwhiches
    finished_sandwhiches.append(x)
    print("I have made your", x)

print("Finished Sandwhiches:",finished_sandwhiches)


# This is the solution to Excercise 5
sandwhich_orders = ["egg sandwhich","pastrami","hotdog sandwhich","pastrami","steak sandwhich","pastrami"] #sandwhich orders list 
finished_sandwhiches = [] # empty finished sandwhiches list

print("Deli has unfortunately ran out of pastrami")
print("\n")

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')
    print("Removing pastrami>>>",sandwhich_orders)

print("\n")

for x in sandwhich_orders: 
    finished_sandwhiches.append(x)
    print("I have made your", x)

print("\nFinished Sandwhiches:",finished_sandwhiches)



#Extra Excercises---------------------------------
#User input will be added in empty list
list = []
for i in range (3):
    user_input = input("Input your values in the list: ")
    list.append(user_input)

print(list)

#Displaying numbers in range using for loop
for i in range(10):
    print(1)

#Displaying numbers using while loop
z = 0 
while z < 10:
  z += 1
  print(z)

#looping through a list
favorite_cafes = ["bubbee","starbucks","tim hortons"]

for x in favorite_cafes:
  print("i love ", x)


#looping through a list a user has created
print("Name your favorite snacks to add to your cart")

snack_list = []
while True:
    user_input = input("snacks: ")
    snack_list.append(user_input)
    print(user_input, "has been added to your cart!")
    if user_input == "enuff snacks":
        break

cart_total = len(snack_list)
print("Your cart contains", snack_list, "=",cart_total)
print("Thank you for shopping with us!")