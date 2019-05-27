#TCPclient

import socket
import pygame as pg
import requests
import config as c

serverName = '10.3.1.20'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

req = requests.get('''Página referente à solicitação dos áudios''')
audioName = input()

clientSocket.send(audioName.encode('utf-8'))
buffer = open('audio.mp3','rw')

while True:
    audio = connectionSocket.recv(512)
    if audio == 'EOF':
        break
    buffer.write(audio.decode('utf-8'))
    if buffer.size() >= 1024:
        pg.mixer.music.load(buffer)
            

clientSocket.close()

