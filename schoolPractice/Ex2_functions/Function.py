
class Function:
    def __init__(self, a, b, c):
        #get the varibales - ax^2 + bx + c
        self.a = a
        self. b = b
        self. c = c
        self.EPSILON = 1e-6

    def getFunction(self):
        #return the function
        return f"{self.a}x^2 {self.b}x {self.c}"
    
    def findMinimum(self):
        #finding the minimum point
        self.der = self.a * 2
        numberToCheck = 0

        while abs(self.der) > self.EPSILON:
            numberToCheck -= self.der * self.EPSILON
            self.der = self.a * 2 * numberToCheck + self.b


        return f"({numberToCheck}, {(self.a * numberToCheck**2) + self.b * numberToCheck + self.c})"


func = Function(0 , 0, 0)
print(func.findMinimum())


