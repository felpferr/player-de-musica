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

#Função para tocar a música.
def play():
    musica = open('audio.mp3','wb')
    while True:
        audio = clientSocket.recv(2048)
        #print(audio)
        if not audio: 
            break   
        musica.write(audio)

        pg.mixer.init()
        if musica.__sizeof__() >= 4096:
            pg.mixer.music.load(musica)
            pg.mixer.music.play()	


#FP = função de execução principal
def FP():

    audioName = input("Forneça uma música:\n")
            
    clientSocket.send(audioName.encode('utf-8'))
    #buffer = open('audio.mp3','wb')

    '''
    while True:

        #Recebendo o arquivo neste loop.
        while True:
            audio = clientSocket.recv(2048)
            #print(audio)
            if not audio: 
                break   
            buffer.write(audio)
        break
    '''
    th = threading.Thread(target=play)
    th.start()

    clientSocket.close()
    


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

if __name__ == '__main__':
	FP()
