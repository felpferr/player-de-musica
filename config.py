diretorio_default = '/home/aluno/Music'
portaDefault = 12003

def obterDiretorioDeUsuario():
    # Obtém o caminho completo do diretorio usado no compartilhamento
    diretorioPadrao = os.path.expanduser(diretorio_default)
  
    try: os.mkdir(diretorio_default)
    finally: return diretorio_default
