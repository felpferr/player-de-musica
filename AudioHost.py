#TCP_server

import socket
import threading
import os
import warnings
import config as c

warnings.filterwarnings('ignore')

serverPort = 12002
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("The server is ready to receive")


#função para verificar a existencia de um arquivo; Nome completo:verifica_existencia_arquivo.
def vea(arq_nome):
        for path , diretorios, arqs_names in os.walk(c.diretorio_default):
                for music_name in arqs_names:
                        if arq_nome == music_name:
                                return True
        
        return False

def conexoes(connectionSocket, addr): 
        ''' 
        Loop usado para manter a conexão caso o usuário queira mais arquivos.
        '''
        while True:
                nameMusic = connectionSocket.recv(4096)
                nameMusic = nameMusic.decode('utf-8')

                if nameMusic == "Sair":
                        connectionSocket.close()
                
                resposta = vea(nameMusic)
                print(resposta)

                if resposta == True:
                        musica = open('/home/felipe/Música/{}'.format(nameMusic), 'rb')
                        print(type(musica))
                        '''
                        Enviando cada linha do arquivo para o cliente.
                        Neste for a variável campos é iterada com o resultado de .readlines(), ou seja, este for será
                        executado até que cada linha do arquivo seja lida.
                        '''
                        for linha in musica:
                                #print(linha)
                                connectionSocket.send(linha)    

                        musica.close()
                        #Será usado se não conseguir integrar uma página html.
                        connectionSocket.close() 
                else:
                        falso = "Falso"
                        connectionSocket.send(falso.encode('utf-8'))

                break
                
                

def main():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão vinda de {}".format(addr))
        th = threading.Thread(target=conexoes, args=(connectionSocket, addr))
        th.start()

if __name__ == '__main__':
	main()
