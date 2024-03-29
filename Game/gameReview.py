import numpy as np
import random
import json
import copy

#if the agent cant win in the next move, he should first check if the opp can win, and block him.

class game_tictactoe:
    #we will play as (2), opponnent will be (1)
    def __init__(self):
        self.board = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
        self.won = None

        #the higher the point the better the result
        self.winPoints = 1 
        self.tiePoints = .5
        self.lostPoints = 0
        self.gama = .9
        self.blockPoints = (self.winPoints + self.gama)/2
 
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
            
        diag = np.diag(np.fliplr(self.board))

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

    def smartAgent(self):
        pass

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

        self.boards = []
        self.blockBoards = [] #a list with all the boards where the agent needs to block the oppenent

        while True:
            #checking for blocks
            for place in self.allValidPlace():
                self.board[place[0]][place[1]] = 2

                if self.isWin() == 2:
                    self.board[place[0]][place[1]] = 1
                    self.blockBoards.append(','.join(self.board.flatten().astype(str)))
                
                self.board[place[0]][place[1]] = 0
            
            self.agentTurn()
            #self.printBoard()
            #print()
            self.boards.append(','.join(self.board.flatten().astype(str)))

            if self.isWin() == 1:
                #print("agent won!\n")
                return self.winPoints
                
                
            if self.tie():
                #print("tie!\n")
                return self.tiePoints
                

            self.oppTurn()
            #self.printBoard()
            #print()
            self.boards.append(','.join(self.board.flatten().astype(str)))
            
            if self.isWin() == 2:
                #print("opp won!\n")
                return self.lostPoints
            
    def givePoints(self):
        result = self.playGame()

        self.boardsWpoint = {}
        self.blockBoardsWpoint = {} #a list with all the boards where the agent needs to block the oppenent and its points

        for i, board in enumerate(reversed(self.boards)):
            self.boardsWpoint[board] = result * (self.gama ** i)

        for board in self.blockBoards:
            self.blockBoardsWpoint[board] = self.blockPoints
  
    
class games:
    def __init__(self):
        self.agentWins = 0
        self.oppWins = 0
        self.gamesPlayed = 1_000_000

        self.allBoards = {}  
        
        try:
            with open('Game\\boards.json', 'r') as data:
                loaded_data = json.load(data)
                if loaded_data:  # Check if the loaded data is not empty
                    self.allBoards = loaded_data
        except (FileNotFoundError, json.JSONDecodeError):
            pass  
        
    def play(self):
        
        for i in range (self.gamesPlayed):
            #print(f'game {i+1}')
            gameBoard = game_tictactoe()
            
            gameBoard.givePoints()

            for board, points in gameBoard.boardsWpoint.items():
                if board not in self.allBoards:
                    self.allBoards[board] = (points, 1)
                else:
                    prev = self.allBoards[board]
                    self.allBoards[board] = ((prev[0] * prev[1] + points) / (prev[1] + 1), prev[1] + 1)

            for board, points in gameBoard.blockBoardsWpoint.items():
                if board not in self.allBoards:
                    self.allBoards[board] = (points, 1)
                else:
                    prev = self.allBoards[board]
                    self.allBoards[board] = (points, prev[1] + 1)

            if i % 100_000 == 0:
                print(i)

        print("done!\n")

    def saveToJson(self):
        with open('Game\\boards.json', 'w') as data:
            json.dump(self.allBoards, data)



#tenGames = games()
#tenGames.play()

#print(f"result: \n agent num of wins: {tenGames.agentWins} \n opponent num of wins: {tenGames.oppWins}")


Mgames = games()
Mgames.play()
Mgames.saveToJson()

'''
oneGame = game_tictactoe()

oneGame.givePoints()
print(oneGame.boardsWpoint)
print("and")
print(oneGame.blockBoardsWpoint)
'''
