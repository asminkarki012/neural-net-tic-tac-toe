import parser
import random
from tictactoe import *
from neuralnet import *

network_file = "net.json"
moveset_file = "training_data.csv"

def get_movelist(list):
    list = list[0].tolist()
    return [ordered[0] for ordered in sorted(enumerate(list), key=lambda i:i[1], reverse=True)]

def get_move(game, ordered_moves):
    for move in ordered_moves:
        if game.is_valid_move(move):
            return move

def get_random_move(game):
    # Heuristic to try and win if possible
    for i in range(9):
        if game.board[i] == game.EMPTY:
            game.board[i] = game.turn
            if game.is_gameover():
                game.board[i] = game.EMPTY
                return i
            else:
                game.board[i] = game.EMPTY

    return random.randint(0, 8)

def train_ai(neuralnet, winning_moves, training_rate, epochs):
    training_data = parser.to_training_data(winning_moves)

    # f = open(moveset_file, "a")
    # for i, o in training_data:
    #     f.write(str(i) + "," + str(o) + "\n")
    # f.close()

    neuralnet.train(training_data, training_rate, epochs)

def write_net(net):
    trained_net = net.export()
    # f = open(network_file, "w")
    # f.write(trained_net)
    # f.close()

def main():
    # f = open(network_file, "r")
    # neuralnet = parser.import_network(f.read()) 
    
    neuralnet = Neural_Net([9, 27, 27, 9])

    game = Tictactoe()
    ai_wins = 0
    player_wins = 0
    draws = 0
    games = 0
    while True:
        try:
            game.reset()
            player = random.randint(0, 1)

            if (player == 0):
                player = game.X
                ai = game.O
            else:
                player = game.O
                ai = game.X
            
            running = True
            while not (game.is_gameover() or game.is_board_full()):

                if (game.turn == player):

                    #Player turn
                    move = get_random_move(game)
                    while not game.is_valid_move(move):
                        move = get_random_move(game)

                    game.make_move(move)

                else:
                    #AI turn
                    net_output = neuralnet.feed_forward(game.export_board())

                    movelist = get_movelist(net_output)
                    ai_move = get_move(game, movelist)

                    game.make_move(ai_move)
                

            if (game.winner == player):
                player_wins += 1
                losing_moves = game.export_losing_moves(ai)
                train_ai(neuralnet, [losing_moves[-1]], 0.1, 4)

            elif (game.winner == ai):
                ai_wins += 1
                train_ai(neuralnet, game.export_player_moves(ai), 0.1, 4)
            else:
                draws += 1
                train_ai(neuralnet, game.export_player_moves(ai), 0.1, 4)

            ai_winrate = (ai_wins+draws) / (ai_wins + player_wins + draws)
            print("Player wins: %d, AI wins: %d, Draws: %d - AI win rateL %lf" % (player_wins, ai_wins, draws, ai_winrate), end='\r')

            games += 1
            if games % 5000:
                write_net(neuralnet)

        except KeyboardInterrupt:
            write_net(neuralnet)
            raise

if __name__ == "__main__":
    main()

