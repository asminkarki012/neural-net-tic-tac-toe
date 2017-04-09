import json
import numpy as np
from neuralnet import *

def import_training_data(json_data):
    training_data = []
    
    datas = json.loads(json_data)
    for data in datas:
        x = list(map(int, data["input"].split(",")))
        y = list(map(int, data["output"].split(",")))

        training_data.append((x, y))

    return training_data


def import_network(json_network):
    network_data = json.loads(json_network)

    layers = [layer["nr_nodes"] for layer in network_data["layers"]]
    layers = [network_data["nr_inputs"]] + layers

    nn = Neural_Net(layers)

    weights = [layer["input_weights"] for layer in network_data["layers"]]
    nn.weights = np.array(weights)

    biases = [layer["input_biases"] for layer in network_data["layers"]]
    nn.biases = np.array(biases)

    #TODO
    #activation functions from import

    return nn

    
