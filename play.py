import parser
import random
from tictactoe import *


def get_movelist(list):
    list = list[0].tolist()
    return [ordered[0] for ordered in sorted(enumerate(list), key=lambda i:i[1], reverse=True)]

def get_move(game, ordered_moves):
    for move in ordered_moves:
        if game.is_valid_move(move):
            return move

def main():

    network_file = open("trained_net-9279-4-punish.json", "r")
    neuralnet = parser.import_network(network_file.read())
    
    game = Tictactoe()
    ai_wins = 0
    player_wins = 0
    draws = 0

    player = random.randint(0, 1)

    if (player == 0):
        player = game.X
        ai = game.O
    else:
        player = game.O
        ai = game.X
    
    running = True
    while not (game.is_gameover() or game.is_board_full()):
        game.print_board()

        if (game.turn == player):

            #Player turn
            move = int(input())
            while not game.is_valid_move(move):
                move = int(input())

            game.make_move(move)

        else:
            #AI turn
            net_output = neuralnet.feed_forward(game.export_board())
            print(net_output)
            movelist = get_movelist(net_output)
            ai_move = get_move(game, movelist)

            game.make_move(ai_move)

    game.print_board()




if __name__ == "__main__":
    main()

