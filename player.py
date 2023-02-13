from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
        
            
            while True:
                cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ').upper()
                if board.isempty(cell):
                    board.board[board.set(cell, self.sign)] = self.sign
                    break
                
                else:
                    print("You did not choose correctly")          
            

class AI(Player):
    def __init__(self, name, sign, board = None):
        self.name = name
        self.sign = sign
        self.moves = self.available_moves(board)
    
    def available_moves(self, board = None):
        if board != None:
            n = board.get_size()
        else:
            n = 3
        available_moves = []
        for char in range(65, 65+n):
            for i in range(1, 1+n):
                available_moves.append(chr(char) + str(i))
        return available_moves

    def choose(self, board=None):
        print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        
        cell = choice(self.moves)
        while board.isempty(cell)!=True:
            cell = choice(self.moves)
        
        board.board[board.set(cell, self.sign)] = self.sign
        self.moves.remove(cell)
            
        

class MiniMax(AI):
    def __init__(self, name, sign, board):
        self.name = name
        self.sign = sign
        self.board = board
        self.other_sign = ""
        if self.sign == "O":
             self.other_sign= "X"
        else:
            self.other_sign = "O"
    
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.board[board.set(cell, self.sign)] = self.sign
    
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == self.other_sign:
                return -1
            # self is a looser (opponent is a winner)
            else:
                return 0
            
        
        # make a move (choose a cell) recursively
        else:
            min = 3000
            max = -3000
            score = 0
            x = ''
            moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
          
            for cell in moves:
                if board.isempty(cell):      
                    if self_player == True:
                        board.board[board.set(cell, self.sign)] = self.sign
                        score = MiniMax.minimax(self, board, False, False)
                        if score > max:
                            max = score
                            x = cell
            
                    else:
                        board.board[board.set(cell, self.other_sign)] = self.other_sign
                        score = MiniMax.minimax(self, board, True, False)
                        x = cell
                        if score < min:
                            min = score
                            x = cell
                    board.board[board.set(cell,' ')] = " "
                    
            
            if start == True:
                return x
            elif self_player == True:
                return max
            else:
                return min
            # use the pseudocode given to you above to implement the missing code