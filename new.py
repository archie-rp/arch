#! /usr/bin/env python

#Created by Achierp
#Contact:archlinux@gmail.com
#
#This file is part of Foobar.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Includes
import os
import sys
from functions import ficheiro, instalar, check_system, database, user, start_check
from termcolor import colored, cprint
os.system("clear")
linha =  colored("-"*30, 'blue')
ans=True
erro=""
db= database()
utilizador=user()

while ans:
	os.system("clear")
	start_check()
	valor1=("valor 1 ")
	valor2=("valor 2 ")
	#print("menu1 %-20s menu2 %10s" % (valor1, valor2))
	print (colored("\nMenu", 'white' , attrs=['bold']))
	menu = ["Utilizadores [Done]","GitHub [Done]","Drivers","Applications","Clear Orpans [Done]"]
	print (linha)
	for i in range(len(menu)):
		print(colored(i , 'yellow') ,menu[i])
	print (erro)

	print ("x) Sair")
	erro= ""
	ans=input("\nWhat would you like to do? ")
	if ans=="0":
		erro= ""
		os.system("clear")
		utilizador.list()
		print("\n"+ linha)
		users = ["Add User","Remove User","Back"]
		for i in range(len(users)):
			print(colored(i , 'yellow') ,users[i])
		print (erro)
		ans=input("\nWhat would you like to do? ")
		if ans=="0":
			utilizador.add()
			#text=input(colored("\nMenu principal ", 'green' ) + "<enter>"))
		elif ans=="1":
			 utilizador.remove()
			 text=input("")
		elif ans== "2":
			pass

	elif ans=="1":
		print("\n GitHub") 
		os.system("clear")
		print(linha+(colored("GitHub: ", 'cyan', attrs=['bold']))+linha)
		instalar('xclip git', 'pacman')
		os.system("clear")
		print((colored("GitHub: ", 'cyan', attrs=['bold'])))
		rsp="no"
		while rsp == "no":
			github_utilizador=input(colored('\nGitHub','yellow')+ colored('@', 'red') + 'Nome:')
			github_email=input(colored('GitHub','yellow') + colored('@', 'red') +  'Email:')
			rsp=input("Confirmar? yes/no")
		else:
		 	#os.system('git config --global user.email ' + github_email )
		  	#os.system('git config --global user.name ' + github_utilizador)
		  	input("YES github")
		exit=input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif ans=="2":
		print("\n Drivers\n Cheking system... VGA graphics") 
		check_system()
		input("Done chipset")
	elif ans=="3":
		print("\n APPS database sqlite3\n") 
		rsp=input("Create , read , insert, remove, install(1,2,3,4,5)")
		if rsp == "1":
			db.create()
		elif rsp == "2":
			db.read()
		elif rsp == "3":
			#apps=input("Apps para inserir:thunar vlc ... ")
			db.insert(apps)
		elif rsp == "4":
			apps=input("Applicacoes a remover:")
			db.remove(apps)
		elif rsp == "5":
			apps=input("Applicacoes a instalar:")
			db.instalar()
		else:
			pass
		input("Done!")
	elif ans=="4":
		utilizador.clean()
	elif ans=="x":
		print("\n Goodbye")
		ans = None 
	elif ans !="":
		#os.system("clear")
		erro =(colored('Opção não válida', 'red', attrs=['bold']))
