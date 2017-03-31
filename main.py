from tictactoe import *

running = True
game = Tictactoe()




while not game.is_gameover():
    game.print_board()

    move = input()

    game.make_move(int(move))

