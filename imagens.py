# - CONFIGURAÇÕES PARA AS IMAGENS DO JOGO:

#----------------------------------------------------------------------#
# - Imports:

import pygame
import random
from os import path
from medidas import *
from pygame.locals import *

#----------------------------------------------------------------------#

img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
window = pygame.display.set_mode((largura, altura))

#----------------------------------------------------------------------#
# - Imagens:

#PERSONAGENS:
PLAYER_PARADO_IMG = 'parado (2).png'
ROGER_IMG = 'roger_imgla_inicial_img'
SHEPPARD_IMG = 'sheppard_img'
CAROLINE_IMG = 'caroline_img'
INIMIGOS_IMG = 'tile2-block.png'
RALPH_IMG = 'ralph_img'
MISS_IMG = 'miss_img'
CHARLES_IMG = 'charles_img'

BARRA_IMG = 'barra.png'
BARRA_VERMELHA_IMG = 'vida_inimigo.png'

# CENÁRIOS/TELA:
Chao="chao"
TELA_INICIAL_IMG = 'tela_inicial_img.png'
TELA_1_IMG = 'tela1.png'
TUTORIAL = 'tutorial.png'
GAMEOVER1 = 'gameovercima.png'
GAMEOVER2 = 'gameoverbaixo.png'
xicara="xicara"
PLATAa="plageral"
PLATMm="plameio"
PLATEe="plaesq"
PLATDd="pladir"

#BOTÕES:
PLAY = 'play_img.png'
PLAYAPERTADO = 'playapertado_img.png'
MENU = 'menu_img.png'
MENUAPERTADO = 'menuapertado_img.png'
SAIR = 'sair.png'
SAIRAPERTADO = 'sairapertado.png'
RESUME = 'resume.png'
RESUMEAPERTADO = 'resumeapertado.png'

# CHAVES E PISTAS:
Chave1="key1.png"
Chave2="key2.png"
Chave3 = "key3.png"
PAREDE='parede.png'
CARTA = 'carta.png'
CARTA_ABERTA= 'carta_aberta.png'
PEGADAS = 'pegadas.png'
ANEL = 'anel.png'
PEGADASg = 'pegadasgrandes'


#----------------------------------------------------------------------#
# - Spritesheet:

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

spritesheet_todos = {'existindoesq':pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_existindoLeft.png')).convert_alpha(), (52*3, 80*2)),
                    'existindodir':pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_existindoRight.png')).convert_alpha(), (52*3, 80*2)),
                     'helandoesq': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_healingLeft.png')).convert_alpha(), (52*4, 80*2)),
                     'andandoesq': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_andandoLeft.png')).convert_alpha(), (52*2, 80)),
                      'andandodir': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_andandoRight.png')).convert_alpha(), (52*2, 80)),
                     'atacandodir': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_atacandoRight.png')).convert_alpha(), (80,80*2)),  
                     'atacandoesq': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_atacandoLeft.png')).convert_alpha(), (80, 160)),
                     #'defendendo': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_defendendoLeft.png')).convert_alpha(), (52*4, 80*2)),
                     # dash': pygame.transform.scale("spritesheet_dashLeft.png")).concert_alpha(), (52*4, 80*2)) ,
                     'danoesq': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_danoLeft.png')).convert_alpha(), (52*2, 80*2)),
                     'danodir': pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_danoRight.png')).convert_alpha(), (52*2, 80*2)),
                     "inimigo":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'inimigo_spritesheet.png')).convert_alpha(), (52*5, 80*4)),
                     "pulandoesq":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_pulandoLeft.png')).convert_alpha(), (52*3, 80*2)),
                     'xicara':pygame.transform.scale(pygame.image.load(path.join(img_dir, 'xicara_healing.png')).convert_alpha(), (largura_xicara*20, altura_xicara*20)),
                     "pulandodir":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_pulandoRight.png')).convert_alpha(), (52*3, 80*2)),
                     "xicrinha":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'xicrinha.png')).convert_alpha(), (largura_xicara*10, altura_xicara*10)),
                     "helandodir":pygame.transform.scale(pygame.image.load(path.join(img_dir, 'spritesheet_healingRight.png')).convert_alpha(), (52*4, 80*2))
}

dicio={}

