import random
import simple_colors

word = open("/workspaces/Python-Stuff/wordle/words.txt").readlines()
word = random.choice(word).lower()

wordArr = []

for letter in word:
    wordArr.append(letter)


geusse = ""

while not geusse == word :
    geusse = input("Enter your word: ")

    index = 0

    for letter in geusse:
        if letter not in word:
            print(simple_colors.red(letter), end= " ")
        elif letter in word and letter == word[index]:
            print(simple_colors.green(letter), end= " ")
        else:
            print(letter, end= " ")
        index = index + 1

    print()

print("Yay! you geussed the word! it was: " + word)