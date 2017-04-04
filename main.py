from tictactoe import *
from neuralnet import *
running = True
#game = Tictactoe()

net = Neural_Net([9,9,9])

training_data = [([1,0,0,0,0,0,0,0,0], [0,0,0,0,1,0,0,0,0])]

print("Before training: ")

output = net.feed_forward([1,0,0,0,0,0,0,0,0])
print(output)

for i in range(1000):
    net.backpropagation(training_data, 0.3)

output = net.feed_forward([0 for x in range(9)])
print("After training: ")
print(output)
