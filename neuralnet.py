import numpy as np

class Neural_Net(object):

    def __init__(self, layers):

        self.layers = layers

        # Set random weights initially
        self.biases = [np.random.randn(x, 1) for x in layers[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(layers[1:], layers[:-1])]

        # Activation functions
        self.activation = sigmoid
        self.activation_derivative = sigmoid_derivative

        # Cost functions
        self.cost_derivative = mse_derivative


    def feed_forward(self, X):
        y_hat = X

        for bias, weight in zip(self.biases, self.weights):
            y_hat = sigmoid(1, np.dot(weight, y_hat))

        return y_hat
      
    #def gradient_descent(self, training_data, learning_rate):
        #for (x, y) in training_data:

    def backpropagation(self, training_data):
        
        for (x, y) in training_data:
            zs = [] # Weighted input vector of every layer 
            acts = [] # Output vector of every layer
            ds = [] # Error vector of every layer

            # Feed forward to get weighted input vector and output vector
            input = x
            for bias, weight in zip(self.biases, self.weights):
                z = np.dot(weight, input)
                zs.append(z)
                
                input = self.activation(np.dot(weight, input))
                acts.append(input)
            
            # Error in output layer
            delta_L = np.multiply(self.cost_derivative(acts[-1], y), self.activation_derivative(zs[-1]))

            # Backprop to get error in previous layers
            for l in range(len(self.layers)-1, 0, -1):
                w_L = np.transpose(self.weights[l+1])
                prev_layer = w_L * delta_L

                delta_l = np.multiply(prev_layer, self.activation_derivative(zs[l]))
                ds.append(delta_l)

            # Updates weights
            self.weights = [w - training_rate/len(training_data) * d * a for w, d, a in zip(self.weights, ds, acts)]



def sigmoid(alpha, x):
    return 1/(1+np.exp(-(alpha *x))) 

def sigmoid_deriv(alpha, x):
    return sigmoid(alpha, x) * (1 - sigmoid(alpha, x))

def mse_derivative(actual, expected):
    return (actual - expected)
