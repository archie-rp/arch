#Created by Achierp
#Contact:archlinux@gmail.com
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

import os
import sys
import socket
import sqlite3
import subprocess
from termcolor import colored, cprint
#Global variables
linha =  colored("-"*30, 'blue')
global m_Home
m_Home = '/home/' + os.getenv("USER")
pasta=os.getcwd()

#Global functions
def internet(host="8.8.8.8", port=53):
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
	"""
	try:
		socket.setdefaulttimeout(1)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		result=(colored('Online' , 'green'))
		return result
	except Exception as ex:
		result=(colored('Offline' , 'red'))
		return result

def start_check():
	#attrs=['reverse', 'blink']
	distro = (colored('Arch Linux', 'blue'))
	print('\n Username : ' + os.getenv("USER") +'\n Hostname : ' + os.uname()[1] + '\n Internet connection : ' +internet()
		+ '\n Distribution :' + distro)

def ficheiro(nome):
	if not os.path.exists(nome):
		pass
	else:
		os.remove(nome)

def instalar(x,y):
	os.system("clear")
	print (linha)
	print((colored("Instalar pacotes: ", 'cyan', attrs=['bold'])))
	print (linha)
	print((colored("A installar :", 'green') + '"' + colored(x, 'blue') + '"'))
	if y == 'pacman':
		os.system('sudo pacman -Syu --noconfirm ' + x )
	elif y == 'yaourt':
		os.system('yaourt --noconfirm -S ' + x )
	else:
		input("Gestor de pacotes invalido")
	pass

#Others
class user():

	def add(self):
		os.system('clear')
		print (linha)
		print((colored("Adicionar Utilizador: ", 'cyan', attrs=['bold'])))
		print (linha)
		utilizador=input("Nome:")
		if utilizador == '':
			text=input("\nNome invalido!\n Voltar <Enter>")
		else:
			os.system('sudo useradd -m -g users -G wheel,storage,video,audio,network -s /bin/bash ' + utilizador)
			print((colored("Password Utilizador: ", 'red', attrs=['bold'])))
			os.system('\nsudo passwd ' + utilizador)
	def remove(self):
		os.system('clear')
		user.list()
		print((colored("Remover Utilizador: ", 'red', attrs=['bold'])))
		print (linha)
		numero=input(colored('Número: ', 'green'))
		utilizadores=user.list()
		numero=int(numero)
		##    remove = utilizadores[numero]
		#if len(utilizadores[numero]) > 1:
		#	teste=input("Utilizador removido")
		#	#os.system('sudo userdel -r ' + user.list(numero))
		#else: 
		#	teste=input("Utilizador nao existe!")
		try:
		    b = utilizadores[numero]
		    print ("Existe!")
		    os.system('sudo userdel -r ' + b)
		except IndexError:
		    print ("Não existe!")

	def list(p=0):
		os.system("clear")
		print (linha)
		print((colored("Utilizadores", 'green' )))
		print (linha)
		#utilizadores=os.system("cat /etc/passwd | grep '/home' | cut -d: -f1")
		utilizadores = os.popen("cat /etc/passwd | grep '/home' | cut -d: -f1").readlines()
		#r = subprocess.Popen(["cat /etc/passwd | grep '/home' | cut -d: -f1"], stdout=subprocess.PIPE)
		#r = subprocess.check_output('cat /etc/passwd | grep "/home" | cut -d: -f1',shell=False)
		#os.system(lista + " >> .users.txt")
		#os.system("users >> .users.txt")
		#users = open(pasta + '/' + '.users.txt', 'r+')
		#users = users.read()
		#ficheiro('.users.txt')
		#utilizadores=map(str.strip, utilizadores)
		#out = r.stdout.read()
		#teste=utilizadores.strip("\n")
		utilizadores = [x.replace('\n', '') for x in utilizadores]
		#sda=input("Array:")
		#print (k) 
		print ('\nExistentes:')
		for u in range(len(utilizadores)):
			if utilizadores[u] == '':
				pass
			else:
				print(colored(u , 'yellow') ,utilizadores[u])
		
		return utilizadores

	def clean(self):
		os.system("clear")
		print (linha)
		print((colored("Limpar Apps: ", 'cyan', attrs=['bold'])))
		print (linha)
		print('\nsudo pacman -Rsc --noconfirm $(pacman -Qqdt)')
		os.system('sudo pacman -Rsc --noconfirm $(pacman -Qqdt)')
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
		


def check_system():
	#installar("dmidecode", "pacman")
	#chipset=os.system("dmidecode --type 1 | grep 'Product Name:'")
	#chipset = os.popen("dmidecode --type 1 | grep 'Product Name:'").readlines()
	chipset = os.popen("dmidecode --type 1 | egrep -i 'virtualbox|bumblebee|nvidia|advanced micro devices|intel corporation' | cut -d: -f2| cut -c2-").readlines()
	#print(chipset)
	vga = [x.replace('\n', '') for x in chipset]
	#print(vga)
	vga="".join(vga)
	vga=vga.lower()
	#input("Chipset: "+ chipset)
	if vga == "virtualbox":
		print("virtualbox!")
	elif vga == "bumblebee":
		print("bumblebee!")
	elif vga == "nvidia":
		print("nvidia!")
	elif vga == "advanced micro devices":
		print("advanced micro devices")
	elif vga == "intel corporation":
		print("intel corporation")
	else:
		"Error no vga found"

class database():

	def create(self):
		#connection = sqlite3.connect("example.db")
		connection = sqlite3.connect("db.db")
		c = connection.cursor()
		#c.execute('create table Persons (id int, name text, city text)')
		c.execute('create table Applications (id integer primary key, name blob, service int, name_service text)')
		#c.execute('insert into Persons VALUES (1, "smith", "dallas")')
		c.execute('insert into Applications (name) VALUES ("nano")')
		c.execute('insert into Applications (name) VALUES ("vim")')
		connection.commit()
		connection.close()

	def read(self):
		conn = sqlite3.connect('db.db')
		c = conn.cursor()
		app=c.execute("DELETE FROM Applications WHERE name IS NULL OR trim(name) = ''")
		x = c.execute("select name from Applications")
		apps= ''
		for row in x:
			apps+=row[0] + ' '

		#print ("apps:", apps)
		#data= x.fetchall()
		print('apps:', x)
		data=apps.split(' ')
		#data='  '.join(apps).split()
		#data=filter(None, data)
		#data = filter(lambda x: len(x)>0, data)
		#data=apps.split(' ')
		tdata=len(data)
		ddata=(int(tdata/2))
	
		#A = [1,2,3,4,5,6]
		#B = data[0:tdata/2]
		#C = data[tdata/2:]
		#B,C=data[:len(data)/2],data[len(data)/2:]
		#print('data:',data,' tamanho:',tdata)
		for i in range(ddata):
			print("menu1 %-20s menu2 %10s" % (data[i], data[i+ddata]))
		#str1 = ''.join(str(e) for e in data)
		#str1 = [x.replace("('", '') for x in str1]
		#
		#data1=' '.join([str(x) for x in data])
		#data3=' '.join(data1)
		#print ("data :",data)
		#print ("data1 :",data1)
		#print ("data 3 :",data3)
		#instalar(apps, 'pacman')
		return apps

	def insert(self, p):
			#connection = sqlite3.connect("example.db")
			connection = sqlite3.connect("db.db")
			c = connection.cursor()
			#c.execute('create table Persons (id int, name text, city text)')
			#c.execute('create table Applications (id integer primary key, name blob, service int, name_service text)')
			#c.execute('insert into Persons VALUES (1, "smith", "dallas")')
			p=input("APPS a inserir:")
			c.execute('insert into Applications (name) VALUES ("' + p + '")')
			connection.commit()
			connection.close()

	def remove(self, p):
			#connection = sqlite3.connect("example.db")
			connection = sqlite3.connect("db.db")
			c = connection.cursor()
			#c.execute('create table Persons (id int, name text, city text)')
			#c.execute('create table Applications (id integer primary key, name blob, service int, name_service text)')
			#c.execute('insert into Persons VALUES (1, "smith", "dallas")')
			print ("APPS a remover:", p)
			#c.execute('delete from Applications (name) where name=', p )
			c.execute("DELETE FROM Applications WHERE name=?", (p,))
			connection.commit()
			connection.close()

	def instalar(self):
			apps=database.read("apps")
			print("sudo pacman -Syu --noconfirm ", apps)
			apps=apps.split(' ')
			print("\nslice:",apps)
			apps_installed = os.popen("pacman -Q -q").readlines()
			apps_installed = [x.replace('\n', '') for x in apps_installed]
			install=set(apps).difference(apps_installed)
			install=' '.join(install)
			print("\ninstalar: ", install)
			#os.system('sudo pacman -Syu --noconfirm ' + apps )

