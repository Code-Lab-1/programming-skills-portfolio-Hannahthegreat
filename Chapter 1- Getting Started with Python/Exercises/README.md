# Chapter 1 Exercises

Exercises with a tick mark :ballot_box_with_check: represent exercises that must be submitted as part of your Programming Skills Portfolio as a minimum expectation. Completing more exercises provides the opportunity to attain higher marks. For each exercise you should create a _**new project**_ with the name of the exercise and save it to this exercises folder in your local repository.

Once you have completed your solution you should make sure you commit and push your solutions to your remote repository on GitHub. You can commit and push as many changes to your solutions as you wish, only those pushed before the chapter deadlines will be marked for the Programming Skills Portfolio.  


&nbsp;

## Exercise 1: Print Strings :ballot_box_with_check:

Write a Python program to print the following string in a specific format.

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

# This is the solution to Excercise 1
print("Twinkle, twinkle, little star, How I wonder what you are!")

print("How I wonder what you are! Up above the world so high, Like a diamond in the sky.")

print("Twinkle, twinkle, little star, How I wonder what you are")


&nbsp;
&nbsp;
&nbsp;
## Exercise 2: Print the Version of Python :ballot_box_with_check:

 Write a Python program to get the Python version you are using.

# This is the solution to Excercise 2
import sys

print("current python version")

print(sys.version)

&nbsp;
&nbsp;
&nbsp;
## Exercise 3: Print date and Time :ballot_box_with_check:

Write a Python program to display the current date and time.

# This is the solution to Excercise 3
import datetime as dt

current_datetime = dt.datetime.now()

print("Current date and time")

print(current_datetime)

&nbsp;
&nbsp;
&nbsp;
## Exercise 4: Strings Concatination :ballot_box_with_check:
Write three strings in different variables and print the output as one string.
# This is the solution to Excercise 4
a = "apple"

b = "banana"

c = "coke"

print(a,b,c)

&nbsp;
&nbsp;
&nbsp;

## Exercise 5: Compute area of Circle :ballot_box_with_check:

Write a Python program which accepts the radius of a circle from the user and compute the area.

# This is the solution to Excercise 5
from math import pi

radius = int(input("Input Circle Radius: ", ))


area = pi*radius**2

print("Circle area with the radius",radius , "is", area)

&nbsp;
&nbsp;
&nbsp;

