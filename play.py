import parser
from tictactoe import *


def main():

    network_file = open("net.json", "r")
    neuralnet = parser.import_network(network_file.read())

    
    game = Tictactoe()

    running = True
    while running:
