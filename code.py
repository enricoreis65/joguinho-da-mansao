import pygame, sys
import random
from os import path
from pygame.locals import *

#----------------Configurações para imagens

# Define a pasta que contem figuras e sons    
img_dir = path.join(path.dirname(__file__), 'img')

# Imagens
PLAYER_IMG = 'player_img'
ROGER_IMG = 'roger_img'
SHEPPARD_IMG = 'sheppard_img'
CAROLINE_IMG = 'caroline_img'
FANTASMA_IMG = 'fantasma_img'
RALPH_IMG = 'ralph_img'
MISS_IMG = 'miss_img'
CHARLES_IMG = 'charles_img'
CHAO_IMG = 'chao_img'
PLAY_IMG = 'play_img'
PLAYAPERTADO_IMG = 'playapertado_img'
MENU_IMG = 'menu_img'
MENUAPERTADO_IMG = 'menuapertado_img'

#------------------

pygame.init()

#-----------------Dados iniciais de tamanho
altura = 540
largura = 960
barra_largura=32
barra_altura=3
heroi_largura=52
heroi_altura=80
vilao_largura=52
vilao_altura=52

#---- Dados movimento
espera = "espera"
pulando = "pulando"
caindo = "caindo"
gravidade=2
chao = altura * 5 // 6
tamanho_do_pulo=20
indefeso = "indefeso"
ataque = "ataque"
tomando_dano="tomando_dano"

# ----- Gera tela principal
#monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
window = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption('mansao')
font = pygame.font.SysFont("joguinho-da-mansao\fonts\VCR_OSD_MONO_1.001.ttf", 40)
text_a = font.render(('ataque'), True, (0, 0, 255))
fullscreen = False

# Definindo o player
barra_img=pygame.image.load(path.join(img_dir, 'barra.png')).convert_alpha()
barra_img=pygame.transform.scale(barra_img, (barra_largura, barra_altura))
barra_vermelha_img=pygame.image.load(path.join(img_dir, 'vida_inimigo.png')).convert_alpha()
barra_vermelha_img=pygame.transform.scale(barra_vermelha_img, (barra_largura, barra_altura))
player_img = pygame.image.load(path.join(img_dir, 'parado (2).png')).convert_alpha()
player_img = pygame.transform.scale(player_img, (heroi_largura, heroi_altura))
inimigos_img=pygame.image.load(path.join(img_dir, 'tile-block.png')).convert_alpha()
inimigos_img = pygame.transform.scale(inimigos_img, (vilao_largura, vilao_altura))
teste_img = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
teste_img = pygame.transform.scale(teste_img, (heroi_largura, heroi_altura))

#----------------Configurações para imagens
#MAPA

#------------------

