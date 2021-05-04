"""
TP 4 - Génie Maths
Méthode de Dichotomie / Sécante
VEYRAT-PARISIEN Mathis
"""
import os
from math import*
from fonctions import*

'''
l-dichot-n    =[]
l-dichot-Xn   =[]
l-dichot-En   =[]

l-dichot-n.append()
l-dichot-Xn.append()
l-dichot-En.append()


l-secant-n    =[]
l-secant-Xn   =[]
l-secant-En   =[]

l-secant-n.append()
l-secant-Xn.append()
l-secant-En.append()
'''

def PointFixe(g, x0, epsilon, Nitermax):
	'''Algorithme du théorème du point fixe'''
	xold = x0
	xnew = g(xold)
	erreur = xnew - xold
	xold = xnew
	n = 1
	l_PtFixe_n = [1]
	l_PtFixe_Xn = [x0]
	l_PtFixe_En = [erreur]

	while abs(erreur) > epsilon and n < Nitermax:
		xnew = g(xold)
		erreur = xnew - xold
		xold = xnew
		n = n + 1
		l_PtFixe_n.append(n)
		l_PtFixe_Xn.append(xnew)
		l_PtFixe_En.append(epsilon)
	return xnew, n, l_PtFixe_n, l_PtFixe_Xn, l_PtFixe_En 

def Newton(f, fder,  x0, epsilon, Nitermax):
	'''Algorithme de la méthode de Newton'''
	xold = x0
	xnew = xold - f(xold)/fder(xold)
	erreur = xnew - xold
	xold = xnew
	n = 1
	l_newton_n = [1]
	l_newton_Xn = [x0]
	l_newton_En = [erreur]
	while abs(erreur) > epsilon and n < Nitermax:
		xnew = xold - f(xold)/fder(xold)
		erreur = xnew - xold
		xold = xnew
		n = n + 1
		l_newton_n.append(n)
		l_newton_Xn.append(xnew)
		l_newton_En.append(epsilon)
	return xnew, n, l_newton_n, l_newton_Xn, l_newton_En

def dichotomie(f, a0, b0, epsilon, Nitermax):
	'''Fonction de l'algorithme de la méthode par dichotomie'''
	an = a0
	bn = b0
	n = 1
	l_dichot_n = [1]
	l_dichot_Xn = [a0]
	l_dichot_En = [epsilon]
	while abs(bn - an) > epsilon and n < Nitermax:
		m = (an + bn)/2

		if (f(an)*f(m) <= 0):
			bn = m

		else: 
			an = m
		n += 1
		l_dichot_n.append(n)
		l_dichot_Xn.append(an)
		l_dichot_En.append(epsilon)
	return m, n


def secante(f, x0, x1, epsilon, Nitermax):
	'''Fonction de l'algorithme de la méthode de la sécante'''
	n = 1
	while abs(x1 - x0) > epsilon and n < Nitermax:
		x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
		x0 = x1
		x1 = x2
		n = n + 1
	return x2, n


def main():

	print("Point Fixe")
	print("La solution pour la cinquième équation est : ", PointFixe(g5, 3/2 ,1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", PointFixe(g6, 1.8 ,1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", PointFixe(g7, 1.6 ,1e-6, 5e4),"\n")

	print("Newton")
	print("La solution pour la cinquième équation est : ", Newton(f5, fder5,   3/2 ,1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", Newton(f6, fder6,   1.8 ,1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", Newton(f7, fder7,   1.6 ,1e-6, 5e4),"\n")

	print("Dichotomie")
	print("La solution pour la cinquième équation est : ", dichotomie(f5, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", dichotomie(f6, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", dichotomie(f7, 1, 2, 1e-6, 5e4),"\n")

	print("Sécante")
	print("La solution pour la cinquième équation est : ", secante(f5, 1.2, 2, 1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", secante(f6, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", secante(f7, 1, 2, 1e-6, 5e4),"\n")

if __name__ == '__main__':
	main()

os.system("pause")
