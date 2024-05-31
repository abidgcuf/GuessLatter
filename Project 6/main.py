import random

word_list = ["Baboon","camel","ardwark"]

random.choice(word_list)

guess = input("Guess a latter:").lower()

for letter in word_list:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")