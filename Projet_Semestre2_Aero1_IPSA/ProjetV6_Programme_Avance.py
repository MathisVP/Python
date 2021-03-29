# -*- coding: utf-8 -*-
"""
Grand Projet Semestre 2
LOGIN
"""
import os
from tkinter import*
from tkinter import ttk
from pandas import*
from numpy import*
from matplotlib import*

Mafenetre = Tk() #Creation de la fenetre

Mafenetre.iconbitmap(".\\Login\\Logo\\Logo_Avion.ico") #Changer le logo en haut à gauche sur la fenêtre
Mafenetre.config(background = "#fcfbfa") # Changer couleur du fond de la fenêtre

onglets = ttk.Notebook(Mafenetre) #Faire le menu
onglets.grid(row = 0)

onglet1 = ttk.Frame(onglets)
onglet1.grid(column = 0)
onglet2 = ttk.Frame(onglets, width = 720, height = 480)
onglet2.grid(column = 1)
onglet3 = ttk.Frame(onglets)
onglet3.grid(column = 2)

onglets.add(onglet1, text = "LOGIN")
onglets.add(onglet2, text = "PASSENGERS")
onglets.add(onglet3, text = "FLIGHT VISUALIZATION")

Mafenetre.title("Flight Analyses System") #Nom de la fenetre


label_title = Label(onglet1, text = "Welcome to Flight Analyses Systeme", font = ("Times New Romans", 15)) #Titre / police / taille
label_title.grid(row = 0, column = 1)

label_email1 = Label(onglet1, text = "Email:", bg = "#bdbbbb", fg = "black") #Texte Email / couleur
label_email1.grid(row = 1, pady = 10)
label_password1 = Label(onglet1, text = "Password:", bg = "#bdbbbb", fg = "black") #Texte Password / couleur
label_password1.grid(row = 2)

email_entry = StringVar()
password_entry = StringVar()

def login():
	'''Fonction qui vérifie si l'utilisateur peut se connecter'''
	Data_Frame = read_csv('user_info.csv', delimiter = ',')


	email = Data_Frame['email']
	password = Data_Frame['password']

	email_user = email_entry.get()
	password_user = str(password_entry.get())

	i = 0
	confirmation_email = 0
	for csv_email in Data_Frame['email']:
		i += 1
		if str(csv_email).strip() == email_user:
			confirmation_email = 1

		numero = i - 1

		if password[numero] == password_user:
			confirmation_pass = 1
			break

		else:
			confirmation_pass = 0

	if confirmation_email and confirmation_pass == 1:
		affichage_resultat1 = Label(onglet1, text = "Bienvenue dans le système d'analyse", padx = 50)
		affichage_resultat1.grid(row = 4, column = 1)

	else:
		affichage_resultat1 = Label(onglet1, text = "Ce compte n'est pas valide!", padx = 50)
		affichage_resultat1.grid(row = 4, column = 1)

Entree_email1 = Entry(onglet1, textvariable = email_entry) #Zone de saisie pour  Email
Entree_email1.grid(row = 1, column = 1)
Entree_password1 = Entry(onglet1, textvariable = password_entry) #Zone de saisie pour  Password
Entree_password1.grid(row = 2, column = 1)


Bouton_login = Button(onglet1, text = "Login", command = login, bg = "#c3c3c3", fg = "black", bd = 2, activebackground='darkgrey') #Bouton Login / couleur / bordure / couleur background quand on clique  
Bouton_login.grid(row = 3, column = 1, pady = 30)

Mafenetre.bind('<Return>', login) ## Ne fonctionne pas encore

label_email2 = Label(onglet1, text = "Email:", bg = "#bdbbbb", fg = "black") #Texte Email / couleur 
label_email2.grid(row = 5, pady = 10)
label_password2 = Label(onglet1, text = "Password:", bg = "#bdbbbb", fg = "black") #Texte Password / couleur
label_password2.grid(row = 6)

email_entry2 = StringVar()
password_entry2 = StringVar()

def Signup():
	'''Fonction pour que l'utilisateur s'inscrive'''
	Data_Frame = read_csv('user_info.csv', delimiter = ',')


	email = Data_Frame['email']
	password = Data_Frame['password']

	nb_element = len(email)

	new_email = email_entry2.get()
	new_password = str(password_entry2.get())

	a = 0
	for csv_email in Data_Frame['email']:
		if str(csv_email).strip() == new_email:
			affichage_resultat2 = Label(onglet1, text = "Vous êtes déjà inscrit!", padx = 50)
			affichage_resultat2.grid(row = 8, column = 1)
			a = 1

		position_user = nb_element + 1

	if a == 0:
		Data_Frame.loc[55] = [position_user, new_email, new_password]
		affichage_resultat2 = Label(onglet1, text = "Votre compte a été créé.", padx = 50)
		affichage_resultat2.grid(row = 8, column = 1)

	Data_Frame.to_csv('user_info.csv', sep = ',', index = False) 

Entree_email2 = Entry(onglet1, textvariable = email_entry2) #Zone de saisie pour  Email
Entree_email2.grid(row = 5, column = 1)

Entree_password2 = Entry(onglet1, textvariable = password_entry2) #Zone de saisie pour  Password
Entree_password2.grid(row = 6, column = 1)


Bouton_signup = Button(onglet1, text = "Signup", command = Signup, bg = "#c3c3c3", fg = "black", bd = 2, activebackground='darkgrey') #Bouton Signup / couleur / bordure / couleur background quand on clique 
Bouton_signup.grid(row = 7, column = 1, pady = 30)



Mafenetre.mainloop()