class heroi(pygame.sprite.Sprite):
    def __init__(self,img,vida,teste_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image2=teste_img
        self.image3=img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = chao
        self.speedx = 0
        self.speedy= 0
        self.estado = indefeso
        self.vida=vida
        self.hora_do_ataque=pygame.time.get_ticks()
        self.porrada_ticks = 850
        self.dano_ticks=2000
        self.hora_do_dano=pygame.time.get_ticks()
    #update    
    def update(self):
        # Atualização da posição do heroi
        self.rect.x += self.speedx
        if self.hora_do_ataque+self.porrada_ticks<agora:
                self.estado=indefeso
                self.image=self.image3
        
        self.speedy += gravidade
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = caindo
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > chao:
            # Reposiciona para a posição do chão
            self.rect.bottom = chao

            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = espera

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

    def pulo(self):
        if self.state == espera:
            self.speedy -= tamanho_do_pulo
            self.state = pulando

    def ataque(self):
        if self.state==espera:
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = agora - self.hora_do_ataque

        # Se já pode atirar novamente...
            
            if elapsed_ticks > self.porrada_ticks*1.5:
            # Marca o tick da nova imagem.
                self.hora_do_ataque = agora
                if self.estado == indefeso:
                    self.image=self.image2
                    self.estado = ataque

    def dano(self):
        if estado_do_jogo.aba=="jogando":
            if player.vida<=0:
                player.kill()
                barra.kill()
                
            else:
                if player.estado==indefeso:
                    colisao=pygame.sprite.spritecollide(player,all_enemis,False,pygame.sprite.collide_mask)
                
                    if len(colisao)>0:
                        if player.rect.bottom-inimigo.rect.centerx<0:
                            player.hora_do_dano=pygame.time.get_ticks()
                            player.estado=tomando_dano
                            player.vida-=10                       
                            player.rect.x-=90
                            player.rect.y-=tamanho_do_pulo*3

                        elif player.rect.right-inimigo.rect.centerx<0:
                            player.hora_do_dano=pygame.time.get_ticks()
                            player.estado=tomando_dano
                            player.vida-=10                       
                            player.rect.x-=60
                            player.rect.y-=tamanho_do_pulo
                        elif player.rect.left-inimigo.rect.centerx>=0:
                            player.hora_do_dano=pygame.time.get_ticks()
                            player.estado=tomando_dano
                            player.vida-=10                       
                            player.rect.x+=60
                            player.rect.y-=tamanho_do_pulo
            
                if player.estado==ataque:
                    colisao=pygame.sprite.spritecollide(player,all_enemis,False,pygame.sprite.collide_mask)   
                    if len(colisao)>0:
                        inimigo.estado=tomando_dano
                        colisao.clear()
                        inimigo.dano()
                        player.estado=espera
                        barra_vermelha.diminuir()

#----------------Configurações para imagens
# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'player.png')).convert_alpha()
    assets[ROGER_IMG] = pygame.image.load(path.join(img_dir, 'roger.png')).convert_alpha()
    assets[SHEPPARD_IMG] = pygame.image.load(path.join(img_dir, 'sheppard.png')).convert_alpha()
    assets[CAROLINE_IMG] = pygame.image.load(path.join(img_dir, 'caroline.png')).convert_alpha()
    assets[FANTASMA_IMG] = pygame.image.load(path.join(img_dir, 'fantasma.png')).convert_alpha()
    assets[RALPH_IMG] = pygame.image.load(path.join(img_dir, 'ralph.png')).convert_alpha()
    assets[MISS_IMG] = pygame.image.load(path.join(img_dir, 'miss.png')).convert_alpha()
    assets[CHARLES_IMG] = pygame.image.load(path.join(img_dir, 'charles.png')).convert_alpha()
    assets[CHAO] = pygame.image.load(path.join(img_dir, 'chao.png')).convert_alpha()
    assets[PLAY] = pygame.image.load(path.join(img_dir, 'play.png')).convert_alpha()
    assets[PLAYAPERTADO] = pygame.image.load(path.join(img_dir, 'playapertado.png')).convert_alpha()
    assets[MENU] = pygame.image.load(path.join(img_dir, 'menu.png')).convert_alpha()
    assets[MENUAPERTADO] = pygame.image.load(path.join(img_dir, 'menuapertado.png')).convert_alpha()

    return assets                        
      
#------------------

class inimigos(pygame.sprite.Sprite):
    def __init__(self,img,player,vida_inimigo):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura-300
        self.rect.bottom = chao
        self.speedx_inimigo = 0
        self.speedy_inimigo= 0
        self.vida=vida_inimigo
        self.estado=espera
    def update(self):
        if self.estado==espera:
            self.rect.x += self.speedx_inimigo
            self.rect.y += self.speedy_inimigo
        elif player.hora_do_ataque+player.porrada_ticks*0.3<agora:
            self.estado=espera
        if player.rect.x-self.rect.x>0 :
            self.speedx_inimigo = 1
            
        if player.rect.x-self.rect.x<0 :
            self.speedx_inimigo = -1

        if self.rect.bottom > chao:
            # Reposiciona para a posição do chão
            self.rect.bottom = chao
        
        if player.rect.y-self.rect.y>0 :
            self.rect.y != altura -chao
            self.speedy_inimigo = 1 

        if player.rect.y-self.rect.y<0 :
            self.speedy_inimigo = -1
    def dano(self):
        inimigo.vida-=10
        if player.rect.right-inimigo.rect.centerx<0:
            inimigo.rect.x+=40
            inimigo.rect.y-=20             
        elif player.rect.left-inimigo.rect.centerx>=0:    
            inimigo.rect.x-=40
            inimigo.rect.y-=20                   
        if inimigo.vida==0:
            inimigo.kill()
            barra_vermelha.kill()
        
        

class modo_de_jogo():
    def __init__(self,player):
        self.aba="menu"
        
    def jogando(self):
        text = font.render(('{0}'.format(player.vida)), True, (0, 0, 255))
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit() 
        # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True 
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player.speedx -= 4
                if event.key == pygame.K_d:                  
                    player.speedx += 4
                if event.key == pygame.K_SPACE:
                    player.pulo()
                if event.key == pygame.K_ESCAPE:
                    self.aba = 'main menu'
        # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
            # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_a:   
                        player.speedx += 4
                    if event.key == pygame.K_d:
                        player.speedx -= 4
        # Verifica se apertou o botão do mouse.
            if event.type == pygame.MOUSEBUTTONDOWN:    
                player.ataque()
            # if event.type == VIDEORESIZE:
            #     window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
     
    # ----- Gera saídas
        window.fill((0, 0, 50))  # Preenche com a cor azul
        all_sprites.draw(window)
        window.blit(text,(10,10))
        player.dano()
                
        all_sprites.update()
        
    # ----- Atualiza estado do jogo
        pygame.display.update()   



    def menu(self):
        text = font.render('Aperte P para jogar', True, (0, 0, 255)) 
        text_rect=text.get_rect()
        text_largura=text_rect.width
        text_altura=text_rect.height
        
        for event in pygame.event.get():
            
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key==pygame.K_p:
                    self.aba="jogando"
        window.fill((255, 255, 255))
        window.blit(text,((largura/2)-text_largura/2,(altura/2)-text_altura/2))
        pygame.display.update() 
    
    # Criando um Menu de Pausa no meio do jogo
    click = False

    def main_menu(self):
        text = font.render('Aperte Esc para voltar e X para sair', True, (255, 255, 255))
        text_rect=text.get_rect()
        text_largura=text_rect.width
        text_altura=text_rect.height
        
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.aba = 'jogando'
                elif event.key == pygame.K_x:
                    pygame.quit()   
            if event.type == pygame.QUIT:
                pygame.quit() 
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        window.fill((0, 0, 50))
        window.blit(text,((largura/2)-text_largura/2,(altura/2)-text_altura/2))
        pygame.display.update() 


    def controlador_menu(self):
        if self.aba=="menu":
            self.menu()
        if self.aba=="jogando":
            self.jogando()
        if self.aba=='main menu':
            self.main_menu()

class stamina(pygame.sprite.Sprite):
    def __init__(self,img,player,largura):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image2 = img

        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 0
        self.largura=largura
        self.largura2=largura

    def update(self):
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.bottom-heroi_altura-2
        if player.estado==ataque:
            if self.largura!=0:
                self.largura-=1
                self.largura2=0
                self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))
        if player.estado==indefeso:
            if self.largura2!=32:
                self.largura2=32
                self.largura=32
                self.image=pygame.transform.scale(self.image2, (self.largura2, barra_altura))

