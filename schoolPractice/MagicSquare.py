import numpy as np
from itertools import permutations
from Square import Square

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

        valid = 0

        for option in self.combinations:
            square = Square(list(option))

            if square.checkMagicSquare(): #if found magic square
                self.MagicDict[valid] = np.arr_str(square.magicSquare)
                valid = valid + 1


s = MagicSquare(3)
s.addAllMagicToDict()
