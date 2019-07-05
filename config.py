diretorio_default = '/home/felipe/Música'
portaDefault = 12001
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z']

def obterDiretorioDeUsuario():
    # Obtém o caminho completo do diretorio usado no compartilhamento.
    diretorioPadrao = os.path.expanduser(diretorio_default)
  
    try: os.mkdir(diretorio_default)
    finally: return diretorio_default

def generateList(conSok):
        List = open('lista.txt','w')
        for path , diretorios, arqs_names in os.walk(c.diretorio_default):
                for i in arqs_names:
                        List.write(i+'\n')
        List.close()
        List = open('lista.txt','rb')
        for linha in List:
                conSok.send(linha)
        List.close()
