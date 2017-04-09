import parser
from tictactoe import *


def get_movelist(list):
    list = list[0].tolist()
    return [ordered[0] for ordered in sorted(enumerate(list), key=lambda i:i[1], reverse=True)]

def get_move(game, ordered_moves):
    for move in ordered_moves:
        if game.is_valid_move(move):
            return move

def main():

    network_file = open("net.json", "r")
    neuralnet = parser.import_network(network_file.read())
    
    game = Tictactoe()
    print(game.is_valid_move(1))
    
    running = True
    while not game.is_gameover():

        # Player turn
        move = int(input())
        while not game.is_valid_move(move):
            print("Invalid move")
            move = int(input())

        game.make_move(move)

        #AI turn
        net_output = neuralnet.feed_forward(game.export_board())
        print("ai output: " + str(net_output))
        movelist = get_movelist(net_output)
        ai_move = get_move(game, movelist)
        print("AI move: " + str(ai_move))
        game.make_move(ai_move)
        
    print(game.board)

    print(game.is_gameover())


if __name__ == "__main__":
    main()

