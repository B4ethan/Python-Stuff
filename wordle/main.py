import random
import simple_colors

word = open("/workspaces/Python-Stuff/wordle/words.txt").readlines()
word = random.choice(word).lower()

wordArr = []

for letter in word:
    wordArr.append(letter)


geusse = ""

while True:
    geusse = input("Enter your word: ")

    if geusse == word:
        print("You won!")
        break

    
    for letter in geusse:
        if letter not in word:
            print(simple_colors.red(letter) + " ")