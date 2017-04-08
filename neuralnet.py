import numpy as np
import json

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
        self.cost = mse
        self.cost_derivative = mse_derivative

        #debug


    def feed_forward(self, X):
        y_hat = X

        for bias, weight in zip(self.biases, self.weights):
            z = np.dot(weight, y_hat)
            y_hat = self.activation(z + bias)

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
                acts.append(input)
                input = self.activation(z + bias)

        
            # Error in output layer
            delta_L = np.multiply(self.cost_derivative(input, y), self.activation_derivative(zs[-1]))

            print("error: " + str(np.linalg.norm(self.cost(input, y))))
            #print("errrs: " + str(np.linalg.norm(delta_L)))
            
            # Backprop to get error in previous layers
            for l in range(len(self.layers)-3, -1, -1):
                w_L = np.transpose(self.weights[l+1])
                next_layer = w_L * delta_L

                #print("next layer" + str(next_layer))
                
                delta_l = np.multiply(next_layer, self.activation_derivative(zs[l]))

                #print("dleta_l" + str(delta_l))
                ds.append(delta_l)

            ds.append(delta_L)

            # Updates weights
            #for w, d, a in zip(self.weights, ds, acts):
            #    print("weight: " + str(w))
            #    print("deltas: " + str(d))
            #    print("actives " + str(a))
            #    print("d * a : " + str(w - np.multiply(d, np.matrix(a).T)))
                
            self.weights = [w - learning_rate/len(training_data) * d * a for w, d, a in zip(self.weights, ds, acts)]
            self.biases = [b - learning_rate/len(training_data) * d for b, d in zip(self.biases, ds)]

            

            #debug

   
    def export(self):
        network = {}
        network["nr_inputs"] = self.layers[0]
        network["nr_outputs"] = self.layers[-1]
        network["nr_layers"] = len(self.layers)

        layers = []

        for l in range(len(self.layers) - 1):
            layer = {}
            layer["nr_nodes"] = self.layers[l+1]
            layer["activation_function"] = { "type": "sigmoid" }
            layer["input_weights"] = self.weights[l].tolist()
            layer["input_biases"] = self.biases[l].tolist()

            layers.append(layer)

        network["layers"] = layers 

        return json.dumps(network)
        

def sigmoid(x):
    return 1/(1+np.exp(-x)) 

def sigmoid_derivative(x):
    return (sigmoid(x) * (1 - sigmoid(x)))

def tanh(x):
    return (np.tanh(x) + 1)/2

def tanh_derivative(x):
    return (1 - np.square(tanh(x)))

def mse(actual, expected):
    return 0.5 * np.square(actual - expected)

def mse_derivative(actual, expected):
    return (actual - expected)
