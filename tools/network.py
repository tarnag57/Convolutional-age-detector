import numpy as np
import math

def sigmoid(x):
	return 1/(1+math.exp(-x))


# Define a max pooling layer
class Pool_layer(object):

	# prev_sizes: W0*H0*D0
	# pool_size: WP*HP*DP
	# output: W0/WP*H0/HP*D0/DP
	def __init__(self, prev_sizes, pool_sizes):
		self.prev_sizes = prev_sizes
		self.pool_sizes = pool_sizes

	def feedforward(self, input):
		# pads with 0
		padded_input = np.pad(input, (self.pool_sizes[0] - (self.prev_sizes[0] % self.pool_sizes[0]), 
			self.pool_sizes[1] - (self.prev_sizes[1] % self.pool_sizes[1]), 
			self.pool_sizes[2] - (self.prev_sizes[2] % self.pool_sizes[2])), 
			'constant')
		


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

		padded_input = np.pad(input, (self.filter_sizes[0] - 1, self.filter_sizes[1] - 1), 'constant')
		np.ndarray()
		for w in range(0, self.prev_sizes[0]):
			for h in range(0, self.prev_sizes[1]):
				for d in range(0, self.filter_sizes[3]):
					self.one_cell((w, h, d), padded_input)
	
	def one_cell(self, pos, input):
		(w, h, d) = pos
		val = 0
		for i in range(0, self.filter_sizes[0]):
			for j in range(0, self.filter_sizes[1]):
				for k in range(0, self.filter_sizes[2]):
					val += self.filters[d][i][j][k] * input[k][i + w][j + h]
		return sigmoid(val + self.biases[d])


class Network(object):

	def __init__(self, sizes):
		pass


	def feedforward(self, img):
		pass

	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data):
		pass