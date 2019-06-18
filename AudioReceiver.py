#TCPclient

import socket
import pygame as pg
import requests
import config as c

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def play(audio):
	if audio.__sizeof__() >= 4096:
			pg.mixer.init()
			pg.mixer_music.queue(audio)
			pg.mixer_music.quit()

#req = requests.get('''Página referente à solicitação dos áudios''')
audioName = input("Forneça uma música:\n")

clientSocket.send(audioName.encode('utf-8'))
buffer = open('audio.mp3','wb')

while True:

	
	#Recebendo o arquivo neste loop.
	while True:
		audio = clientSocket.recv(4096)
		
		#print(type(audio))
		#print(audio)
		if not audio: 
			break   
		buffer.write(audio)

	clientSocket.close()
	break
	print(buffer)
	#Criar uma forma de confirmar no cliente a msg de inexistência do arquivo.
	'''if audio == "Falso":
		audioName = input("Música não encontrada!\nForneça uma nova:\nSair!\n")
		clientSocket.send(audioName.encode('utf-8'))
		if audioName == "Sair":
			clientSocket.close()
	else:
		buffer.write(audio)
		play(buffer)
	'''	

buffer.close()
#clientSocket.close()