class vida_verm(pygame.sprite.Sprite):
    def __init__(self,img,inimigo):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 0
        self.largura=30
    
    def update(self):
        self.rect.centerx = inimigo.rect.centerx
        self.rect.bottom = inimigo.rect.bottom-heroi_altura-2
    def diminuir(self):
        if self.largura>0:
            self.largura-=6
            self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))
        
        
# ----- Inicia estruturas de dados
clock = pygame.time.Clock()
vida=100
vida_inimigo=50
FPS = 60
all_sprites = pygame.sprite.Group()
all_enemis = pygame.sprite.Group()

player= heroi(player_img,vida,teste_img)
estado_do_jogo= modo_de_jogo(player)
inimigo= inimigos(inimigos_img,player,vida_inimigo)
barra= stamina(barra_img,player,barra_largura)
barra_vermelha=vida_verm(barra_vermelha_img,inimigo)
all_sprites.add(player)
all_sprites.add(barra)
all_sprites.add(barra_vermelha)
all_sprites.add(inimigo)
all_enemis.add(inimigo)
keys_down = {}
game=True

agora=pygame.time.get_ticks()

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    estado_do_jogo.controlador_menu()
    agora=pygame.time.get_ticks() 
    
    
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         pygame.quit()
    #         sys.exit()
        
    #     if event.type == VIDEORESIZE:
    #         if not fullscreen:
    #             screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    #     if event.type == KEYDOWN:
    #         if event.key == K_f:
    #             fullscreen = not fullscreen
    #             if fullscreen:
    #                 screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
    #             else:
    #                 screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)