var NeuralNet = function(layers) {

	this.num_layers = layers.length;

	this.layers = layers;

	this.biases = [];

	this.weights = [];

	this.feedforward = function(a) {
		var values = zip(this.biases, this.weights);

		for (var i = 0; i < values.length; i++) {
			var bias = values[0];
			var weight = values[1];

			a = sigmoid(dot_product(weight, a) + bias);
		}
		return a;
	}
};

function sigmoid(x) {
	return 1/(1 + Math.exp(-x));
}

function dot_product(value, array) {
	for (var i = 0; i < array.length; i++) {
		array[i] *= values;
	}
	return array;
}

function zip(a, b) {
	return a.map(function(e, i) {
		return [a[i], b[i]];
	});
}
