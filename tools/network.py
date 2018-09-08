import numpy as np


# Define a convolutional layer
class Conv_layer(object):

	def __init__(self, prev_sizes, after_sizes, filter_size):
		self.prev_sizes = prev_sizes
		self.after_sizes = after_sizes
		self.filters = [np.random.randn(filter_size[0], filter_size[1], filter_size[2])
								for y in after_sizes[0][1]]

	def feedforward(input):



class Network(object):

	def __init__(self, sizes):
		pass


	def feedforward(self, img):
		pass

	def SGD(self, training_data, epochs, mini_batch_size, eta, test_data):
		pass