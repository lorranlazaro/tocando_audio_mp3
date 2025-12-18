import pygame
import os
import time
import emoji

pygame.mixer.init()

diretorio_script = os.path.dirname(__file__)
caminho_audio = os.path.join(diretorio_script, 'assets', 'labirinto_de_amor.mp3')

caminho_audio = os.path.abspath(caminho_audio)
print(f"Procurando arquivo em: {caminho_audio}")

if os.path.exists(caminho_audio):
    print(emoji.emojize(f":check_mark:  Arquivo encontrado! Carregando...: {caminho_audio}"))
    
    pygame.mixer.music.load(caminho_audio)
    
    pygame.mixer.music.play(loops=-1)
    
    print("Reproduzindo áudio...")
    print("Pressione Ctrl+C para parar")
  
    try:
        while pygame.mixer.music.get_busy():
            time.sleep(0.1) 
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nReprodução interrompida!")
    
    print("Reprodução finalizada!")
else:
    print(f"Erro: Arquivo não encontrado em {caminho_audio}")