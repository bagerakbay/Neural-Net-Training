#!/usr/bin/python3
#Simple neural network code 
# based on https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1
# Removed matrix codes to make it more readable
# thanks to aib

from math import e

def normalize (x):
	return (1 / ( 1 + pow(e, -1*x)))

def denormalize (x):
	return (x * (1-x))
	
def iterateOne(inputs, output, _weights) :

	result = 0
	
	for i in range(len(inputs)):
		result = result + inputs[i] * _weights[i]
	result = normalize(result)
	
	error = result - output
	#print ("error :",error)
	
	for i in range(len(inputs)):
		_weights[i] = _weights[i] - ( error * inputs[i] * denormalize(result))
			
	#print ("weights :", _weights)
	return _weights
	

	
def iterateAll(inputList, outputList, _weights):
	for i in range(len(inputList)):
		iterateOne (inputList[i], outputList[i], _weights)
	
	return _weights	

def testNN(inputs, _weights):
	result = 0
	for i in range(len(inputs)):
		result = result + inputs[i] * _weights[i]
	result = normalize(result)
	print ("result:", result)
	

def main():

	inputList = [[0,0,1],[1,1,1],[1,0,1],[0,1,1]]
	outputList = [0,1,1,0] 
	weights =[1,1,1]
	test_inputs = [1,0,0]
	iteration = 50

	print ("weights :", weights)
	for i in range(iteration):
		print (i, ".deneme")
		weights = iterateAll(inputList, outputList, weights)
		testNN(test_inputs, weights)
	print ("weights:", weights)
	#iterateOne (inputList[2], outputList[2])


main()			
	