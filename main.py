#!/usr/bin/python3

from tictactoe import *
from neuralnet import *
running = True
#game = Tictactoe()

net = Neural_Net([9,9,9])

training_data = [([1,0,0,0,0,0,0,0,0], [1,1,0,0,0,0,0,0,0])]

print("Before training: ")

output = net.feed_forward([1,0,0,0,0,0,0,0,0])
print(output)

#for i in range(10):
net.backpropagation(training_data, 0.3)


print("After training: ")
output = net.feed_forward([1,0,0,0,0,0,0,0,0])
print(net.weights)
print(output)
