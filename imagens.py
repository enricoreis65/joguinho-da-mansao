import pygame
import random
from os import path
from medidas import *
from pygame.locals import *

img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
window = pygame.display.set_mode((largura, altura))
# Imagens
ROGER_IMG = 'roger_imgla_inicial_img'
SHEPPARD_IMG = 'sheppard_img'
CAROLINE_IMG = 'caroline_img'
INIMIGOS_IMG = 'tile2-block.png'
RALPH_IMG = 'ralph_img'
MISS_IMG = 'miss_img'
CHARLES_IMG = 'charles_img'
Chao="chao"
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
GAMEOVER1 = 'gameovercima.png'
GAMEOVER2 = 'gameoverbaixo.png'
SAIR = 'sair.png'
SAIRAPERTADO = 'sairapertado.png'
RESUME = 'resume.png'
RESUMEAPERTADO = 'resumeapertado.png'
Chave1="key1.png"
Chave2="key2.png"
def carrega_spritesheet(spritesheet, linhas, colunas):
    
    sprite_width = spritesheet.get_width() // colunas
    sprite_height = spritesheet.get_height() // linhas
    
    sprites = []
    for linha in range(linhas):
        for coluna in range(colunas):
            x = coluna * sprite_width
            y = linha * sprite_height
            dest_rect = pygame.Rect(x,y,sprite_width,sprite_height) 
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            
            image.blit(spritesheet, (0,0), dest_rect)
            sprites.append(image)
    return sprites

spritesheet_todos = {'existindo':pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_existindoLeft.png')).convert_alpha(), (52*3, 80*2)),
                     'healing': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_healingLeft.png')).convert_alpha(), (52*4, 80*2)),
                     'andandoesq': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_andandoLeft.png')).convert_alpha(), (52*2, 80)), 
                     'atacando': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_atacandoLeft.png')).convert_alpha(), (52*4, 80*4)),
                     #'defendendo': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_defendendoLeft.png')).convert_alpha(), (52*4, 80*2)),
                     # dash': pygame.transform.scale("spritesheet_dashLeft.png")).concert_alpha(), (52*4, 80*2)) ,
                     'dano': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_danoLeft.png')).convert_alpha(), (52*2, 80*2)),
                     "inimigo":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'inimigo_spritesheet.png')).convert_alpha(), (52*5, 80*4)),
                     "pulando":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_pulandoLeft.png')).convert_alpha(), (52*3, 80*2))
}

dicio={}

dicio['existindo']=carrega_spritesheet(spritesheet_todos["existindo"], 2, 3)
dicio['atacando']=carrega_spritesheet(spritesheet_todos['atacando'], 3, 2)
dicio['andandoesq']=carrega_spritesheet(spritesheet_todos['andandoesq'], 1, 2)
dicio['dano']=carrega_spritesheet(spritesheet_todos['dano'], 2, 2)
dicio["inimigo"]=carrega_spritesheet(spritesheet_todos['inimigo'], 4, 5)
dicio["pulando"]=carrega_spritesheet(spritesheet_todos['pulando'], 2, 3)
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
    assets[Chao] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[PLAY] = pygame.image.load(path.join(img_dir, 'play_img.png')).convert_alpha()
    assets[PLAYAPERTADO] = pygame.image.load(path.join(img_dir, 'playapertado_img.png')).convert_alpha()
    assets[MENU] = pygame.image.load(path.join(img_dir, 'menu_img.png')).convert_alpha()
    assets[MENUAPERTADO] = pygame.image.load(path.join(img_dir, 'menuapertado_img.png')).convert_alpha()
    assets[TUTORIAL] = pygame.image.load(path.join(img_dir, 'tutorial.png')).convert_alpha()
    assets[GAMEOVER1] = pygame.image.load(path.join(img_dir, 'gameovercima.png')).convert_alpha()
    assets[GAMEOVER2] = pygame.image.load(path.join(img_dir, 'gameoverbaixo.png')).convert_alpha()
    assets[SAIR] = pygame.image.load(path.join(img_dir, 'sair.png')).convert_alpha()
    assets[SAIRAPERTADO] = pygame.image.load(path.join(img_dir, 'sairapertado.png')).convert_alpha()
    assets[RESUME] = pygame.image.load(path.join(img_dir, 'resume.png')).convert_alpha()
    assets[RESUMEAPERTADO] = pygame.image.load(path.join(img_dir, 'resumeapertado.png')).convert_alpha()
    assets[Chave1] = pygame.image.load(path.join(img_dir, 'key1.png')).convert_alpha()
    assets[Chave2] = pygame.image.load(path.join(img_dir, 'key2.png')).convert_alpha()

    # Definindo o player e imagens de teste:
    #assets[PLAYER_PARADO_IMG] = pygame.image.load(path.join(img_dir, 'parado (2).png')).convert_alpha()
    #assets[TESTE_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
    assets[BARRA_IMG] = pygame.image.load(path.join(img_dir, 'barra.png')).convert_alpha()
    assets[BARRA_VERMELHA_IMG] = pygame.image.load(path.join(img_dir, 'vida_inimigo.png')).convert_alpha()
    assets[INIMIGOS_IMG] = pygame.image.load(path.join(img_dir, 'inimigo_spritesheet.png')).convert_alpha()

    #Escalas imagens
    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG], (barra_largura, barra_altura))
    assets[BARRA_VERMELHA_IMG]=pygame.transform.scale(assets[BARRA_VERMELHA_IMG], (barra_largura, barra_altura))
    #assets[PLAYER_PARADO_IMG] = pygame.transform.scale(assets[PLAYER_PARADO_IMG], (heroi_largura, heroi_altura))
    assets[INIMIGOS_IMG] = pygame.transform.scale(assets[INIMIGOS_IMG], (vilao_largura, vilao_altura))
    #assets[TESTE_IMG] = pygame.transform.scale(assets[TESTE_IMG], (heroi_largura, heroi_altura))
    assets[GAMEOVER1] = pygame.transform.scale(assets[GAMEOVER1], (gameover1_largura, gameover1_altura))
    assets[GAMEOVER2] = pygame.transform.scale(assets[GAMEOVER2], (gameover2_largura, gameover2_altura))
    assets[SAIR] = pygame.transform.scale(assets[SAIR], (sair_largura, sair_altura))
    assets[SAIRAPERTADO] = pygame.transform.scale(assets[SAIRAPERTADO], (sairapertado_largura, sairapertado_altura))
    assets[RESUME] = pygame.transform.scale(assets[RESUME], (resume_largura, resume_altura))
    assets[RESUMEAPERTADO] = pygame.transform.scale(assets[RESUMEAPERTADO], (resumeapertado_largura, resumeapertado_altura))
    assets[Chave1]=pygame.transform.scale(assets[Chave1], (chave_largura, chave_altura))
    assets[Chave2]=pygame.transform.scale(assets[Chave2], (chave_largura, chave_altura))
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
