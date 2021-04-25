# -*- coding: utf-8 -*-
"""
Grand Projet Semestre 2
"""
import os
from tkinter import*
from tkinter import ttk
from pandas import*
from numpy import*
from matplotlib import*
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import*
from time import*


###PARTIE création et configuration de la fenêtre###
Mafenetre = Tk() #Creation de la fenetre

Mafenetre.iconbitmap(".\\Logo\\Logo_Avion.ico") #Changer le logo en haut à gauche sur la fenêtre
Mafenetre.config(background = "#fcfbfa") # Changer couleur du fond de la fenêtre

Mafenetre.state('zoomed')
Mafenetre.minsize(1200,700)

onglets = ttk.Notebook(Mafenetre) #Faire le menu

onglets.place(relwidth = 1, relheight = 1)

onglet1 = ttk.Frame(onglets)
onglet1.grid(column = 0)
onglet2 = ttk.Frame(onglets)
onglet2.grid(column = 1)
onglet3 = ttk.Frame(onglets)
onglet3.grid(column = 2)

onglets.add(onglet1, text = "LOGIN")
onglets.add(onglet2, text = "PASSENGERS")
onglets.add(onglet3, text = "FLIGHT VISUALIZATION")

Mafenetre.title("Flight Analyses System") #Nom de la fenetre


label_title = Label(onglet1, text = "Welcome to Flight Analyses Systeme", font = ("Adobe Caslon Pro Bold", 20)) #Titre / police / taille
label_title.place(relx = 0.35, rely = 0)

label_email1 = Label(onglet1, text = "Email:", bg = '#03224c', fg = "white", font = ("Adobe Caslon Pro Bold", 10)) #Texte Email / couleur
label_email1.place(relx = 0.4, rely = 0.3)
label_password1 = Label(onglet1, text = "Password:", bg = "#A31E01", fg = "white", font = ("Adobe Caslon Pro Bold", 10)) #Texte Password / couleur
label_password1.place(relx = 0.4, rely = 0.34)

###Partie Login###
email_entry = StringVar()
password_entry = StringVar()


def login():
	'''Fonction qui vérifie si l'utilisateur peut se connecter'''
	log = False
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

		if str(password[numero]) == password_user:
			confirmation_pass = 1
			break

		else:
			confirmation_pass = 0

	if confirmation_email and confirmation_pass == 1:
		affichage_resultat1 = Label(onglet1, text = "Bienvenue dans le système d'analyse", padx = 50, font = ("Arial", 10))
		affichage_resultat1.place(relx = 0.38, rely = 0.45)
		log = True

	else:
		affichage_resultat1 = Label(onglet1, text = "Ce compte n'est pas valide !", padx = 55, font = ("Arial", 10))
		affichage_resultat1.place(relx = 0.4, rely = 0.45)

	return log
	

Entree_email1 = Entry(onglet1, textvariable = email_entry) #Zone de saisie pour Email
Entree_email1.place(relx = 0.45, rely = 0.305)
Entree_password1 = Entry(onglet1, textvariable = password_entry, show = "•") #Zone de saisie pour Password
Entree_password1.place(relx = 0.45, rely = 0.345)


Bouton_login = Button(onglet1, text = "Login", command = lambda:[login_time(login())], bg = "#c3c3c3", fg = "black", bd = 2, activebackground='darkgrey', font = ("Arial", 10)) #Bouton Login / couleur / bordure / couleur background quand on clique  
Bouton_login.place(relx = 0.475, rely = 0.4)


label_email2 = Label(onglet1, text = "Email:", bg = '#03224c', fg = "white", font = ("Adobe Caslon Pro Bold", 10)) #Texte Email / couleur 
label_email2.place(relx = 0.4, rely = 0.5)
label_password2 = Label(onglet1, text = "Password:", bg = "#A31E01", fg = "white", font = ("Adobe Caslon Pro Bold", 10)) #Texte Password / couleur
label_password2.place(relx = 0.4, rely = 0.54)

def login_time(log):
	'''Ajouter le numero, l'email, la date et l'heure de conexion
	 dans le fichier user_login pour un utilisateur qui viens de ce connecter'''
	df = read_csv('user_login.csv', delimiter = ',')

	number = df['number']

	email_user = email_entry.get()

	new_date = strftime('%d/%m/%y', localtime())
	new_time = strftime('%H:%M:%S', localtime())
	number_max = max(number)
	new_number = number_max + 1

	if log == True:
		df.loc[2] = [new_number, email_user, new_date, new_time]
		df.to_csv('user_login.csv', sep = ',', index = False)

	else:
		pass


