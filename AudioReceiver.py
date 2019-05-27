#TCPclient

import socket
import pygame as pg
import requests 

serverName = '10.3.1.20'
serverPort = 13000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

req = requests.get('Página referente à solicitação dos áudios')
audioName = input()

clientSocket.send(audioName.encode('utf-8'))
buffer = open('audio.mp3','rw')

for audio != 'EOF':
    audio = connectionSocket.recv(512)
    buffer.write(audio.decode('utf-8'))
    if buffer.size() >= 1024:
        pg.mixer.music.load(buffer)
    




'''
with open('nomedoaquivo{}'.format(mp3),buffering = 1000000) as play:
    mixer()

'''

clientSocket.close()