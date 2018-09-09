import numpy as np


# Define a convolutional layer
class Conv_layer(object):

	# prev_sizes: W0*H0*D0
	# filter_sizes: WF*HF*D0*DF
	# biases: 1*1*1*DF => represented as 1D array
	# output: W0*H0*DF
	def __init__(self, prev_sizes, filter_size):
		self.prev_sizes = prev_sizes
		self.filter_sizes = filter_size

		# Check input params
		if filter_size[2] != prev_sizes[2]:
			raise Exception('The filters should have the same depths as the input. Filter depth: ' 
				+ filter_size[2] + ', input depth: ' + prev_sizes[2] )

		self.filters = [np.random.randn(filter_size[0], filter_size[1], filter_size[2])
								for y in filter_size[3]]
		self.biases = [np.random.randn(1) for y in filter_size[3]]

	def feedforward(self, input):
		if input.shape != (self.prev_sizes[0], self.prev_sizes[1], self.prev_sizes[2]):
			raise Exception('The input matrix has different sizes than expected. Input shape: ' + input.shape)

		return  


class Network(object):

	def __init__(self, sizes):
		pass


	def feedforward(self, img):
		pass

	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data):
		pass