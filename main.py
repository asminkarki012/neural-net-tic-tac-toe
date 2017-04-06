#!/usr/bin/python3

from tictactoe import *
from neuralnet import *
running = True
#game = Tictactoe()

net = Neural_Net([3,3,3,3,3])
input = [0.137289, 0.172, 0.75]
training_data = [(input, [0.9912, 0.481, 0.101])]


output_before = net.feed_forward(input)

for i in range(10000):
    net.backpropagation(training_data, 0.5)


print("Before training: ")
print(output_before)

print("After training: ")
output = net.feed_forward(input)
print(net.weights)
print(output)
