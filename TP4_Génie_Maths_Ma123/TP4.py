"""
TP 4 - Génie Maths
Méthode de Dichotomie / Sécante + (PF, Newton)
VEYRAT-PARISIEN Mathis
"""
from math import*
from fonctions import*
from numpy import*
from matplotlib.pyplot import*

def PointFixe(g, x0, epsilon, Nitermax):
	'''Algorithme du théorème du point fixe'''
	xold = x0
	xnew = g(xold)
	erreur = abs(xnew - xold)
	xold = xnew
	n = 1
	l_PtFixe_n = [n]
	l_PtFixe_Xn = [x0]
	l_PtFixe_En = [erreur]

	while erreur > epsilon and n < Nitermax:
		xnew = g(xold)
		erreur = abs(xnew - xold)
		xold = xnew
		n += 1
		l_PtFixe_n.append(n)
		l_PtFixe_Xn.append(xnew)
		l_PtFixe_En.append(erreur)

	nb = len(l_PtFixe_n)
	semilogy(l_PtFixe_n, l_PtFixe_En)
	title("Représentation graphique de l'évolution de l'erreur de la méthode du Point Fixe")
	xlabel("Le nombre d'itération n")
	ylabel("l'erreur en")
	show()

	return xnew, n , l_PtFixe_n, l_PtFixe_Xn, l_PtFixe_En 

def Newton(f, fder,  x0, epsilon, Nitermax):
	'''Algorithme de la méthode de Newton'''
	xold = x0
	xnew = xold - f(xold)/fder(xold)
	erreur = abs(xnew - xold)
	xold = xnew
	n = 1
	l_newton_n = [n]
	l_newton_Xn = [x0]
	l_newton_En = [erreur]

	while erreur > epsilon and n < Nitermax:
		xnew = xold - f(xold)/fder(xold)
		erreur = abs(xnew - xold)
		xold = xnew
		n += 1
		l_newton_n.append(n)
		l_newton_Xn.append(xnew)
		l_newton_En.append(erreur)

	nb = len(l_newton_n)
	semilogy(l_newton_n, l_newton_En)
	title("Représentation graphique de l'évolution de l'erreur de la méthode de Newton")
	xlabel("Le nombre d'itération n")
	ylabel("l'erreur en")
	show()

	return xnew, n, l_newton_n, l_newton_Xn, l_newton_En

def dichotomie(f, a0, b0, epsilon, Nitermax):
	'''Fonction de l'algorithme de la méthode par dichotomie'''
	an = a0
	bn = b0
	erreur = abs(bn - an)
	n = 1
	l_dichot_n = [n]
	l_dichot_Xn = [a0]
	l_dichot_En = [erreur]
	while erreur > epsilon and n < Nitermax:
		m = (an + bn)/2

		if (f(an)*f(m) <= 0):
			bn = m

		else: 
			an = m
		erreur = abs(bn - an)
		n += 1
		l_dichot_n.append(n)
		l_dichot_Xn.append(an)
		l_dichot_En.append(erreur)

	nb = len(l_dichot_n)
	semilogy(l_dichot_n, l_dichot_En)
	title("Représentation graphique de l'évolution de l'erreur de la méthode par dichotomie")
	xlabel("Le nombre d'itération n")
	ylabel("l'erreur en")
	show()

	return m, n, l_dichot_n, l_dichot_Xn, l_dichot_En


def secante(f, x0, x1, epsilon, Nitermax):
	'''Fonction de l'algorithme de la méthode de la sécante'''
	erreur = abs(x1 - x0)
	n = 1
	l_secant_n    =[n]
	l_secant_Xn   =[x0]
	l_secant_En   =[erreur]
	while erreur > epsilon and n < Nitermax:
		x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
		x0 = x1
		x1 = x2
		erreur = abs(x1 - x0)
		n += 1
		l_secant_n.append(n)
		l_secant_Xn.append(x2)
		l_secant_En.append(erreur)

	nb = len(l_secant_n)
	semilogy(l_secant_n, l_secant_En)
	title("Représentation graphique de l'évolution de l'erreur de la méthode de la sécante")
	xlabel("Le nombre d'itération n")
	ylabel("l'erreur en")
	show()

	return x2, n, l_secant_n, l_secant_Xn, l_secant_En


def main():

	print("#"*10 + "Point Fixe" + "#"*10)
	print("La solution pour la cinquième équation est : ", PointFixe(g5, 3/2 ,1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", PointFixe(g6, 1.8 ,1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", PointFixe(g7, 1.6 ,1e-6, 5e4),"\n")

	print("#"*10 + "Newton" + "#"*10)
	print("La solution pour la cinquième équation est : ", Newton(f5, fder5,   3/2 ,1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", Newton(f6, fder6,   1.8 ,1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", Newton(f7, fder7,   1.6 ,1e-6, 5e4),"\n")

	print("#"*10 + "Dichotomie" + "#"*10)
	print("La solution pour la cinquième équation est : ", dichotomie(f5, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", dichotomie(f6, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", dichotomie(f7, 1, 2, 1e-6, 5e4),"\n")

	print("#"*10 + "Sécante" + "#"*10)
	print("La solution pour la cinquième équation est : ", secante(f5, 1.2, 2, 1e-6, 5e4),"\n")
	print("La solution pour la sixième équation est :   ", secante(f6, 1, 2, 1e-6, 5e4),"\n")
	print("La solution pour la septième équation est :  ", secante(f7, 1, 2, 1e-6, 5e4),"\n")

	print("#"*10 + "Pour l'équation 2x = 1 + sin(x)" + "#"*10)
	print("La solution avec la méthode du point fixe est: ", PointFixe(g, 0, 1e-6, 5e4),"\n")
	print("La solution avec la méthode de Newton est: ", Newton(f, fder, 0, 1e-6, 5e4),"\n")
	print("La solution avec la méthode par dichotomie est: ", dichotomie(f, 0, 1, 1e-6, 5e4),"\n")
	print("La solution avec la méthode de la sécante est: ", secante(f, 0, 1, 1e-6, 5e4))

if __name__ == '__main__':
	main()