dicio['existindoesq']=carrega_spritesheet(spritesheet_todos["existindoesq"], 2, 3)
dicio['existindodir']=carrega_spritesheet(spritesheet_todos["existindodir"], 2, 3)
dicio['atacandodir']=carrega_spritesheet(spritesheet_todos["atacandodir"], 2, 1)
dicio['atacandoesq']=carrega_spritesheet(spritesheet_todos['atacandoesq'], 2, 1)
dicio['andandoesq']=carrega_spritesheet(spritesheet_todos['andandoesq'], 1, 2)
dicio['andandodir']=carrega_spritesheet(spritesheet_todos['andandodir'], 1, 2)
dicio['danoesq']=carrega_spritesheet(spritesheet_todos['danodir'], 2, 2)
dicio['danodir']=carrega_spritesheet(spritesheet_todos['danoesq'], 2, 2)
dicio["inimigo"]=carrega_spritesheet(spritesheet_todos['inimigo'], 4, 5)
dicio["pulandoesq"]=carrega_spritesheet(spritesheet_todos['pulandoesq'], 2, 3)
dicio["pulandodir"]=carrega_spritesheet(spritesheet_todos['pulandodir'], 2, 3)
dicio['existindoesq']=carrega_spritesheet(spritesheet_todos["existindoesq"], 2, 3)
dicio['xicara']=carrega_spritesheet(spritesheet_todos["xicara"], 4, 3)
dicio['xicrinha']=carrega_spritesheet(spritesheet_todos["xicrinha"], 2, 2)
dicio['helandoesq']=carrega_spritesheet(spritesheet_todos["helandoesq"], 3, 5)
dicio['helandoedir']=carrega_spritesheet(spritesheet_todos["helandodir"], 3, 5)

