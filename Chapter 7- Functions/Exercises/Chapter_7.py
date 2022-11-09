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


# This is the solution to Excercise 4
def describe_city(city,country='japan'):
    print(f"\n{city} is in {country}")


describe_city('kyoto')
describe_city('manila','philippines')
describe_city('new york','america')