###Partie Signup###
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
			affichage_resultat2 = Label(onglet1, text = "Vous êtes déjà inscrit !", padx = 50, font = ("Arial", 10))
			affichage_resultat2.place(relx = 0.415, rely = 0.65)
			a = 1
			
		position_user = nb_element + 1
		
	if a == 0:
                        
		Data_Frame.loc[55] = [position_user, new_email, new_password]
		affichage_resultat2 = Label(onglet1, text = "Votre compte a été créé.", padx = 50, font = ("Arial", 10))
		affichage_resultat2.place(relx = 0.41, rely = 0.65)

	Data_Frame.to_csv('user_info.csv', sep = ',', index = False)		


Entree_email2 = Entry(onglet1, textvariable = email_entry2) #Zone de saisie pour Email
Entree_email2.place(relx = 0.45, rely = 0.505)

Entree_password2 = Entry(onglet1, textvariable = password_entry2, show = "•") #Zone de saisie pour Password
Entree_password2.place(relx = 0.45, rely = 0.545)


Bouton_signup = Button(onglet1, text = "Signup", command = Signup, bg = "#c3c3c3", fg = "black", bd = 2, activebackground='darkgrey', font = ("Arial", 10)) #Bouton Signup / couleur / bordure / couleur background quand on clique 
Bouton_signup.place(relx = 0.475, rely = 0.6)

def cliquer():
	'''Permet de connaitre le nombre de clique sur le bouton'''
	global cpt
	cpt += 1

def view():
	'''Permet d'appliquer ou non les "*" pour les mots de passes'''
	if cpt%2 == 1: #Si le nombre de clique est impaire alors l'utilisateur peut voir le mot de passe

		Entree_password1 = Entry(onglet1, textvariable = password_entry)
		Entree_password1.place(relx = 0.45, rely = 0.345)

		Entree_password2 = Entry(onglet1, textvariable = password_entry2)
		Entree_password2.place(relx = 0.45, rely = 0.545)

	else:

		Entree_password1 = Entry(onglet1, textvariable = password_entry, show = "•")
		Entree_password1.place(relx = 0.45, rely = 0.345)

		Entree_password2 = Entry(onglet1, textvariable = password_entry2, show = "•")
		Entree_password2.place(relx = 0.45, rely = 0.545)


photo_eye = PhotoImage(file = ".\\Logo\\eye.gif")
cpt = 0
Bouton_mdp = Button(onglet1,  command = lambda:[cliquer(), view()], image = photo_eye)
Bouton_mdp.place(relx = 0.6, rely = 0.45)

###Partie Passengers###

def liste():
    i = 0
    df = read_csv('passenger_info.csv', delimiter=(';'))
    confiramation = 0
    for airline in df['Airline']:
        i+=1
        if str(airline) == spinbox1.get():
            numero=i-1
            destination = df['Destination']
            prix = df['Price']
            if str(destination[numero]) == spinbox2.get():
                if str(prix[numero]) == spinbox3.get():
                    print('gg')
                    confirmation = 1
                    passengersid = df['PassengerID']
                    a=str(passengersid[numero])
                    nom=df['Lastname']
                    b=str(nom[numero])
                    terminal=df['Terminal']
                    c=str(terminal[numero])
                    zone=df['Boarding Area']
                    d=str(zone[numero])
                    affichage=tableau.insert(parent='', index=0, text='', values=(a,b,c,d))


Bouton_passengers = Button(onglet2, text = "list passengers", command = liste, font = ("Adobe Caslon Pro Bold", 12))
Bouton_passengers.place(relx = 0.05, rely = 0.12, relwidth = 0.2, relheight = 0.1)

libelle = Label(onglet2, text = 'Passenger Information', font = ("Adobe Caslon Pro Bold", 15))
libelle.place(relx = 0.5, rely = 0.1, relwidth = 0.3, relheight = 0.2)


tableau = ttk.Treeview(onglet2, columns=('passengerid', 'lastname', 'terminal','BoardingArea')) 
tableau.heading('passengerid', text='Passengerid')
tableau.heading('lastname', text='Lastname')
tableau.heading('terminal', text='Terminal')
tableau.heading('BoardingArea', text='Boarding Area')
tableau['show'] = 'headings'
tableau.place(relx = 0.28, rely = 0.3, relwidth = 0.7, relheight = 0.5)

df = read_csv('passenger_info.csv', sep=';')

company = list(set(df['Airline'].values.tolist()))
destination = list(set(df['Destination'].values.tolist()))
price= list(set(df['Price'].values.tolist()))


spinbox1 = ttk.Spinbox(onglet2, values = company)
spinbox1.place(relx = 0, rely = 0.05)

spinbox2 = ttk.Spinbox(onglet2, values = destination )
spinbox2.place(relx = 0.1, rely = 0.05)

