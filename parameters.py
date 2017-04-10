import parser
import random
from neuralnet import *
from tictactoe import *


def get_movelist(list):
    list = list[0].tolist()
    return [ordered[0] for ordered in sorted(enumerate(list), key=lambda i:i[1], reverse=True)]

def get_move(game, ordered_moves):
    for move in ordered_moves:
        if game.is_valid_move(move):
            return move

def get_random_move():
    return random.randint(0, 8)

def train_ai(neuralnet, winning_moves, training_rate, epochs):
    training_data = parser.to_training_data(winning_moves)

    neuralnet.train(training_data, training_rate, epochs)


def play_and_train(game, layers, games):
    neuralnet = Neural_Net(layers)
    ai_wins = 0
    player_wins = 0
    draws = 0
    for k in range(games):
        game.reset()
        player = random.randint(0, 1)

        if (player == 0):
            player = game.X
            ai = game.O
        else:
            player = game.O
            ai = game.X
        
        while not (game.is_gameover() or game.is_board_full()):

            if (game.turn == player):

                #Player turn
                move = get_random_move()
                while not game.is_valid_move(move):
                    move = get_random_move()

                # net_output = neuralnet.feed_forward(game.export_board())

                # movelist = get_movelist(net_output)
                # move = get_move(game, movelist)

                game.make_move(move)

            else:
                #AI turn
                net_output = neuralnet.feed_forward(game.export_board())

                movelist = get_movelist(net_output)
                ai_move = get_move(game, movelist)

                game.make_move(ai_move)
            

        if (game.winner == player):
            player_wins += 1
        elif (game.winner == ai):
            ai_wins += 1
        else:
            draws += 1

        if game.is_gameover():
            train_ai(neuralnet, game.export_winning_moves(), 0.1, 8)

        ai_winrate = (ai_wins+draws) / (ai_wins + player_wins + draws)
        # print("Player wins: %d, AI wins: %d, Draws: %d - AI win rateL %lf" % (player_wins, ai_wins, draws, ai_winrate), end="\r")

    return ai_winrate

def main():

    input_layers = 9
    output_layers = 9
    game = Tictactoe()

    layers = (input_layers, 0, output_layers)

    print("Test parameters: " + str(layers))

    winrate = 0
    for j in range(100):               
        winrate += play_and_train(game, layers, 10000)
        print("winrate: " + str(winrate/(j+1)))
    # print()
    print(str(layers) + " : " + str(winrate/100))

if __name__ == "__main__":
    main()