#----------------------------------------------------------------------#
# - Carrega os assets de uma vez:
def load_assets(img_dir):
    assets = {}

    # - Imagens do cenário e telas:
    assets[TELA_INICIAL_IMG] = pygame.image.load(path.join(img_dir, 'tela_inicial_img.png')).convert_alpha()
    assets[Chao] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
    assets[PLATAa] = pygame.image.load(path.join(img_dir, 'tile-wood.png')).convert()
    assets[PLATMm] = pygame.image.load(path.join(img_dir, 'tile-wood-2.png')).convert()
    assets[PLATEe] = pygame.image.load(path.join(img_dir, 'tile-wood-1.png')).convert()
    assets[PLATDd] = pygame.image.load(path.join(img_dir, 'tile-wood-3.png')).convert()
    assets[PAREDE] = pygame.image.load(path.join(img_dir, 'parede.png')).convert()
    assets[TUTORIAL] = pygame.image.load(path.join(img_dir, 'tutorial.png')).convert_alpha()
    assets[GAMEOVER1] = pygame.image.load(path.join(img_dir, 'gameovercima.png')).convert_alpha()
    assets[GAMEOVER2] = pygame.image.load(path.join(img_dir, 'gameoverbaixo.png')).convert_alpha()
   

    # - Imagens dos botões:
    assets[PLAY] = pygame.image.load(path.join(img_dir, 'play_img.png')).convert_alpha()
    assets[PLAYAPERTADO] = pygame.image.load(path.join(img_dir, 'playapertado_img.png')).convert_alpha()
    assets[MENU] = pygame.image.load(path.join(img_dir, 'menu_img.png')).convert_alpha()
    assets[MENUAPERTADO] = pygame.image.load(path.join(img_dir, 'menuapertado_img.png')).convert_alpha()
    assets[SAIR] = pygame.image.load(path.join(img_dir, 'sair.png')).convert_alpha()
    assets[SAIRAPERTADO] = pygame.image.load(path.join(img_dir, 'sairapertado.png')).convert_alpha()
    assets[RESUME] = pygame.image.load(path.join(img_dir, 'resume.png')).convert_alpha()
    assets[RESUMEAPERTADO] = pygame.image.load(path.join(img_dir, 'resumeapertado.png')).convert_alpha()
    
    # - Imagens das pistas e chaves para passar de nível:
    assets[Chave1] = pygame.image.load(path.join(img_dir, 'key1.png')).convert_alpha()
    assets[Chave2] = pygame.image.load(path.join(img_dir, 'key2.png')).convert_alpha()
    assets[Chave3] = pygame.image.load(path.join(img_dir, 'key3.png')).convert_alpha()
    assets[ANEL] = pygame.image.load(path.join(img_dir, 'anel.png')).convert_alpha()
    assets[CARTA] = pygame.image.load(path.join(img_dir, 'carta.png')).convert_alpha()
    assets[CARTA_ABERTA] = pygame.image.load(path.join(img_dir, 'carta_aberta.png')).convert_alpha()
    assets[PEGADAS] = pygame.image.load(path.join(img_dir, 'pegadas.png')).convert_alpha()
    assets[PEGADASg] = pygame.image.load(path.join(img_dir, 'pegadas.png')).convert_alpha()
    # Definindo o player e imagens de teste:
    
    assets[BARRA_IMG] = pygame.image.load(path.join(img_dir, 'barra.png')).convert_alpha()
    assets[BARRA_VERMELHA_IMG] = pygame.image.load(path.join(img_dir, 'vida_inimigo.png')).convert_alpha()
    assets[INIMIGOS_IMG] = pygame.image.load(path.join(img_dir, 'inimigo_spritesheet.png')).convert_alpha()

   


    #----------------------------------------------------------------------#
    # - Escalas das imagens:

    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG], (barra_largura, barra_altura))
    assets[BARRA_VERMELHA_IMG]=pygame.transform.scale(assets[BARRA_VERMELHA_IMG], (barra_largura, barra_altura))
    
    assets[INIMIGOS_IMG] = pygame.transform.scale(assets[INIMIGOS_IMG], (vilao_largura, vilao_altura))
   
    # - Imagens do cenário e telas:
    assets[GAMEOVER1] = pygame.transform.scale(assets[GAMEOVER1], (gameover1_largura, gameover1_altura))
    assets[GAMEOVER2] = pygame.transform.scale(assets[GAMEOVER2], (gameover2_largura, gameover2_altura))
    assets[TELA_INICIAL_IMG] = pygame.transform.scale(assets[TELA_INICIAL_IMG],(largura,altura))
    
    

    # - Imagens dos botões:
    assets[PLAY] = pygame.transform.scale(assets[PLAY],(play_largura, play_altura))
    assets[PLAYAPERTADO] = pygame.transform.scale(assets[PLAYAPERTADO],(playapertado_largura,playapertado_altura))
    assets[MENU] = pygame.transform.scale(assets[MENU],(menu_largura, menu_altura))
    assets[MENUAPERTADO] = pygame.transform.scale(assets[MENUAPERTADO],(menuapertado_largura, menuapertado_altura))
    assets[TUTORIAL] = pygame.transform.scale(assets[TUTORIAL],(largura, altura))
    assets[SAIR] = pygame.transform.scale(assets[SAIR], (sair_largura, sair_altura))
    assets[SAIRAPERTADO] = pygame.transform.scale(assets[SAIRAPERTADO], (sairapertado_largura, sairapertado_altura))
    assets[RESUME] = pygame.transform.scale(assets[RESUME], (resume_largura, resume_altura))
    assets[RESUMEAPERTADO] = pygame.transform.scale(assets[RESUMEAPERTADO], (resumeapertado_largura, resumeapertado_altura))

    # - Imagens das pistas e chaves para passar de nível:
    assets[CARTA] = pygame.transform.scale(assets[CARTA],(carta_largura, carta_altura))
    assets[CARTA_ABERTA] = pygame.transform.scale(assets[CARTA_ABERTA],(carta_aberta_largura,carta_aberta_altura))
    assets[PEGADAS] = pygame.transform.scale(assets[PEGADAS],(pegadas_largura,pegadas_altura))
    assets[PEGADASg] = pygame.transform.scale(assets[PEGADASg],(largura,altura))
    assets[ANEL] = pygame.transform.scale(assets[ANEL],(anel_largura,anel_altura))
    assets[Chave1]=pygame.transform.scale(assets[Chave1], (chave_largura, chave_altura))
    assets[Chave2]=pygame.transform.scale(assets[Chave2], (chave_largura, chave_altura))
    assets[Chave3]=pygame.transform.scale(assets[Chave3], (chave_largura, chave_altura))
    
    return assets                        
