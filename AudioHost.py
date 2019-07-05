#TCP_server
#coding: utf-8

import socket
import threading
import warnings
import config as c
import wave
import time
import os

warnings.filterwarnings('ignore')

serverPort = c.portaDefault
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("Servidor em execução")


#função para verificar a existencia de um arquivo; Nome completo:verifica_existencia_arquivo.
def vea(arq_nome):
        for path , diretorios, arqs_names in os.walk(c.diretorio_default):
                for music_name in arqs_names:
                        if arq_nome == music_name:
                                return True
        
        return False


def conexoes(connectionSocket, addr):  
        
        #Loop usado para manter a conexão caso o usuário queira mais arquivos.
        while True:
                nameMusic = connectionSocket.recv(4096).decode('utf-8')
                if nameMusic == "q":
                        connectionSocket.close()
                        print("Conexão encerrada com {}".format(addr))
                        exit()
                
                if vea(nameMusic+'.wav') == True:
                        musica = wave.open('/home/felipe/Música/{}.wav'.format(nameMusic),'rb')
                        
                        '''
                        Convertendo o valor da taxa de reprodução(rate) que é um inteiro
                        para string para poder enviar pelo socket.
                        '''
                        rate = str(musica.getframerate())
                        
                        #Enviando a taxa de reprodução para o cliente.
                        connectionSocket.send(rate.encode('utf-8'))
                
                        time.sleep(1.5)
                        while musica != '':
                                connectionSocket.send(musica.readframes(4096))    

                        musica.close()
                        #Será usado se não conseguir integrar uma página html.
                        print("Conexão encerrada com {}".format(addr))
                        connectionSocket.close()

                else:
                        falso = "Falso"
                        connectionSocket.send(falso.encode('utf-8'))

def main():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão   vinda   de  {}".format(addr))
        th = threading.Thread(target=conexoes, args=(connectionSocket, addr))
        th.start()
        time.sleep(5)

if __name__ == '__main__':
	main()
