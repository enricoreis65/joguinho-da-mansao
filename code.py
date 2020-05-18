import pygame, sys
import random
from os import path
from pygame.locals import *

#-----------------Dados iniciais de tamanho
altura = 540
largura = 960
barra_largura=32
barra_altura=3
heroi_largura=52
heroi_altura=80
vilao_largura=52
vilao_altura=52

#----------------Configurações para imagens

# Define a pasta que contem figuras e sons    
img_dir = path.join(path.dirname(__file__), 'img')

# Imagens
ROGER_IMG = 'roger_img'
SHEPPARD_IMG = 'sheppard_img'
CAROLINE_IMG = 'caroline_img'
INIMIGOS_IMG = 'tile-block.png'
RALPH_IMG = 'ralph_img'
MISS_IMG = 'miss_img'
CHARLES_IMG = 'charles_img'
CHAO = 'chao_img'
PLAY = 'play_img.png'
PLAYAPERTADO = 'playapertado_img.png'
MENU = 'menu_img.png'
MENUAPERTADO = 'menuapertado_img.png'
TELA_INICIAL_IMG = 'telainicial.png'
TELA_1_IMG = 'tela1.png'
PLAYER_PARADO_IMG = 'parado (2).png'
TESTE_IMG = 'hero-single.png'
BARRA_IMG = 'barra.png'
BARRA_VERMELHA_IMG = 'vida_inimigo.png'

# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    # assets[TELA_INICIAL_IMG] = pygame.image.load(path.join(img_dir, 'telainicial.png')).convert_alpha()
    # assets[TELA_1_IMG] = pygame.image.load(path.join(img_dir, 'tela1.png')).convert_alpha()
    # assets[ROGER_IMG] = pygame.image.load(path.join(img_dir, 'roger.png')).convert_alpha()
    # assets[SHEPPARD_IMG] = pygame.image.load(path.join(img_dir, 'sheppard.png')).convert_alpha()
    # assets[CAROLINE_IMG] = pygame.image.load(path.join(img_dir, 'caroline.png')).convert_alpha()
    assets[INIMIGOS_IMG] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert_alpha()
    # assets[RALPH_IMG] = pygame.image.load(path.join(img_dir, 'ralph.png')).convert_alpha()
    # assets[MISS_IMG] = pygame.image.load(path.join(img_dir, 'miss.png')).convert_alpha()
    # assets[CHARLES_IMG] = pygame.image.load(path.join(img_dir, 'charles.png')).convert_alpha()
    # assets[CHAO] = pygame.image.load(path.join(img_dir, 'chao.png')).convert_alpha()
    # assets[PLAY] = pygame.image.load(path.join(img_dir, 'play.png')).convert_alpha()
    #assets[PLAYAPERTADO] = pygame.image.load(path.join(img_dir, 'playapertado.png')).convert_alpha()
    # assets[MENU] = pygame.image.load(path.join(img_dir, 'menu.png')).convert_alpha()
    # assets[MENUAPERTADO] = pygame.image.load(path.join(img_dir, 'menuapertado.png')).convert_alpha()
    # Definindo o player e imagens de teste
    assets[PLAYER_PARADO_IMG] = pygame.image.load(path.join(img_dir, 'parado (2).png')).convert_alpha()
    assets[TESTE_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
    assets[BARRA_IMG] = pygame.image.load(path.join(img_dir, 'barra.png')).convert_alpha()
    assets[BARRA_VERMELHA_IMG] = pygame.image.load(path.join(img_dir, 'vida_inimigo.png')).convert_alpha()

    #Escalas das imagens
    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG], (barra_largura, barra_altura))
    assets[BARRA_VERMELHA_IMG]=pygame.transform.scale(assets[BARRA_VERMELHA_IMG], (barra_largura, barra_altura))
    assets[PLAYER_PARADO_IMG] = pygame.transform.scale(assets[PLAYER_PARADO_IMG], (heroi_largura, heroi_altura))
    assets[INIMIGOS_IMG] = pygame.transform.scale(assets[INIMIGOS_IMG], (vilao_largura, vilao_altura))
    assets[TESTE_IMG] = pygame.transform.scale(assets[TESTE_IMG], (heroi_largura, heroi_altura))
    # assets[TELA_INICIAL_IMG] = pygame.transform.scale(assets[TELA_INICIAL_IMG],(telainicial_largura, telainicial_altura))
    # assets[TELA_1_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))

    # assets[ROGER_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[SHEPPARD_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[CAROLINE_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[INIMIGOS_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[RALPH_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[MISS_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[CHARLES_IMG] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[CHAO] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[PLAY] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    # assets[PLAYAPERTADO] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    #assets[MENU] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    #assets[MENUAPERTADO] = pygame.transform.scale(assets[TELA_1_IMG],(tela_1_largura, tela_1_altura))
    return assets                        
