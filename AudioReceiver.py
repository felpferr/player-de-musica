#TCPclient
#coding: utf-8

import socket
import config as c
import threading
import pyaudio
from pydub import AudioSegment

serverName = '127.0.0.1'
serverPort = c.portaDefault

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


#Função para tocar a música.
def play():
        buffer = pyaudio.PyAudio()
        
        '''
        Recebendo a taxa de reprodução do servidor caso a música exista;
        O objeto Rate terá outra função que será armazenar uma resposta falso 
        caso não haja uma música desejada, iniciando uma sub-tarefa voltando à tela
        inicial.
        '''
        Rate = clientSocket.recv(1024).decode('utf-8')
        
        #if Rate == "Falso":
        #        FP()
                

        stream = buffer.open(format=pyaudio.paInt32, channels=1, 
        rate=int(Rate), frames_per_buffer=4096, output=True)
        stream.start_stream()
        
        #Neste loop são adquidos pacotes que são reproduzidos pela stream de áudio
        while True:
                audio = clientSocket.recv(4096)
                stream.write(audio)
                if not audio:
                    break
                
        stream.stop_stream()
        stream.close()
        buffer.terminate()
        clientSocket.close()


#FP = função de execução principal
def FP():
    audioName = input("Forneça uma música:\n")
    
    clientSocket.send(audioName.encode('utf-8'))

    if audioName == "Sair":
            clientSocket.shutdown(1)
            clientSocket.close()
    else:
        play()

    clientSocket.close()

if __name__ == '__main__':
	FP()
