# Chapter 6 Exercises

Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  

---
&nbsp;

## Exercise 1: Pizza Toppings :ballot_box_with_check:

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.


# This is the solution to Excercise 1

print("\tWelcome to freddie's pizzaria")
print("\nadd as many toppings as you want. \nWhen it's enough type\n\t 'QUIT'")

while 1:
    topping = input("Insert Topping: ")
    if topping == 'quit' : break
    print("\nadding {0} to your pizza".format(topping))


print("\nSufficient toppings succesfully added<3")

&nbsp;
&nbsp;

## Exercise 2: Movie Tickets: :ballot_box_with_check:

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 

age, and then tell them the cost of their movie ticket

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

&nbsp;
&nbsp;

## Exercise 3: Infinity :ballot_box_with_check:

Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)


# This is the solution to Excercise 3

while 1:
    print("This is an infinite loop")
    
&nbsp;
&nbsp;

## Exercise 4: Deli :ballot_box_with_check:

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# This is the solution to Excercise 4

sandwhich_orders = ["egg sandwhich","hotdog sandwhich","steak sandwhich"] #sandwhich orders list 
finished_sandwhiches = [] # empty finished sandwhiches list


for x in sandwhich_orders : #for loop: print sandwhiches and append each variable x in finished sandwhiches
    finished_sandwhiches.append(x)
    print("I have made your", x)

print("Finished Sandwhiches:",finished_sandwhiches)

&nbsp;
&nbsp;

## Exercise 5: No Pastrami :ballot_box_with_check:

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

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

&nbsp;
&nbsp;


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