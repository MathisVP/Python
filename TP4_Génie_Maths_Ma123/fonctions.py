"""
TP 4 - Génie Maths
Fonctions
VEYRAT-PARISIEN Mathis
"""

from math import*

def f5(x):
	return 2*tan(x) - x - 5

def f6(x):
	return exp(x) - x**2 - 3

def f7(x):
	return 3*x + 4*log(x) - 7


#########################################################
def g5(x):
	return atan((x+5)/2)

def g6(x):
	return log(x**2 + 3)

def g7(x):
	return (7 - 4*log(x))/3
#########################################################
def f5(x):
	return 2*tan(x) - x - 5

def fder5(x):
	return 2/(cos(x)**2) - 1

def f6(x):
	return exp(x) - x**2 - 3

def fder6(x):
	return exp(x) - 2*x

def f7(x):
	return 3*x + 4*log(x) - 7

def fder7(x):
	return 3 + 4/x
###########################################################

def f(x):
	return 1 + sin(x) - 2*x

def g(x):
	return (1 + sin(x))/2

def fder(x):
	return cos(x) - 2
