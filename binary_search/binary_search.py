import sys
import numpy as np
import matplotlib.pyplot as plt

sys.stdout = open('sqrt.txt', 'w')

def f(x):
	return (1.0*x*x);


def square_root(n):
	low, high = 0.0, 1.0*n
	mid = (high+low)/2
	fval = f(mid)-n
	errors = []

	while(abs(fval) > 1e-4):
		mid = (high+low)/2
		fval = f(mid) - n
		errors.append(fval);
		print("f({}) = {}".format(mid, fval))
		if(fval < 0):
			low = mid
		else:
			high = mid 
	
	return errors, mid


n = 2 
errors, res = square_root(n)
x = np.arange(0, len(errors), 1)

print("sqrt({}) = {} (computed)".format(n,res))
print("sqrt({}) = {} (actual)".format(n,np.sqrt(n)))

plt.plot(x,errors)
plt.grid(True)
plt.ylabel("error")
plt.xlabel("iteration")
plt.show()
