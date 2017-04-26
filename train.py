import sys
import getopt
import parser
from neuralnet import *

def main(argv):
    # Default training data and output file
    inputfile = "training_data.csv"
    outputfile = "net.json"

    try:
        opts, args = getopt.getopt(argv, "i:o:", []])
    except getopt.GetoptError:
        print("Wrong usage, please check README.md")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            inputfile = arg
        elif opt == "-o":
            outputfile = arg


    training_file = open(inputfile, "r")
    network_file = open(outputfile, "w")

    # Create the neural net
    nn = Neural_Net([9, 27, 27, 9])
    training_data = parser.import_training_data_csv(inputfile)

    print("Finish import: " + str(len(training_data)))

    learning_rate = 0.2
    epochs = 10000

    # # Train it
    nn.train(training_data, learning_rate, epochs, True)

    # Export trained network as JSON
    nn_json = nn.export()
    network_file.write(nn_json)

    
if __name__ == "__main__":
    main(sys.argv[1:])
