import numpy as np
import json

class Neural_Net(object):
    
    def __init__(self, layers):
        self.layers = layers
   
        # Set random weights initially
        self.biases = [np.zeros([x, 1]) for x in layers[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(layers[1:], layers[:-1])]

        # Activation functions
        self.activation = sigmoid
        self.activation_derivative = sigmoid_derivative
        

        # Cost functions
        self.cost = mse
        self.cost_derivative = mse_derivative

        #debug


    def feed_forward(self, X):
        y_hat = np.reshape(X, [len(X),-1])
        
        for bias, weight in zip(self.biases, self.weights):
            z = np.dot(weight, y_hat) + bias
            y_hat = self.activation(z)

            # Debug
            #print("z shape = " + z.shape)
            #print("yhat shape = " = y_hat.shape)

        # Tranpose on return for readability
        return y_hat.T

    
    def forward_backward_prop(self, x, y, learning_rate):
        zs = [] # Weighted input vector of every layer 
        acts = [] # Output vector of every layer
        ds = [] # Error vector of every layer

        # Reshape x and  y to be of the form [n, 1]
        input = np.reshape(x, [len(x),-1])
        y = np.reshape(y, [len(y),-1])
        #print("input shape =", input.shape)

        # Feed forward to get weighted input vector and output vector
        for bias, weight in zip(self.biases, self.weights):
            acts.append(input)

            z = np.dot(weight, input) + bias
            zs.append(z)
            input = self.activation(z)

            # Debug
            #print("z shape =", z.shape)
            #print("bias shape =", bias.shape)
            #print("input shape = ", input.shape)

        #print("acts.shape =", [i.shape for i in acts])
        #print("cost derivative shape =", self.cost_derivative(input, y).shape)

        # Error in output layer
        delta_L = np.multiply(self.cost_derivative(input, y), self.activation_derivative(zs[-1]))

        ds.append(delta_L)

        #print("error: " + str(np.linalg.norm(self.cost(input, y))))
        #print("errrs: " + str(np.linalg.norm(delta_L)))

        # Backprop to get error in previous layers
        for l in range(len(self.layers)-3, -1, -1):
            w_L = np.transpose(self.weights[l+1]) 
            next_layer = np.dot(w_L, delta_L)

            delta_L = np.multiply(next_layer, self.activation_derivative(zs[l]))

            # Prepend error of the layer
            ds = [delta_L] + ds

        #print("ds.shape =", [i.shape for i in ds])

        # Updates weights and biases
        self.weights = [w - learning_rate * np.dot(d, np.array(a).T) for w, d, a in zip(self.weights, ds, acts)]

        self.biases = [b - learning_rate * d for b, d in zip(self.biases, ds)]

        # Debug
        #print("weight after update shape =", [w.shape for w in self.weights])
        #print("bias after update shape =", [b.shape for b in self.biases])


    def train(self, training_data, learning_rate, epochs):
        for i in range(epochs):
            for (x, y) in training_data:
                self.forward_backward_prop(x, y, learning_rate)

            if i % 100 == 0:
                output = self.feed_forward(x)
                print("Epoch " + str(i) + " - Error: " + str(np.linalg.norm(self.cost(output, y))))

            
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
    return (sigmoid(x) * (1 - sigmoid(x)))

def tanh(x):
    return (np.tanh(x) + 1)/2

def tanh_derivative(x):
    return (1 - np.square(tanh(x)))

def mse(actual, expected):
    return 0.5 * np.square(actual - expected)

def mse_derivative(actual, expected):
    return (actual - expected)
