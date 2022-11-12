# This is the solution to Excercise 1
def display_message():
    print("We are learning python functions in chapter 7!")


display_message() 

# This is the solution to Excercise 2
def favorite_book(book_title):
    print(f"\nMy favorite book is {book_title}") 


favorite_book("atomic habits")

# This is the solution to Excercise 3
def make_shirt(size, message):
    print(f"\nT-shirt size: {size} \nPrinted Message: {message}")


make_shirt("small","have a good day")
make_shirt(message="4lyfers", size="large")

# This is the solution to Excercise 4
def make_shirt(size='large', message='I love Python!'):
    print(f"\nT-shirt size is {size}")
    print(f"Printed Message is {message}")

make_shirt()
make_shirt(size='medium')
make_shirt('small','Programmers are cute')


# This is the solution to Excercise 5
def describe_city(city,country='japan'):
    print(f"\n{city} is in {country}")


describe_city('kyoto')
describe_city('manila','philippines')
describe_city('new york','america')



#Extra Excercises---------------------------------
# Write a program to print all the names in a list

names = ["patrice", "hannah","sandy", "princess"]

def call_name(name):
  for x in names:
    print("Her name is", x)

call_name(names)

# Write a python function to check whether a number falls in a given range
range_1 = range(6)
user_input = int(input("Input number: "))

def range_check(range):
    if user_input in range_1:
        print("Number is in range a")
    else:
        print("Number is not in range a")

range_check(user_input)

# Write a program that takes a number from user and check whether the number is prime or not
print("This function checks whether number is prime or not")
num = int(input("Input number: "))

def prime_noprime(number):
    for i in range(2,number):
        if number % i == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")

prime_noprime(num)


#User input in calling functions
print("THIS IS AN IMITATION OF SIRI")

mac_response = ["How are you today?","okay see you later<3","thats great to hear<3, enjoy your day!"]
user_input = input("\nHey user! ")


def comp_ans(response):
    if user_input == "hey mac!":
        print(mac_response[0])
        userf = input()
        if userf == "im good":
          print(mac_response[2])
    elif user_input == "no":
        print(mac_response[1])
    else:
        print("wrong input")

comp_ans(user_input)
        

#Calculator function

print("THIS IS A SIMPLE CALCULATOR")
math_symbols = ["add","subtract","divide","multiply"]
i = 0
for x in math_symbols:
  i += 1
  print(i,x)

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

while True:
    choice = input("\nChoose math equation: ")

    if choice in ('1','2','3','4'):
        num1 = float(input("Input number: "))
        num2 = float(input("Input number: "))

        if choice == '1': 
            print(num1,"+",num2,"=", add(num1,num2))
        if choice == '2': 
            print(num1,"-",num2,"=", subtract(num1,num2))
        if choice == '3': 
            print(num1,"/",num2,"=", divide(num1,num2))
        if choice == '4': 
            print(num1,"*",num2,"=", multiply(num1,num2))
        
        next_calculation = input("Comtinue? yes/no : ")
        if next_calculation == "no":
            print("\nthank you for using calculator<3")
            break
    else:
        print("Invalid input")