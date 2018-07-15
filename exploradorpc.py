__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-

import requests
import json
import time

def abrir_fichero():
	global direcciones
	#f = 'C:/Users/ACER/Documents/datos.txt'
	f = 'datos.txt'
	try:
		fit = open(f, 'r')
		direcciones = []
		a = fit.readline()
		while a != "":
			a = a[0 :-1]
			direcciones.append(a)
			a = fit.readline()
		fit.close()
		print ('>> CARGADO FICHERO CON ' + str(len(direcciones)) + ' DIRECCIONES')
	except:
		print ('### ERROR FICHERO NO EXISTENTE ###')

def b1(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b2(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b3(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
			
def b4(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
def b5(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b6(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b7(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b8(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b9(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def b10(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
def b11(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b12(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b13(addr):
	try:
	
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b14(addr):
	try:
		request = 'http://127.0.0.1:3001/ext/getbalance/' + addr
		response = requests.get(request, timeout=10)
		content = float(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1

def eureca(direccion):
        f = open ("eureca.txt", "a")
        f.write((direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b1')+ " hay una direccion con sat\n")
        f.close()

global direcciones

n = 1
naddr = 0
pausa = 0.1
nerror = 0
abrir_fichero()


while naddr<= len(direcciones):
	if n == 1:
		saldo = b1(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b1')
			time.sleep(pausa)
			n = 2
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 2
			nerror += 1
	elif n == 2:
		saldo = b2(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b2')
			time.sleep(pausa)
			n = 3
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 3
			nerror += 1
	elif n == 3:
		saldo = b3(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b3')
			time.sleep(pausa)
			n = 4
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 4
			nerror += 1
	elif n == 4:
		saldo = b4(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b4')
			time.sleep(pausa)
			n = 5
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 5
			nerror += 1
	elif n == 5:
		saldo = b5(direcciones[naddr])
		if saldo != -1:
                        
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b5')
			time.sleep(pausa)
			n = 6
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 6
			nerror += 1
	elif n == 6:
		saldo = b6(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b6')
			time.sleep(pausa)
			n = 7
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 7
			nerror += 1
	elif n == 7:
		saldo = b7(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b7')
			time.sleep(pausa)
			n = 8
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 8
			nerror += 1
	elif n == 8:
		saldo = b8(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b8')
			time.sleep(pausa)
			n = 9
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 9
			nerror += 1
	elif n == 9:
		saldo = b9(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b9')
			time.sleep(pausa)
			n = 10
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 10
			nerror += 1
	elif n == 10:
		saldo = b10(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b10')
			time.sleep(pausa)
			n = 11
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 11
			nerror += 1
	elif n == 11:
		saldo = b11(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b11')
			time.sleep(pausa)
			n = 12
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 12
			nerror += 1
	elif n == 12:
		saldo = b12(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b12')
			time.sleep(pausa)
			n = 13
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 13
			nerror += 1
	elif n == 13:
		saldo = b13(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b13')
			time.sleep(pausa)
			n = 14
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 14
			nerror += 1
	elif n == 14:
		saldo = b14(direcciones[naddr])
		if saldo != -1:
			print (direcciones[naddr] + ' -- SALDO= ' + str(saldo) + ' Sat - b14')
			time.sleep(pausa)
			n = 1
			naddr +=1
			nerror = 0
			if saldo>0:
				eureca(direcciones[naddr])
		else:
			n = 1
			nerror += 1
	if nerror > 14:
		exit()
	
