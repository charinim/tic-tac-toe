class Board:
       def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(" " * self.size**2)
            #self.l1 = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            #self.l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            # the winner's sign O or X
            self.winner = ""
       def get_size(self): 
             # optional, return the board size (an instance size)
             return self.size
            
       def get_winner(self):
            # return the winner's sign O or X (an instance winner)     
            return self.winner 
       def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you
            labels = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            indices = [0,1,2,3,4,5,6,7,8]

            for i in range(len(labels)):
                if cell.upper() == labels[i]:
                    self.board[i] = sign
                    return indices[labels.index(cell)]


       def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)

            labels = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            index = [0,1,2,3,4,5,6,7,8]
            try:
                index = labels.index(cell.upper())
            except:
                return False
            
            if self.board[index] == " ":
                return True
            else:
                return False
       
       def isdone(self):
            done = False
            self.winner = ''


            if self.board[0] == self.board[1] == self.board[2] == "X":
                self.winner = "X"
                done = True
            elif self.board[0] == self.board[1] == self.board[2] == "O":
                self.winner = "O"
                done = True
            elif self.board[3] == self.board[4] == self.board[5] == "X":
                self.winner = "X"
                done = True
            elif self.board[3] == self.board[4] == self.board[5] == "O":
                self.winner = "O"
                done = True
            elif self.board[6] == self.board[7] == self.board[8] == "X":
                self.winner = "X"
                done = True
            elif self.board[6] == self.board[7] == self.board[8] == "O":
                self.winner = "O"
                done = True
            
            
            elif self.board[0] == self.board[3] == self.board[6] == "X":
                self.winner = "X"
                done = True
            elif self.board[0] == self.board[3] == self.board[6] == "O":
                self.winner = "O"
                done = True
            elif self.board[1] == self.board[4] == self.board[7] == "X":
                self.winner = "X"
                done = True
            elif self.board[1] == self.board[4] == self.board[7] == "O":
                self.winner = "O"
                done = True
            elif self.board[2] == self.board[5] == self.board[8] == "X":
                self.winner = "X"
                done = True
            elif self.board[2] == self.board[5] == self.board[8] == "O":
                self.winner = "O"
                done = True
            
            
            elif self.board[0] == self.board[4] == self.board[8] == "X":
                self.winner = "X"
                done = True
            elif self.board[0] == self.board[4] == self.board[8] == "O":
                self.winner = "O"
                done = True
            elif self.board[2] == self.board[4] == self.board[6] == "X":
                self.winner = "X"
                done = True
            elif self.board[2] == self.board[4] == self.board[6] == "O":
                self.winner = "O"
                done = True
            
            elif " " not in self.board:
                self.winner = " "
                done = True
            
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            return done

    
    
       def show(self):
            # draw the board
            print("   A   B   C")
            print(" +---+---+---+")
            print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
            print(" +---+---+---+")
            print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
            print(" +---+---+---+")
            print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
            print(" +---+---+---+")
