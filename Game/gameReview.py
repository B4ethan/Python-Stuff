import numpy as np
import random

class game_tictactoe:
    #we will play as (2), opponnent will be (1)
    def __init__(self):
        self.board = np.zeros((3,3))
        self.won = None

    #return a list of the leagal places (tupples)
    def allValidPlace(self):
        zero_indices = [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]


    #returns 0 if there is no win, 1 if opponnent won, 2 if we won 
    def isWin(self):
        pass

    #return true if the board is full, and no one wins
    def tie(self):
        pass

    def agentTurn(self, place = None):
        if place == None: #if no place is given
            place = random.choice(self.allValidPlace())

    def oppTurn(self, place = None):
        if place == None: #if no place is given
            place = random.choice(self.allValidPlace())
    
    def printBoard(self):
        print(self.board)

    def playGame(self):
        pass

class games:
    def __init__(self):
        self.agentWins = None
        self.oppWins = None
        self.gamesPlayed = 1_000_000


game = game_tictactoe()
game.board = np.array([[1.0, 0.0, 3.0],
                  [0.0, 5.0, 0.0],
                  [7.0, 0.0, 9.0]])

print(game.allValidPlace())