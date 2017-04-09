import json
from neuralnet import *

def import_training_data(json_data):
    training_data = []
    
    datas = json.loads(json_data)
    for data in datas:
        x = map(int, data["input"].split(","))
        y = map(int, data["output"].split(","))

        training_data.append((x, y))

    return training_data


def import_network(json_network):
    network_data = json.loads(json_network)

    layers = [layer["nr_nodes"] for layer in network_data["layers"]]
    layers = [network_data["nr_inputs"]] + layers

    nn = Neural_Net(layers)

    weights = [layer["input_weights"] for layer in network_data["layers"]]
    nn.weights = weights

    print(weights)


    
