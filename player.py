from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  
            self.sign = sign 
      def get_sign(self):
            return self.sign
      def get_name(self):
            return self.name
      def choose(self, board):
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
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1
            elif board.get_winner() == self.other_sign:
                return -1
            else:
                return 0
            
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