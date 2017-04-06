import numpy as np
import json

class Neural_Net(object):

    def __init__(self, layers):
        self.layers = layers

        # Set random weights initially
        self.biases = [np.random.randn(x, 1) for x in layers[1:]]
        self.weights = [np.zeros(shape=(x, y)) for x, y in zip(layers[1:], layers[:-1])]

        # Activation functions
        self.activation = sigmoid 
        self.activation_derivative = sigmoid_derivative

        # Cost functions
        self.cost = mse
        self.cost_derivative = mse_derivative

        #debug
        print("Input weights:")
        print(self.weights)


    def feed_forward(self, X):
        y_hat = X

        for bias, weight in zip(self.biases, self.weights):
            z = np.dot(weight, y_hat)
            y_hat = self.activation(z)

        return y_hat

    def backpropagation(self, training_data, learning_rate):
        
        for (x, y) in training_data:
            zs = [] # Weighted input vector of every layer 
            acts = [] # Output vector of every layer
            ds = [] # Error vector of every layer

            # Feed forward to get weighted input vector and output vector
            input = x
            for bias, weight in zip(self.biases, self.weights):
                z = np.dot(weight, input) 
                zs.append(z)

                input = self.activation(z)

                acts.append(input)
                
                
        
            # Error in output layer
            delta_L = np.multiply(self.cost_derivative(acts[-1], y), self.activation_derivative(zs[-1]))
            
            # Backprop to get error in previous layers
            for l in range(len(self.layers)-3, -1, -1):
                w_L = np.transpose(self.weights[l+1])
                next_layer = w_L * delta_L
                
                delta_l = np.multiply(next_layer, self.activation_derivative(zs[l]))
                ds.append(delta_l)

            ds.append(delta_L)

            # Updates weights
            self.weights = [w - learning_rate/len(training_data) * d * a for w, d, a in zip(self.weights, ds, acts)]
            self.biases = [b - learning_rate/len(training_data) * d for b, d in zip(self.biases, ds)]

            #debug

    def import_network(self, json_network):
        data = json.loads(json_network)
        layers = data["nr_inputs"]

        layers.extend([nodes for nodes in data["layers"]])



    def export_network(self):
        network = {}
        network["nr_inputs"] = self.layers[0]
        network["nr_ouputs"] = self.layers[-1]
        network["nr_layers"] = len(self.layers)

        layers = [] 

        return json.dumps(network)
        

def sigmoid(x):
    return 1/(1+np.exp(-x)) 

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def tanh(x):
    return (np.tanh(x) + 1)/2

def tanh_derivative(x):
    return (1 - np.square(tanh(x)))

def mse(actual, expected):
    return 0.5 * np.square(actual - expected)

def mse_derivative(actual, expected):
    return (actual - expected)
