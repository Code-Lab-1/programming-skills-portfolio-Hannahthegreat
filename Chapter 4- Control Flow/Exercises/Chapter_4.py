# This is the solution to Excercise 1
alien_color = "green", "yellow", "red"

alien_color="green"
if alien_color=="green":
    print("You just earned five points")

alien_color="red"
if alien_color=="green":
    print("You just earned five points")


# This is the solution to Excercise 2
alien_color = "green", "yellow", "red"

alien_color = "green"
if alien_color=="green":
    print("You shot an alien!")
    print("+5 points")
else:
    print("You earned 10 points")

alien_color = "yellow"
if alien_color=="green":
    print("You shot an alien!")
    print("+5 points")
else:
    print("You earned 10 points")

# This is the solution to Excercise 3
print("Aliens: green, yellow, red")
alien_color= input("Alien color: ")

if alien_color== "green":
    print("You have earned +5 points!")
elif alien_color== "yellow":
    print("You have earned +10 points!")
elif alien_color=="red":
    print("You have earned +15 points!")

# This is the solution to Excercise 4
age = int(input("Age: "))

if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else:
    print("You are an elder")

# This is the solution to Excercise 5
favourite_fruits = ["apple", "banana", "grape"]

if "orange" in favourite_fruits:
    print("You really like oragnes!")
if "grape" in favourite_fruits:
    print("You really like grapes!")
if "cherries" in favourite_fruits:
    print("You really like cherries!")
if "banana" in favourite_fruits:
    print("You really like bananas!")
if "apple" in favourite_fruits:
    print("You really like apples!")

