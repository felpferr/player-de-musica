#TCPclient

import socket
import pygame as pg
import requests
import config as c
import threading

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def play(audioName):
	buffer = open('audio.mp3','rb')
	pg.mixer.init()
	pg.mixer.music.load(buffer)
	pg.mixer.music.play()

	th = threading.Thread(target=)

#req = requests.get('''Página referente à solicitação dos áudios''')
audioName = input("Forneça uma música:\n")

clientSocket.send(audioName.encode('utf-8'))
buffer = open('audio.mp3','wb')
i = 0
while True:

	#Recebendo o arquivo neste loop.
	while True:
		audio = clientSocket.recv(4096)
		#print(audio)
		if not audio: 
			break   
		buffer.write(audio)
	
	#play(buffer)

	#clientSocket.close()
	#break
	
	
	#Criar uma forma de confirmar no cliente a msg de inexistência do arquivo.
	'''if audio == "Falso":
		audioName = input("Música não encontrada!\nForneça uma nova:\nSair!\n")
		clientSocket.send(audioName.encode('utf-8'))
		if audioName == "Sair":
			clientSocket.close()
	else:
	'''	

buffer.close()
#clientSocket.close()

