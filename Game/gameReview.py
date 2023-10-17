import numpy as np
import random

class game_tictactoe:
    #we will play as (2), opponnent will be (1)
    def __init__(self):
        self.board = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
        self.won = None

    #return a list of the leagal places (tupples)
    def allValidPlace(self):
        valid = [] #array with all the valid places

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0: #if found a valid place
                    valid.append((i, j)) #add the place to the array
        return valid


    #returns 0 if there is no win, 1 if opponnent won, 2 if we won
    def isWinRow(self): #checking for win in the rows
        for i in range(3):
            row = self.board[i, :]

            if np.all(row == row[0]): #if all the number in the row is the same (someone win, or no one placed)
                if row[0] == 1:
                    return 1
                elif row[0] == 2:
                    return 2
                
        return 0

    def isWinColumn(self): #checking for wim in the columns
        for i in range(3):
            row = self.board[:, i]

            if np.all(row == row[0]): #if all the number in the column is the same (someone win, or no one placed)
                if row[0] == 1:
                    return 1
                elif row[0] == 2:
                    return 2
                
        return 0

    def isWinDiag(self): #cheking for win in the diagonals
        diag = np.diag(self.board)

        if np.all(diag == diag[0]): #if all the number in the diagonal is the same (someone win, or no one placed)
            if diag[0] == 1:
                return 1
            if diag[0] == 2:
                return 2
            
        diag = np.diag(np.flip(self.board))

        if np.all(diag == diag[0]): #if all the number in the diagonal is the same (someone win, or no one placed)
            if diag[0] == 1:
                return 1
            if diag[0] == 2:
                return 2
        return 0

    def isWin(self):
        wins = [self.isWinRow(), self.isWinColumn(), self.isWinDiag()]

        if 1 in wins:
            return 1
        elif 2 in wins:
            return 2
        else:
            return 0

    #return true if the board is full, and no one wins
    def tie(self):
        return self.allValidPlace() == [] and self.isWin() == 0

    def agentTurn(self, place = None):
        if place == None: #if no place is given
            place = random.choice(self.allValidPlace())
        else:
            while place not in self.allValidPlace():
                xPlace = int(input("pls enter a valid x place: "))
                yPlace = int(input("pls enter a valid y place: "))\
                
                place = (xPlace, yPlace)

        self.board[place[0]][place[1]] = 1

    def oppTurn(self, place = None):
        if place == None: #if no place is given
            place = random.choice(self.allValidPlace())
        else:
            while place not in self.allValidPlace():
                xPlace = int(input("pls enter a valid x place: "))
                yPlace = int(input("pls enter a valid y place: "))\
                
                place = (xPlace, yPlace)

        self.board[place[0]][place[1]] = 2
    
    def printBoard(self):
        print(self.board)

    
    def playGame(self):
        #self.printBoard()
        #print()

        while True:
            self.agentTurn()
            #self.printBoard()
            #print()

            if self.isWin() == 1:
                print("agent won!\n")
                return 1
                
            if self.tie():
                print("tie!\n")
                return 0

            self.oppTurn()
            #self.printBoard()
            #print()
            
            if self.isWin() == 2:
                print("opp won!\n")
                return 2

class games:
    def __init__(self):
        self.agentWins = 0
        self.oppWins = 0
        self.gamesPlayed = 10

    def play(self):
        
        for i in range (self.gamesPlayed):
            print(f'game {i+1}')
            result = game_tictactoe().playGame()

            if result == 1:
                self.agentWins += 1
            elif result == 2:
                self.oppWins += 1
        print("done!\n")



tenGames = games()
tenGames.play()

print(f"result: \n agent num of wins: {tenGames.agentWins} \n opponent num of wins: {tenGames.oppWins}")
            
