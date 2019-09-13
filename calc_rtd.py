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
import numpy as np

r0=100    
a=3.9083e-3
b=-5.775e-7
c=-4.183e-12
def rtd(T):
	Rt = r0 * (1 + a*T + b*T**2 + c*(T-100) * T**3)
	return Rt

def percent_rtd(T):
	first = a*T 
	second = b * T**2
	third = - 100 * c * T**3
	fourth = c * T**4
	Rt = 1 + a*T + b*T**2 + c*(T-100) * T**3
	fir_per = first 
	sec_per = second 
	thi_per = third 
	fou_per = fourth 
	one_per = 1 
	print(Rt)
	return fir_per, sec_per, thi_per, fou_per ,one_per
temp = input('input temp here: ')
Rt = rtd(float(temp))
print('this is Rt: ', Rt)
p = ([c*r0, -100*c*r0, b*r0, a*r0, 1*r0-Rt])
print('this is the temp: ', np.roots(p))

