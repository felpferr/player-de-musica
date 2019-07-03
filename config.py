diretorio_default = '/home/felipe/Música'
portaDefault = 12001

def obterDiretorioDeUsuario():
    # Obtém o caminho completo do diretorio usado no compartilhamento
    diretorioPadrao = os.path.expanduser(diretorio_default)
  
    try: os.mkdir(diretorio_default)
    finally: return diretorio_default
