# This is the solution to Excercise 1

from audioop import reverse


names = ["kaye", "chrizalee", "lyla", "sophia"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])


# This is the solution to Excercise 2

names = ["kaye", "chrizalee", "lyla", "sophia"]

print(names[0], ", goodluck with ur band!")
print("hi",names[1],", i hope u get into your dream college")
print("hey,",names[2],"i miss playin softball with you")
print("sup",names[3],"i miss copyin ur answers in tests")


# This is the solution to Excercise 3

transpo = ["metro", "car", "boat"]

print("i will buy my dream sports",transpo[1],"which is the porsche 9/11 model")
print(transpo[0],"is convenient, but it is costly")
print("I once road a ",transpo[2],"to a vacation spot with my family")


# This is the solution to Excercise 4

people = ["Micheal Jackson", "Zild", "RM"]

print("Hi", people[0], "I'd like to invite you to dinner, Tell me your life story")
print("Hi po", people[1], "Can you tell me how to be a succesful musician over dinner?")
print("Hi", people[2],"form BTS, how did you and your members master the art of performing? Let's have a chat at my place 8 pm;>")


# This is the solution to Excercise 5

people = ["Micheal Jackson", "Zild", "RM"]

print("Hi", people[0], "I'd like to invite you to dinner, Tell me your life story")
print("Hi po", people[1], "Can you tell me how to be a succesful musician over dinner?")
print("Hi", people[2],"form BTS, how did you and your members master the art of performing? Let's have a chat at my place 8 pm;>")

print(people[0],"can't make it to dinner")

people[0] = "Avril Lavigne"

print("Hi", people[0], "I'd like to invite you to dinner, Tell me your life story")
print("Hi po", people[1], "Can you tell me how to be a succesful musician over dinner?")
print("Hi", people[2],"form BTS, how did you and your members master the art of performing? Let's have a chat at my place 8 pm;>")


# This is the solution to Excercise 6

people = ["Micheal Jackson", "Zild", "RM"]
print(people[0],"can't make it to dinner")

people[0] = "Avril Lavigne"
print("Hi", people[0], "I'd like to invite you to dinner, Tell me your life story")
print("Hi po", people[1], "Can you tell me how to be a succesful musician over dinner?")
print("Hi", people[2],"form BTS, how did you and your members master the art of performing? Let's have a chat at my place 8 pm;>")

print("You can only invite two people to dinner.")
people.pop

print(people[0],"You are still invited to dinner")
print(people[1],"You are still invited to dinner")

del people[:]
print(people)


# This is the solution to Excercise 7

#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["maldives", "aurora lights", "seoul", "tokyo","harajuku"]
#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
print(places)

#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
#•	 Show that your list is still in its original order by printing it.
a = sorted(places)
print(a)
print(places)

#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
b = sorted(places, reverse=True)
print(b)
print(places)

#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)

#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print(places)

#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print(places)

#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)