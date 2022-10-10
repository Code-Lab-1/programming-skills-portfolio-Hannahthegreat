# This is the solution to Excercise 1

sentence_1 = "Hello this is the start of human mass extinction."
print(sentence_1)

sentence_1 = "Bomb will detonate in 3 seconds."
print(sentence_1)

# This is the solution to Excercise 2
quote = "My dog stepped on a bee"
author = "Amber Heard"

print(author, "once said, ", quote)

# This is the solution to Excercise 3

list = ['\tPatrice\n', '\tSandy\n', '\tPrincess\n']
print(list[0].lstrip())
print(list[1].rstrip())
print(list[2].strip())


# This is the solution to Excercise 4
fav_num = 14

print("My lucky number is ", fav_num)

# This is the solution to Excercise 5

usb = 6
money = 50

result = int(money/usb)
change = money - (result * usb)
print("The equation: {0} / {1}\n".format(usb,money))
print("She will get {0} amount of sticks".format(result))
print("Her change is: {0}".format(change))