spinbox3 = ttk.Spinbox(onglet2, values = price )
spinbox3.place(relx = 0.2, rely = 0.05)


###Partie Flight Visualization###

dd = read_csv('flight_info.csv', delimiter=',')

 

tv = ttk.Treeview(onglet3)
tv.place(relwidth = 1, relheight = 1)

 

tv = ttk.Treeview(onglet3, column=('Year','Month','DayofMonth','DayOfWeek','FlightDate','FlightNum','OriginAirportID','OriginCityName','OriginState','OriginStateName','DestAirportID','DestCityName','DestState','DestStateName','DepTime','DepDelayMinutes','ArrTime','ArrDelayMinutes','AirTime','Distance'))

 


tv.column('#0', width=0, stretch=NO)
tv.column('Year', anchor=CENTER, width=50)
tv.column('Month', anchor=CENTER, width=50)
tv.column('DayofMonth', anchor=CENTER, width=60)
tv.column('DayOfWeek', anchor=CENTER, width=80)
tv.column('FlightDate', anchor=CENTER, width=60)
tv.column('FlightNum', anchor=CENTER, width=80)
tv.column('OriginAirportID',anchor=CENTER, width=80 ) 
tv.column('OriginCityName', anchor=CENTER, width=80)
tv.column('OriginState', anchor=CENTER, width=60)
tv.column('OriginStateName', anchor=CENTER, width=80)
tv.column('DestAirportID',anchor=CENTER, width=80)
tv.column('DestCityName', anchor=CENTER, width=80)
tv.column('DestState', anchor=CENTER, width=55)
tv.column('DestStateName', anchor=CENTER, width=80)
tv.column('DepTime',anchor=CENTER, width=80)
tv.column('DepDelayMinutes',anchor=CENTER, width=80)
tv.column('ArrTime', anchor=CENTER, width=80)
tv.column('ArrDelayMinutes', anchor=CENTER, width=80)
tv.column('AirTime', anchor=CENTER, width=80)
tv.column('Distance', anchor=CENTER, width=55)

 

 

 

tv.heading('#0', text='', anchor=CENTER)
tv.heading('Year', text='Year', anchor=CENTER)
tv.heading('Month', text='Month', anchor=CENTER)
tv.heading('DayofMonth', text='DayofMonth', anchor=CENTER)
tv.heading('DayOfWeek', text='DayOfWeek', anchor=CENTER)
tv.heading('FlightDate', text='FlightDate', anchor=CENTER)
tv.heading('FlightNum', text='FlightNum', anchor=CENTER)
tv.heading('OriginAirportID', text='OriginAirportID', anchor=CENTER)
tv.heading('OriginCityName', text='OriginCityName', anchor=CENTER)
tv.heading('OriginState', text='OriginState', anchor=CENTER)
tv.heading('OriginStateName', text='OriginStateName', anchor=CENTER)
tv.heading('DestAirportID', text='DestAirportID', anchor=CENTER)
tv.heading('DestCityName', text='DestCityName', anchor=CENTER)
tv.heading('DestState', text='DestState', anchor=CENTER)
tv.heading('DestStateName', text='DestStateName', anchor=CENTER)
tv.heading('DepTime', text='DepTime', anchor=CENTER)
tv.heading('DepDelayMinutes', text='DepDelayMinutes', anchor=CENTER)
tv.heading('ArrTime', text='ArrTime', anchor=CENTER)
tv.heading('ArrDelayMinutes', text='ArrDelayMinutes', anchor=CENTER)
tv.heading('AirTime', text='AirTime', anchor=CENTER)
tv.heading('Distance', text='Distance', anchor=CENTER)

 

dd1 = dd['Year']
dd2 = dd['Month']
dd3 = dd['DayofMonth']
dd4 = dd['DayOfWeek']
dd5 = dd['FlightDate']
dd6 = dd['FlightNum']
dd7 = dd['OriginAirportID']
dd8 = dd['OriginCityName']
dd9 = dd['OriginState']
dd10 = dd['OriginStateName']
dd11 = dd['DestAirportID']
dd12 = dd['DestCityName']
dd13 = dd['DestState']
dd14 = dd['DestStateName']
dd15 = dd['DepTime']
dd16 = dd['DepDelayMinutes']
dd17 = dd['ArrTime']
dd18 = dd['ArrDelayMinutes']
dd19 = dd['AirTime']
dd20 = dd['Distance']

 


len(dd1)
a = 0

 

#tableau du haut
 

while a < len(dd1):
    tv.insert(parent='', index=a, iid=a, text='', values=(dd1[a],dd2[a],dd3[a],dd4[a],dd5[a],dd6[a],dd7[a],dd8[a],dd9[a],dd10[a],dd11[a],dd12[a],dd13[a],dd14[a],dd15[a],dd16[a],dd17[a],dd18[a],dd19[a],dd20[a]))
    a += 1

 

