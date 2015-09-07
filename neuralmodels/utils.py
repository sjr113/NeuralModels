import theano
import numpy as np
import cPickle
from theano import tensor as T 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import math
import pdb
import sys 

def zero0s(shape):
	return theano.shared(value=np.zeros(shape,dtype=theano.config.floatX))

def permute(samples):
	x = np.random.permutation(samples)
	for i in range(5):
		x = x[np.random.permutation(samples)]
	return x

def readCSVasFloat(filename):
	returnArray = []
	lines = open(filename).readlines()
	for line in lines:
		line = line.strip().split(',')
		if len(line) > 0:
			returnArray.append(np.array([np.float32(x) for x in line]))
	return np.array(returnArray)
