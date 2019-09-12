'''

r0=100    
a=3.9083e-3
b=-5.775e-7
c=-4.183e-12
def rtd(T):
	Rt = r0 * (1 + a*T + b*T**2 + c*(T-100) * T**3)
	return Rt

import numpy as np

scan = [1,2,3,4,5]

def prod_arr(scan):
	new_list = [None for s in scan]
	for i,item in enumerate(scan):
		prod = 1 
		for arr in scan:
			if arr != item:
				prod = arr * prod
		new_list[i] = prod
	return new_list
'''
#car(cons(3,4)) -> 3
#cdr(cons(3,4)) -> 4
'''
def cons(a,b):
	def pair(f):
		return f(a,b)
	return pair

def cdr(f):
	def right(a,b):
		return b
	return f(right)

k = (cdr(cons(3,4)))
	
print(k)
'''
r0=100    
a=3.9083e-3
b=-5.775e-7
c=-4.183e-12
def rtd(T):
	Rt = r0 * (1 + a*T + b*T**2 + c*(T-100) * T**3)
	return Rt