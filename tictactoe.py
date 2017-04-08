class Tictactoe(object):

    def __init__(self):
        self.EMPTY = '_'
        self.X = 'X'
        self.O = 'O'

        self.SIZE = 3

        self.reset()
        

    def make_move(self, pos):
        if (pos < self.SIZE**2 and self.board[pos] == self.EMPTY):
            self.board[pos] = self.turn
            self.print_board()

            if self.is_gameover():
                print(self.turn + " won!")
            elif self.is_board_full():
                print("It's a draw!")
            else:
                self.turn = self.next_turn()
        else:
            print("Invalid move")

    def next_turn(self):
       return (self.O if self.turn == self.X else self.X)

    def is_gameover(self):
        return self.is_row_over() or self.is_col_over() or self.is_diag_over()

    def is_board_full(self):
        non_empty = [not self.board[i] == self.EMPTY for i in range(self.SIZE**2)]

        if all(non_empty):
            return True
        return False
    
    def reset(self): 
        self.turn = self.X
        self.board = [self.EMPTY for i in range(self.SIZE**2)]

        self.print_board()
      

    def is_row_over(self):
        for i in range(0, (self.SIZE**2), self.SIZE):
            same = [self.board[j] == self.board[j+1] for j in range(i, (i + self.SIZE -1))]
            
            if all(same) and not self.board[i] == self.EMPTY:
                return True
        return False

    def is_col_over(self):
        for i in range(self.SIZE):
            same = [self.board[j] == self.board[j+self.SIZE] for j in range(i, (self.SIZE**2 - self.SIZE), self.SIZE)]

            if all(same) and not self.board[i] == self.EMPTY:
                return True

        return False

    def is_diag_over(self):
        increment = self.SIZE - 1
        same = [self.board[i] == self.board[i+increment] for i in range(increment, (self.SIZE**2 - 2*increment), increment)]

        if all(same) and not self.board[increment] == self.EMPTY:
            return True

        increment = self.SIZE + 1
        same = [self.board[i] == self.board[i+increment] for i in range(0, (self.SIZE**2 - increment), increment)]

        if all(same) and not self.board[increment] == self.EMPTY:
            return True

        return False

    def print_board(self):
        for i in range(self.SIZE**2):
            if i % self.SIZE == 0 and not i == 0:
                print()
                print(''.join(['-' for i in range(self.SIZE*2 - 1)]))
            if not i % self.SIZE == 0:
                print('|', end='')
            print(self.board[i], end='')
        print()

