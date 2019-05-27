#TCP_server

import socket
import threading

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("The server is ready to receive")

def conexoes(connectionSocket, addr):
    
    nameMusic = connectionSocket.recv(2048)
    musica = open('/home/felipe/Documentos/musicas/-{}'.format(nameMusic.decode('utf-8')), 'wb'),
    while musica != 'EOF':
        aux.write(musica)
        connectionSocket.send(aux.encode('utf-8'))
        
    nameMusic.close()
    connectionSocket.close()

def main():
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão vinda de {}".format(addr))
        th = threading.Thread(target=conexoes, args=(connectionSocket, addr))
        th.start()

if __name__ == '__main__':
	main()