"""
TP 3 - Génie Maths
Méthode De Newton
VEYRAT-PARISIEN Mathis
TERRE Dael
10/04/2021
"""
import os
from math import*

def Newton(f, fder,  x0, epsilon, Nitermax):
	'''Algorithme de la méthode de Newton'''
	xold = x0
	xnew = xold - f(xold)/fder(xold)
	erreur = xnew - xold
	xold = xnew
	n = 1
	while abs(erreur) > epsilon and n < Nitermax:
		xnew = xold - f(xold)/fder(xold)
		erreur = xnew - xold
		xold = xnew
		n = n + 1
	return xnew, n

def f1(x):
	return x**4 + 3*x - 9

def fder1(x):
	return 4*x**3 + 3

def f2(x):
	return  3*cos(x) - 2 - x

def fder2(x):
	return -3*sin(x) - 1

def f3(x):
	return  x*exp(x) - 7

def fder3(x):
	return x*exp(x) + exp(x)

def f4(x):
	return exp(x) - x - 10

def fder4(x):
	return exp(x) - 1

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

def f8(x):
	return x**4 - 2*x**2 + 4*x - 17

def fder8(x):
	return 4*x**3 - 4*x + 4

def f9(x):
	return exp(x) - 2*sin(x) - 7

def fder9(x):
	return exp(x) - 2*cos(x)

def f10(x):
	return log(x**2 + 4)*exp(x) - 10

def fder10(x):
	return (2*x)/(x**2 + 4)*exp(x) + log(x**2 + 4)*exp(x)

print("(solution, nombres d'itérations)")
print("La solution pour le premier zéro de la première équation est :   ", Newton(f1, fder1,   3/2, 1e-6, 5e4))
print("La solution pour le deuxième zéro de la première équation est :  ", Newton(f1, fder1,  -2,   1e-6, 5e4),"\n")
print("La solution pour le premier zéro de la deuxième équation est :   ", Newton(f2, fder2,   1/2, 1e-6, 5e4))
print("La solution pour le deuxième zéro de la deuxième équation est :  ", Newton(f2, fder2,  -1,   1e-6, 5e4))
print("La solution pour le troisième zéro de la deuxième équation est : ", Newton(f2, fder2,  -1/2, 1e-6, 5e4),"\n")
print("La solution pour la troisième équation est :                     ", Newton(f3, fder3,   3/2 ,1e-6, 5e4),"\n")
print("La solution pour le premier zéro de la quatrième équation est :  ", Newton(f4, fder4,  -8 ,  1e-6, 5e4))
print("La solution pour le deuxième zéro de la quatrième équation est : ", Newton(f4, fder4,   2 ,  1e-6, 5e4),"\n")
print("La solution pour la cinquième équation est :                     ", Newton(f5, fder5,   3/2 ,1e-6, 5e4),"\n")
print("La solution pour la sixième équation est :                       ", Newton(f6, fder6,   1.8 ,1e-6, 5e4),"\n")
print("La solution pour la septième équation est :                      ", Newton(f7, fder7,   1.6 ,1e-6, 5e4),"\n")
print("La solution pour le premier zéro de la huitième équation est :   ", Newton(f8, fder8,   2 ,  1e-6, 5e4))
print("La solution pour le deuxième zéro de la huitième équation est :  ", Newton(f8, fder8,  -5/2 ,1e-6, 5e4),"\n")
print("La solution pour la neuvième équation est :                      ", Newton(f9, fder9,   5/2 ,1e-6, 5e4),"\n")
print("La solution pour la dixième équation est :                       ", Newton(f10, fder10, 3/2 ,1e-6, 5e4),"\n")

os.system("pause")