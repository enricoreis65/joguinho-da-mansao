# - CONFIGURAÇÕES PARA OS SONS DO JOGO:

#----------------------------------------------------------------------#
# - Imports:

import pygame
import random
from os import path
from pygame.locals import *

sound_dir = path.join(path.dirname(__file__), 'musicas')
# - Carrega os sons do jogo:
pygame.init()
#pygame.mixer.music.load('')

pygame.mixer.music.load(path.join(sound_dir, 'musica_teste.ogg'))
pygame.mixer.music.set_volume(0.4)

#destroy_sound = pygame.mixer.Sound('')
#pew_sound = pygame.mixer.Sound('')


