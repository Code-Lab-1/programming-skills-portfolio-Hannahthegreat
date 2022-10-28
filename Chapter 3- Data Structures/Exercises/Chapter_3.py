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

places = ["maldives", "aurora lights", "seoul", "tokyo","harajuku"]
print(places)

a = sorted(places)
print(a)
print(places)

b = sorted(places, reverse=True)
print(b)
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)