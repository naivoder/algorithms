"""
this file is a simple game of tic-tac-toe against the computer, just for fun

"""
import random

class PlayerO():
    def __init__(self):
        self.icon = 'O'

    def generateMove(self, board):
        found = False; tries = 0
        while not found and tries <= 9:
            position = random.randint(1,10)
            tries += 1
            if board.moveAvailable(position):
                print("Computer move: ", position)
                board.updateMove(self.icon, position)
                print(board)
                found = True
        if found is False and tries > 9:
            return False
        return True

class PlayerX():
    def __init__(self):
        self.icon = 'X'

    def getMove(self, board):
        desired = input("Enter a number (1-9) to make your move! ")
        try:
            int(desired)
        except:
            print("You must enter a number!")
            self.getMove(board)
        if board.moveAvailable(desired):
            board.updateMove(self.icon, desired)
            print(board)
        else:
            print("That space is already taken!")
            self.getMove(board)

class Board():

    def __init__(self):
         self.view = "\n*-----*\n|1|2|3|\n|4|5|6|\n|7|8|9|\n*-----*\n"
         self.board = [[0 for col in range(3)] for row in range(3)]

    def __str__(self):
        return ''.join(self.view)

    def moveAvailable(self,position):
        for char in self.view:
            if char == str(position):
                return True
        else:
            return False

    def updateMove(self, player, position):
        position = int(position)
        if position - 3 > 0:
            # bottom row
            if position - 6 > 0:
                row = 2
                col = (position - 7)
                self.board[row][col] = player
                for char in self.view:
                    if char == str(position):
                        remainder = self.view[self.view.index(char)+1:]
                        self.view = self.view[0:self.view.index(char)]
                        self.view += player
                        self.view += remainder
            # middle row
            else:
                row = 1
                col = (position - 4)
                self.board[row][col] = player
                for char in self.view:
                    if char == str(position):
                        remainder = self.view[self.view.index(char)+1:]
                        self.view = self.view[0:self.view.index(char)]
                        self.view += player
                        self.view += remainder
        # top row
        else:
            row = 0
            col = (position - 1)
            self.board[row][col] = player
            for char in self.view:
                if char == str(position):
                    remainder = self.view[self.view.index(char)+1:]
                    self.view = self.view[0:self.view.index(char)]
                    self.view += player
                    self.view += remainder

    def checkForWin(self):
        # horizontal win
        for i in range(3):
            if (self.board[i][0] == self.board[i][1]) and (self.board[i][0] == self.board[i][2]) and (self.board[i][0] != 0):
                return True, self.board[i][0]
        # vertical win
        for i in range(3):
            if (self.board[0][i] == self.board[1][i]) and (self.board[0][i] == self.board[2][i]) and (self.board[0][i] != 0):
                return True, self.board[0][i]
        # diagonal forward win
        if (self.board[0][0] == self.board[1][1]) and (self.board[0][0] == self.board[2][2]) and (self.board[0][0] != 0):
            return True, self.board[0][0]
        # diagonal reverse win
        if (self.board[2][0] == self.board[1][1]) and (self.board[2][0] == self.board[0][2]) and (self.board[2][0] != 0):
            return True, self.board[2][0]

        return False, None


if __name__=="__main__":
    board = Board()
    computer = PlayerO()
    user = PlayerX()
    gameOver = False; winner = None;
    print("Welcome, Player X!")
    print(board)
    moves = 0

    while not gameOver:
        user.getMove(board)
        gameOver, winner = board.checkForWin()
        if winner is not None:
            break
        gameOn = computer.generateMove(board)
        if not gameOn:
            break
        gameOver, winner = board.checkForWin()

    if winner is None:
        print("Nobody won this game!")
    else:
        print("Player %s is the winner!" % winner)
