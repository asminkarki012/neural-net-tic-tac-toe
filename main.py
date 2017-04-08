#!/usr/bin/python3

from tictactoe import *
from neuralnet import *
from parser import *

running = True
#game = Tictactoe()

net = Neural_Net([3,3,3,3,3])
input = [0.137289, 0.172, 0.75]
training_data = [(input, [0.9912, 0.481, 0.101])]


output_before = net.feed_forward(input)

# Training
#net.train(training_data, 0.2, 1000)

print("After training: ")
output = net.feed_forward(input)
print(net.weights)
print(output)

print(net.weights)

with open("testnet.json", "w") as f:
    f.write(net.export_network())
    f.close()    
