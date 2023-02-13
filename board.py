class Board:
       def __init__(self):
            self.sign = " "
            self.size = 3
            self.board = list(" " * self.size**2)
            self.winner = ""

       def get_size(self): 
             return self.size
            
       def get_winner(self):
            return self.winner 
       def set(self, cell, sign):
            labels = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
            indices = [0,1,2,3,4,5,6,7,8]

            for i in range(len(labels)):
                if cell.upper() == labels[i]:
                    self.board[i] = sign
                    return indices[labels.index(cell)]


       def isempty(self, cell):
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
            return done

    
    
       def show(self):

            print("   A   B   C")
            print(" +---+---+---+")
            print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
            print(" +---+---+---+")
            print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
            print(" +---+---+---+")
            print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
            print(" +---+---+---+")