tv.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.3)

 

#tableau du bas
 

fig2 = ttk.Treeview(onglet3)

 

data1 = {'ville': ['AA                Arizona','AB                Texas','AC                Florida','AD                North Carolina','AE                California','AF                Pennsylvania','AG                Washington',
                   'AH                Nevada','AI                Georgia','AJ                Virginia','AK                Wisconsin','AM                          Ohio','AN                                    Illinois','AO                Missouri',
                   'AP                       Nebraska','AQ                Indiana','AR                Utah','AS                Massachusetts','AT                Hawaii','AU                        New York','AV                            Iowa',
                   'AW                Minnesota','AX                Colorado','AY                Oregon','AZ                Maryland'],
         'Top':[1077,469,296,228,166,116,87,69,69,64,58,55,54,51,31,23,20,17,17,16,8,7,1,1,1]
        }

 

df1 = DataFrame(data1,columns=['ville','Top'])

 

data2 = {'ville': ['Arizona','California','Colorado','Florida','Georgia','Hawaii','Illinois','Indiana','Iowa','Maryland','Massachusetts','Minnesota','Missouri','Nebraska','Nevada','New York','North Carolina','Ohio','Oregon','Pennsylvania','Texas','Utah','Virginia','Washington','Wisconsin'],
         'Dep': [10846,2057,87,1734,768,243,776,286,36,22,21,66,220,180,630,174,1239,795,0,1288,4479,407,706,896,165]
        }
df2 = DataFrame(data2,columns=['ville','Dep'])

 

data3 = {'ville': ['Arizona','California','Colorado','Florida','Georgia','Hawaii','Illinois','Indiana','Iowa','Maryland','Massachusetts','Minnesota','Missouri','Nebraska','Nevada','New York','North Carolina','Ohio','Oregon','Pennsylvania','Texas','Utah','Virginia','Washington','Wisconsin'],
         'Arr': [12030,3065,79,2038,869,456,644,246,27,27,4,70,231,89,961,122,1208,707,0,1201,4360,544,648,824,157]
        }  
df3 = DataFrame(data3,columns=['ville','Arr'])
 
data4 = {'ville': ['AA                       Hawaii','AB                Arizona','AC                California','AD                North Carolina','AE                Nevada','AF                Ohio','AG                           Virginia',
                   'AH                       Florida','AI                      Minnesota','AJ                Indiana','AK                     Texas','AL                Wisconsin','AM                      Illinois','AN                        Nebraska','AO                Pennsylvania'],
         'Best': [2845,2845,2296,2296,2176,1995,1979,1972,1501,1488,1464,1460,1440,1330,1303]
        }  
df4 = DataFrame(data4,columns=['ville','Best'])

 

 

figure1 = plt.Figure(figsize=(6,5), dpi=50)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, onglet3)
bar1.get_tk_widget().place(relx = 0, rely = 0.3, relwidth = 0.3, relheight = 0.7)
df1 = df1[['ville','Top']].groupby('ville').sum()
df1.plot(kind='bar', legend=True, ax=ax1, color = '#CABF1A')
ax1.set_title('Le nombre de vols vers différentes destinations')

 

figure2 = plt.Figure(figsize=(6,5), dpi=60)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, onglet3)
bar2.get_tk_widget().place(relx = 0.3, rely = 0.3, relwidth = 0.25, relheight = 0.7)
df2 = df2[['ville','Dep']].groupby('ville').sum()
df2.plot(kind='bar', legend=True, ax=ax2, color = 'r')
ax2.set_title('DepDelayMinutes Vs. DestStateName')

 

figure3 = plt.Figure(figsize=(6,5), dpi=60)
ax3 = figure3.add_subplot(111)
bar3 = FigureCanvasTkAgg(figure3, onglet3)
bar3.get_tk_widget().place(relx = 0.55, rely = 0.3, relwidth = 0.25, relheight = 0.7)
df3 = df3[['ville','Arr']].groupby('ville').sum()
df3.plot(kind='bar', legend=True, ax=ax3, color = 'r')
ax3.set_title('ArrDelayMinutes Vs. DestStateName')

 

figure4 = plt.Figure(figsize=(6,5), dpi=60)
ax4 = figure4.add_subplot(111)
bar4 = FigureCanvasTkAgg(figure4, onglet3)
bar4.get_tk_widget().place(relx = 0.80, rely = 0.3, relwidth = 0.20, relheight = 0.7)
df4 = df4[['ville','Best']].groupby('ville').sum()
df4.plot(kind='bar', legend=True, ax=ax4, color = 'g')
ax4.set_title('Les plus long dest.')


Mafenetre.mainloop()