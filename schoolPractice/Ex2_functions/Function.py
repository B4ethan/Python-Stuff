
class Function:
    def __init__(self, a, b, c):
        #get the varibales - ax^2 + bx + c
        self.a = a
        self. b = b
        self. c = c

    def getFunction(self):
        #return the function
        return f"{self.a}x^2 {self.b}x {self.c}"
    
    def calcDerFunc(self, Xvalue):
        return self.a * 2 * Xvalue + self.b

    '''
    def findMinimum(self, epochs = 1000, learningRate = 0.001):
        #finding the minimum point
        self.calcDerFunc()
        numberToCheck = 0

        while abs(self.derA) > self.EPSILON or epochs > 0:
            numberToCheck -= self.derA * self.EPSILON
            self.derA = self.a * 2 * numberToCheck + self.b
            epochs -= 1

        return f"({numberToCheck}, {(self.a * numberToCheck**2) + self.b * numberToCheck + self.c})"
    '''
    def findMinimum(self, epochs = 1000, learningRate = 0.001):
        value = self.calcDerFunc(5)
        Xpoint = 0

        while epochs > 0 or abs(value) > learningRate:
            Xpoint = Xpoint - learningRate  * value
            value = self.calcDerFunc(Xpoint)
            epochs -= 1
        
        return f"({Xpoint}, {(self.a * Xpoint**2) + self.b *Xpoint + self.c})"


func = Function(1 , 2, 2)
print(func.findMinimum())


