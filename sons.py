# - CONFIGURAÇÕES PARA OS SONS DO JOGO:

#----------------------------------------------------------------------#
# - Imports:

import pygame
import random
from os import path
from pygame.locals import *

#- Inicialização:
sound_dir = path.join(path.dirname(__file__), 'musicas')
pygame.init()

pygame.mixer.music.load(path.join(sound_dir, 'code.ogg'))
pygame.mixer.music.set_volume(0.4)

# - Carrega os sons do jogo:
pulosond = pygame.mixer.Sound(path.join(sound_dir, 'pulo.wav'))
cortandoar=pygame.mixer.Sound(path.join(sound_dir, 'aircut.wav'))
inimigo_acerto=pygame.mixer.Sound(path.join(sound_dir, 'inimigodano.wav'))
danoplayer=pygame.mixer.Sound(path.join(sound_dir, 'danoplayer.wav'))
andando=pygame.mixer.Sound(path.join(sound_dir, 'andando.wav'))
pegando_item=pygame.mixer.Sound(path.join(sound_dir, 'pegando_item.wav'))
defendendosound=pygame.mixer.Sound(path.join(sound_dir, 'defendendo.wav'))
dashsound=pygame.mixer.Sound(path.join(sound_dir, 'dash.ogg'))
chavesound=pygame.mixer.Sound(path.join(sound_dir, 'chave.wav'))
fantasmasound=pygame.mixer.Sound(path.join(sound_dir, 'fantasmasound.ogg'))
gameoversound=pygame.mixer.Sound(path.join(sound_dir, 'gameovers.wav'))
tomandocafe=pygame.mixer.Sound(path.join(sound_dir, 'tomandocafe.wav'))