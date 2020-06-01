import pygame
import random
from os import path
from medidas import *
from pygame.locals import *
img_dir = path.join(path.dirname(__file__), 'img')

# Imagens
ROGER_IMG = 'roger_imgla_inicial_img'
SHEPPARD_IMG = 'sheppard_img'
CAROLINE_IMG = 'caroline_img'
INIMIGOS_IMG = 'tile2-block.png'
RALPH_IMG = 'ralph_img'
MISS_IMG = 'miss_img'
CHARLES_IMG = 'charles_img'
BLOCK="chao"
PLAY = 'play_img.png'
PLAYAPERTADO = 'playapertado_img.png'
MENU = 'menu_img.png'
MENUAPERTADO = 'menuapertado_img.png'
TELA_INICIAL_IMG = 'tela_inicial_img.png'
TELA_1_IMG = 'tela1.png'
PLAYER_PARADO_IMG = 'parado (2).png'
TESTE_IMG = 'hero-single.png'
BARRA_IMG = 'barra.png'
BARRA_VERMELHA_IMG = 'vida_inimigo.png'
TUTORIAL = 'tutorial.png'


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}

    assets[TELA_INICIAL_IMG] = pygame.image.load(path.join(img_dir, 'tela_inicial_img.png')).convert_alpha()
    # assets[TELA_1_IMG] = pygame.image.load(path.join(img_dir, 'tela1.png')).convert_alpha()
    # assets[ROGER_IMG] = pygame.image.load(path.join(img_dir, 'roger.png')).convert_alpha()
    # assets[SHEPPARD_IMG] = pygame.image.load(path.join(img_dir, 'sheppard.png')).convert_alpha()
    # assets[CAROLINE_IMG] = pygame.image.load(path.join(img_dir, 'caroline.png')).convert_alpha()
    # assets[RALPH_IMG] = pygame.image.load(path.join(img_dir, 'ralph.png')).convert_alpha()
    # assets[MISS_IMG] = pygame.image.load(path.join(img_dir, 'miss.png')).convert_alpha()
    # assets[CHARLES_IMG] = pygame.image.load(path.join(img_dir, 'charles.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[PLAY] = pygame.image.load(path.join(img_dir, 'play_img.png')).convert_alpha()
    assets[PLAYAPERTADO] = pygame.image.load(path.join(img_dir, 'playapertado_img.png')).convert_alpha()
    assets[MENU] = pygame.image.load(path.join(img_dir, 'menu_img.png')).convert_alpha()
    assets[MENUAPERTADO] = pygame.image.load(path.join(img_dir, 'menuapertado_img.png')).convert_alpha()
    assets[TUTORIAL] = pygame.image.load(path.join(img_dir, 'tutorial.png')).convert_alpha()

    # Definindo o player e imagens de teste
    assets[PLAYER_PARADO_IMG] = pygame.image.load(path.join(img_dir, 'parado (2).png')).convert_alpha()
    assets[TESTE_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
    assets[BARRA_IMG] = pygame.image.load(path.join(img_dir, 'barra.png')).convert_alpha()
    assets[BARRA_VERMELHA_IMG] = pygame.image.load(path.join(img_dir, 'vida_inimigo.png')).convert_alpha()
    assets[INIMIGOS_IMG] = pygame.image.load(path.join(img_dir, 'tile-block2.png')).convert_alpha()


    #Escalas das imagens
    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG], (barra_largura, barra_altura))
    assets[BARRA_VERMELHA_IMG]=pygame.transform.scale(assets[BARRA_VERMELHA_IMG], (barra_largura, barra_altura))
    assets[PLAYER_PARADO_IMG] = pygame.transform.scale(assets[PLAYER_PARADO_IMG], (heroi_largura, heroi_altura))
    assets[INIMIGOS_IMG] = pygame.transform.scale(assets[INIMIGOS_IMG], (vilao_largura, vilao_altura))
    assets[TESTE_IMG] = pygame.transform.scale(assets[TESTE_IMG], (heroi_largura, heroi_altura))

    assets[TELA_INICIAL_IMG] = pygame.transform.scale(assets[TELA_INICIAL_IMG],(largura,altura))
    # assets[TELA_1_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[ROGER_IMG] = pygame.transform.scale(assets[ROGER_IMG],(roger_largura, roger_altura))
    # assets[SHEPPARD_IMG] = pygame.transform.scale(assets[SHEPPARD_IMG],(tela_1_largura, tela_1_altura))
    # assets[CAROLINE_IMG] = pygame.transform.scale(assets[CAROLINE_IMG],(caroline_largura, caroline_altura))
    # assets[RALPH_IMG] = pygame.transform.scale(assets[RALPH_IMG],ralph_largura, ralph_altura))
    # assets[MISS_IMG] = pygame.transform.scale(assets[MISS_IMG],(miss_largura, miss_altura))
    # assets[CHARLES_IMG] = pygame.transform.scale(assets[CHARLES_IMG],(charles_largura, charles_altura))
    
    assets[PLAY] = pygame.transform.scale(assets[PLAY],(play_largura, play_altura))
    assets[PLAYAPERTADO] = pygame.transform.scale(assets[PLAYAPERTADO],(playapertado_largura,playapertado_altura))
    assets[MENU] = pygame.transform.scale(assets[MENU],(menu_largura, menu_altura))
    assets[MENUAPERTADO] = pygame.transform.scale(assets[MENUAPERTADO],(menuapertado_largura, menuapertado_altura))
    assets[TUTORIAL] = pygame.transform.scale(assets[TUTORIAL],(largura, altura))
    return assets                        
