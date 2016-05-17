# Program w/ func that computes the fibonacci number of the parameter.

def fibonacci(x):
	a,b = 1,1
	for i in range(x-1):
		a,b = b,a+b
	return a
