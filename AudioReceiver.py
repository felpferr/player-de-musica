#TCPclient

import socket
import pygame as pg
import requests
import config as c

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#req = requests.get('''Página referente à solicitação dos áudios''')
audioName = input("Forneça uma música:\n")

clientSocket.send(audioName.encode('utf-8'))
buffer = open('audio.mp3','a')

while True:
    audio = clientSocket.recv(1024)
    audio = audio.decode('utf-8')
    if audio == "Falso":
        audioName = input("Música não encontrada!\nForneça uma nova:\nSair")
        clientSocket.send(audioName.encode('utf-8'))
    else:
        #if audio == 'EOF':
        #    break
        buffer.write(audio)
        if buffer.__sizeof__() >= 2048:
            pg.mixer.music.load(buffer)
            

buffer.close()
clientSocket.close()

