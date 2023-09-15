import numpy as np
import random
import math

class Square:
    def __init__(self, digits):
        self.digits = np.array(digits)
        self.magicSquare = np.reshape(self.digits, (int(math.sqrt(len(self.digits))), int(math.sqrt(len(self.digits)))))

    def sumOfDiagonals(self):
        #if the sum of the diagonals is euqals- return the sum, if not- return -1
        sum = np.diag(self.magicSquare).sum()
        if sum == np.diag(np.flip(self.magicSquare, axis=0)).sum():
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
   
    def checkForDups(self):
        #true if there is no duplicates in the square
        #false if there is at least one duplicate in the square

        digit, times = np.unique(self.magicSquare, return_counts= True)
        #digits - every digit that appears in the sqaure
        #times - the amount of times the number appered in the square

        dups = digit[times > 1]#creating an array with only the numbers that has duplicate

        return len(dups) == 0 #if the length is 0, that means that there is no duplicate in the sqaure


    def checkMagicSquare(self):
        #if the square is magic- return true, else return false
        
        if not self.checkForDups():
            return False


        arraySums = np.array([self.sumOfDiagonals(), self.sumOfRows(), self.sumOfColumns()])

        if -1 in arraySums: #if found -1
            return False
        
        if np.all(arraySums == arraySums[0]):
            return True
        else:
            return False

