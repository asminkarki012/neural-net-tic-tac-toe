# %load main.py
#!/usr/bin/python3

from tictactoe import *
from neuralnet import *
from parser import *

running = True
#game = Tictactoe()

net = Neural_Net([9, 3, 9]) 
input = [0.137289, 0.172, 0.75, 0.3, 0.999, 0.4123, 0.77773, 0.324, 0.6543]
training_data = [(input, [0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])]

print("Before training: ")
output_before = net.feed_forward(input)
print(output_before)

# Training
net.train(training_data, 0.2, 1000)

print("After training: ")
output = net.feed_forward(input)
print(output)

