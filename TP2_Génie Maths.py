"""
TP 2 - Génie Maths
Méthode Du Point Fixe
VEYRAT-PARISIEN Mathis
TERRE Dael
29/03/2021
"""
import os
from math import*

def PointFixe(g, x0, epsilon, Nitermax):
	'''Algorithme du théorème du point fixe'''
	xold = x0
	xnew = g(xold)
	erreur = xnew - xold
	xold = xnew
	n = 1
	while abs(erreur) > epsilon and n < Nitermax:
		xnew = g(xold)
		erreur = xnew - xold
		xold = xnew
		n = n + 1
	return xnew, n


def g1_1(x):
	return (9-3*x)**(1/4) #Première solution

def g1_2(x):
	return -(9-3*x)**(1/4) #Deuxième solution

def g2_1(x):
	return acos((x+2)/3) #Donne une solution

def g2_2(x):
	return -acos((x+2)/3) #Donne une solution

def g3(x):
	return log(7) - log(x)	#Donne la solution 

def g4_1(x):
	return exp(x) - 10 #Donne une solution

def g4_2(x):
	return log(x + 10) #Donne une solution

def g5(x):
	return atan((x+5)/2) #Donne une solution

def g6(x):
	return log(x**2 + 3) #Donne une solution

def g7(x):
	return (7 - 4*log(x))/3 #Donne la solution

def g8_1(x):
	return (2*x**2-4*x+17)**(1/4) #Donne une solution

def g8_2(x):
	return -(2*x**2-4*x+17)**(1/4) #Donne une solution

def g9(x):
	return log(7 + 2*sin(x)) #Donne la solution

def g10(x):
	return log(10)-log(log(x**2+4)) #Donne la solution

print("(solution, nombres d'itérations)")
print("La solution pour le premier zéro de la première équation est :   ", PointFixe(g1_1, 3/2 ,1e-3, 5e4))
print("La solution pour le deuxième zéro de la première équation est :  ", PointFixe(g1_2, -2 ,1e-3, 5e4),"\n")
print("La solution pour le premier zéro de la deuxième équation est :   ", PointFixe(g2_1, 1/2 ,1e-3, 5e4))
print("La solution pour le deuxième zéro de la deuxième équation est :  ", PointFixe(g2_2, -1/2 ,1e-3, 5e4),"\n")
print("La solution pour la troisième équation est :                     ", PointFixe(g3, 3/2 ,1e-3, 5e4),"\n")
print("La solution pour le premier zéro de la quatrième équation est :  ", PointFixe(g4_1, 0 ,1e-3, 5e4))
print("La solution pour le deuxième zéro de la quatrième équation est : ", PointFixe(g4_2, 0 ,1e-3, 5e4),"\n")
print("La solution pour la cinquième équation est :                     ", PointFixe(g5, 3/2 ,1e-3, 5e4),"\n")
print("La solution pour la sixième équation est :                       ", PointFixe(g6, 1.8 ,1e-3, 5e4),"\n")
print("La solution pour la septième équation est :                      ", PointFixe(g7, 1.6 ,1e-3, 5e4),"\n")
print("La solution pour le premier zéro de la huitième équation est :   ", PointFixe(g8_1, 2 ,1e-3, 5e4))
print("La solution pour le deuxième zéro de la huitième équation est :  ", PointFixe(g8_2, -5/2 ,1e-3, 5e4),"\n")
print("La solution pour la neuvième équation est :                      ", PointFixe(g9, 5/2 ,1e-3, 5e4),"\n")
print("La solution pour la dixième équation est :                       ", PointFixe(g10, 3/2 ,1e-3, 5e4),"\n")

os.system("pause")
