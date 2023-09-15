import numpy as np
from itertools import permutations
from Square import Square
import json

class MagicSquare:
    def __init__(self, size):
        self.MagicDict = { }
        self.size = size
        self.combinations = []

        #creating an array of the numbers
        for number in range(1, self.size**2+1):
            self.combinations.append(number)

        self.combinations = list(permutations(self.combinations))


    def addAllMagicToDict(self):
        #checking all the array if they are magic square, if so, adding it to array

        valid = 1

        for option in self.combinations:
            square = Square(list(option))

            print(square.magicSquare)
            print()

            if square.checkMagicSquare(): #if found magic square
                self.MagicDict[valid] = f"{square.magicSquare}  \n"
                valid = valid + 1


def writeToJson(newData):
    #converting data to json file

    with open ("/workspaces/Python-Stuff/schoolPractice/magicSquare.json", "w") as data:
        json.dump(newData, data)


def main():
    s = MagicSquare(3)
    s.addAllMagicToDict()
    writeToJson(s.MagicDict)

if __name__ == "__main__":
    main()