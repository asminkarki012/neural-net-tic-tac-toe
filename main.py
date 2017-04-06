# %load main.py
#!/usr/bin/python3

from tictactoe import *
from neuralnet import *
running = True
#game = Tictactoe()

# with 3 layers, with input dimension = 9 and hidden = 4.
net = Neural_Net([[4, 9],[4,4],[9, 4]]) 
input = [0.137289, 0.172, 0.75, 0.3, 0.999, 0.4123, 0.77773, 0.324, 0.6543]
training_data = [(input, [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])]


output_before = net.feed_forward(input)

for i in range(10000):
    net.forward_backward_prop(training_data, 0.5)


print("Before training: ")
print(output_before)

print("After training: ")
output = net.feed_forward(input)
# print(net.weights)
print(output)