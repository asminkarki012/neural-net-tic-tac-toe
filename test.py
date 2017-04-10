#!/usr/bin/python3

from neuralnet import *

def test_input(training_data):
    for i, o in training_data:
        a = net.feed_forward(i)
        print("expected: " + str(o))
        print("actual:   " + str(a))

net = Neural_Net([9, 3, 9]) 

#Random inputs
input1 = [0.137289, 0.172, 0.75, 0.3, 0.999, 0.4123, 0.77773, 0.324, 0.6543]
input2 = [-0.51, 0.5, -0.123, 0.3, 1, 0.444, 0.66123, 0.092, 0.843119]

#Expected outputs
output1 = [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
output2 = [0, 0.5, 0, 0.5, 0, 0.5, 0, 0.5, 0]

training_data = [(input1, output1), (input2, output2)]

print("Before training: ")
test_input(training_data)

# Training the network
learning_rate = 0.2
epochs = 1000
net.train(training_data, learning_rate, epochs, True)

print("After training: ")
test_input(training_data)