#------------------

pygame.init()


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
font = pygame.font.SysFont(None, 40)
text_a = font.render(('ataque'), True, (0, 0, 255))
fullscreen = False

#----------------Configurações para imagens
#MAPA

#------------------

class heroi(pygame.sprite.Sprite):
    def __init__(self,vida,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[PLAYER_PARADO_IMG]
        self.image2 = assets[TESTE_IMG]
        self.image3=assets[PLAYER_PARADO_IMG]
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
                        if player.rect.bottom-inimigo.rect.top<0:
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
                        elif player.rect.left-inimigo.rect.centerx>0:
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



class inimigos(pygame.sprite.Sprite):
    def __init__(self,vida_inimigo,player,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[INIMIGOS_IMG]
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

class adicionais(pygame.sprite.Sprite):
    def __init__(self,img,quem_ta_seguindo,largura):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image2 = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 0
        self.largura=largura
        self.largura2=largura
        self.quem_ta_seguindo=quem_ta_seguindo

    def update(self):
        if self.quem_ta_seguindo==player:
            self.rect.centerx = self.quem_ta_seguindo.rect.centerx
            self.rect.bottom = self.quem_ta_seguindo.rect.bottom-heroi_altura-2
            if self.quem_ta_seguindo.estado==ataque:
                if self.largura!=0:
                    self.largura-=1
                    self.largura2=0
                    self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))
            if self.quem_ta_seguindo.estado==indefeso:
                if self.largura2!=32:
                    self.largura2=32
                    self.largura=32
                    self.image=pygame.transform.scale(self.image2, (self.largura2, barra_altura))
        if self.quem_ta_seguindo==inimigo:
            self.rect.centerx = self.quem_ta_seguindo.rect.centerx
            self.rect.bottom = self.quem_ta_seguindo.rect.bottom-heroi_altura-2
    def diminuir(self):
        if self.quem_ta_seguindo==inimigo:
            if self.largura>0:
                self.largura-=6
                self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))

# class vida_verm(pygame.sprite.Sprite):
#     def __init__(self,img,inimigo):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = img
#         self.rect = self.image.get_rect()
#         self.rect.centerx = 0
#         self.rect.bottom = 0
#         self.largura=30
    
#     def update(self):
#         self.rect.centerx = inimigo.rect.centerx
#         self.rect.bottom = inimigo.rect.bottom-heroi_altura-2
#     def diminuir(self):
#         if self.largura>0:
#             self.largura-=6
#             self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))
        
        
# ----- Inicia estruturas de dados
clock = pygame.time.Clock()
vida=100
vida_inimigo=50
FPS = 60
all_sprites = pygame.sprite.Group()
all_enemis = pygame.sprite.Group()
assets = load_assets(img_dir)
player= heroi(vida,assets)
estado_do_jogo= modo_de_jogo(player)
inimigo= inimigos(vida_inimigo,player,assets)
barra= adicionais(assets[BARRA_IMG],player,barra_largura)
barra_vermelha= adicionais(assets[BARRA_VERMELHA_IMG],inimigo,barra_largura)
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