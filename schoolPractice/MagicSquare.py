import numpy as np
import random

class MagicSquare:
    def __init__(self, size):
        self.size = size
        self.magicSquare = random.sample(range(1, self.size**2+1), self.size**2)
        self.magicSquare = np.reshape(self.magicSquare, (self.size, self.size))

    def sumOfDiagonals(self):
        #if the sum of the diagonals is euqals- return the sum, if not- return -1
        sum = np.diag(self.magicSquare).sum()
        if sum == np.diag(self.magicSquare[::-1])[::-1].sum():
            return sum
        else:
            return -1
    
    def sumOfRows(self):
        #if the sum of the lines is euqals- return the sum, if not- return -1
        arrayOfSum = np.sum(self.magicSquare, axis = 0)

        if np.all(arrayOfSum == arrayOfSum[0]): #cheking if all the rows has the same sum
            return arrayOfSum[0]
        else:
            return -1
    
    def sumOfColumns(self):
        #if the sum of the columns is equals - return the sum, if not - return -1
        arrayOfSum = np.sum(self.magicSquare, axis = 1)

        if np.all(arrayOfSum == arrayOfSum[0]):
            return arrayOfSum[0]
        else:
            return -1
   

    def checkMagicSquare(self):
        #if the square is magic- return true, else return false

        if len(np.unique(self.magicSquare)) != len(self.magicSquare): #if there is at least one duplicate in the array
            return False
        
        arraySums = np.array([self.sumOfDiagonals(), self.sumOfRows(), self.sumOfColumns()])

        if -1 in arraySums: #if found -1
            return False
        
        if np.all(arraySums == arraySums[0]):
            return True
        else:
            return False


#square = MagicSquare(3)
#print(square.magicSquare)
       

ms = MagicSquare(3)
print(ms.magicSquare)
print(ms.checkMagicSquare())