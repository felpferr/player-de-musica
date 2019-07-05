#TCPclient
#coding: utf-8

import socket
import config as c
import threading
import pyaudio
import keyboard
from player import streamming
import warnings

warnings.filterwarnings('ignore')

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
            

#Função para tocar a música.
def player():
        '''
        Recebendo a taxa de reprodução do servidor caso a música exista;
        
        O objeto Rate terá outra função que será armazenar uma resposta falso 
        caso não haja uma música desejada, iniciando uma sub-tarefa voltando à tela
        inicial.
        '''
        Rate = clientSocket.recv(1024).decode('utf-8')
        
        if Rate == "Falso":
                print('Música não encontrada!\n')
                FP()
                exit()
        playback = streamming(Rate)
        playback.play(clientSocket)
        clientSocket.close()

#FP = função de execução principal
def FP():
    audioName = input("Forneça uma música ou pressione q para sair:\n")
    
    clientSocket.send(audioName.encode('utf-8'))

    if audioName == "q":
            clientSocket.shutdown(1)
            clientSocket.close()
    else:
        player()

    clientSocket.close()

if __name__ == '__main__':
	FP()
