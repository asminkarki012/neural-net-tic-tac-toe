import numpy as np
import json

class Neural_Net(object):
    
    # init layers with each layers' dimension, i.e. len(layers) = num_layers, layers[i] = [shape of weights]
    def __init__(self, layers):
        self.layers = layers
   
        # Set random weights initially
        self.biases = [np.zeros([x, 1]) for x, _ in layers] 
        self.weights = [np.random.randn(x, y) for x, y in layers]
        
        # Activation functions
        self.activation = sigmoid
        self.activation_derivative = sigmoid_derivative
        

        # Cost functions
        self.cost = mse
        self.cost_derivative = mse_derivative

        #debug


    def feed_forward(self, X):
        y_hat = np.reshape(X, [len(X),-1]) # <-- very important!
        
        for bias, weight in zip(self.biases, self.weights):
            z = np.dot(weight, y_hat)
            print("z shape =", z.shape)
            y_hat = self.activation(z + bias)
            print("yhat shape =", y_hat.shape)
        return y_hat
    
    # changed name to forward_backward_prop for better notation
    def forward_backward_prop(self, training_data, learning_rate):
        
        for (x, y) in training_data:
            zs = [] # Weighted input vector of every layer 
            acts = [] # Output vector of every layer
            ds = [] # Error vector of every layer

            # Feed forward to get weighted input vector and output vector
            # bias shape is [x,1], but z has shape [x,] !
            input = np.reshape(x, [len(x),-1])
            y = np.reshape(y, [len(y),-1])
            # ^ this is important!!!!!!! make sure input shape is in form [x,1], not [x,]

            #print("input shape =", input.shape)
            for bias, weight in zip(self.biases, self.weights):
                acts.append(input)
           
                z = np.dot(weight, input) + bias
                zs.append(z)
                #print("z shape =", z.shape)
                #print("bias shape =", bias.shape)
                input = self.activation(z)
                #print("input shape = ", input.shape)
                
            #print("acts.shape =", [i.shape for i in acts])
            # Error in output layer
            #print("cost derivative shape =", self.cost_derivative(input, y).shape)
            # wrong shape! cost_derivative should give 9*1 shape, not 9*9! The error occurred because label has shape [x,]!
            delta_L = np.multiply(self.cost_derivative(input, y), self.activation_derivative(zs[-1]))
            
            # should append this delta_L first
            ds.append(delta_L)
            
            #print("error: " + str(np.linalg.norm(self.cost(input, y))))
            #print("errrs: " + str(np.linalg.norm(delta_L)))
            
            # Backprop to get error in previous layers
            for l in range(len(self.layers)-2, -1, -1):   #<- changed to -2 to fit new self.layers format
                w_L = np.transpose(self.weights[l+1]) 
                # you did not loop the delta_L here! you used delta_l below!
                next_layer = np.dot(w_L, delta_L) # <- also use np.dot here! they are matrices!

                #print("next layer" + str(next_layer))
                
                delta_L = np.multiply(next_layer, self.activation_derivative(zs[l]))

                #print("dleta_l" + str(delta_l))
                
                # for ds, you appended it backwards! so ds[0] is actually the final layer! hence you got to append it in front.
                #ds.append(delta_L)
                ds = [delta_L] + ds

            #ds.append(delta_L) #<- why append here?
            #print("ds.shape =", [i.shape for i in ds])
            
            # Updates weights
            #for w, d, a in zip(self.weights, ds, acts):
            #    print("weight: " + str(w))
            #    print("deltas: " + str(d))
            #    print("actives " + str(a))
            #    print("d * a : " + str(w - np.multiply(d, np.matrix(a).T)))
            
            # these are matrices! you got to use dot product!!!! still not sure why len(train_data) is used here,
            # remember to transpose a! This part is tricky
            self.weights = [w - learning_rate/len(training_data) * np.dot(d, np.array(a).T) for w, d, a in zip(self.weights, ds, acts)]
            #print("weight after update shape =", [w.shape for w in self.weights])
            
            self.biases = [b - learning_rate/len(training_data) * d for b, d in zip(self.biases, ds)]
            #print("bias after update shape =", [b.shape for b in self.biases])
            

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
    return (sigmoid(x) * (1 - sigmoid(x)))

def tanh(x):
    return (np.tanh(x) + 1)/2

def tanh_derivative(x):
    return (1 - np.square(tanh(x)))

def mse(actual, expected):
    return 0.5 * np.square(actual - expected)

def mse_derivative(actual, expected):
    return (actual - expected)
