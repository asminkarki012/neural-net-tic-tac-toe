import numpy as np

class Neural_Net(object):

    def __init__(self, layers):

        self.layers = layers

        # Set random weights initially
        self.biases = [np.random.randn(x, 1) for x in layers[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(layers[1:], layers[:-1])]

    def feed_forward(self, X):
        y_hat = X

        for bias, weight in zip(self.biases, self.weights):
            y_hat = sigmoid(1, np.dot(weight, y_hat))

        return y_hat
       

def sigmoid(alpha, x):
    return 1/(1+np.exp(-(alpha *x)))

def sigmoid_deriv(alpha, x):
    return sigmoid(alpha, x) * (1 - sigmoid(alpha, x))
