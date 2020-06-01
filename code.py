import pygame, sys
import random
from os import path
from pygame.locals import *
from mapa import BLOCK,EMPTY,MAP1,MAP2,Tile
from imagens import *
from medidas import *
from fases import *
#----------------Configurações para imagens

# Define a pasta que contem figuras e sons    
img_dir = path.join(path.dirname(__file__), 'img')

pygame.init()


#---- Dados movimento
espera = "espera"
pulando = "pulando"
caindo = "caindo"
gravidade = 2

tamanho_do_pulo = 25
indefeso = "indefeso"
ataque = "ataque"
tomando_dano="tomando_dano"
defendendo="defendendo"
pronto_para_acao="pronto_para_acao"
dash="dash"
# ----- Gera tela principal
#monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fenrly Park')
font = pygame.font.Font(path.join("fonts", 'Minecraft.ttf'), 16)

fullscreen = False

#----------------Configurações para imagens
# MAPA

# SPRITESHEET
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

#------------------
class heroi(pygame.sprite.Sprite):
    def __init__(self,vida,player_sheet,blocks):
        pygame.sprite.Sprite.__init__(self)
        player_sheet = pygame.transform.scale(player_sheet, (52*4, 80*2))
        spritesheet = carrega_spritesheet(player_sheet, 2, 3)
        self.blocks=blocks
        self.animations = {
            indefeso: spritesheet[0:4],
            ataque: spritesheet[0:1],
            defendendo: spritesheet[0:1],
            tomando_dano: spritesheet[0:1],
            dash: spritesheet[0:1]
            }
        
        self.estado = indefeso
        self.animation = self.animations[self.estado]
        self.frame = 0
        self.image = self.animation[self.frame]

        self.state = espera
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = 12*48
        self.speedx = 0
        self.speedy= 0
        
        self.vida=vida
        self.quantdash=3
        
        self.acao_ticks = 300*2
        self.frame_ticks = 300
        self.last_update = pygame.time.get_ticks()

        self.hora_do_dano=pygame.time.get_ticks()
        self.hora_da_acao=pygame.time.get_ticks()
        
    # Update    
    def update(self):
        
        now = pygame.time.get_ticks()
        elapsed2_ticks = now - self.last_update

        if elapsed2_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            self.animation = self.animations[self.estado]

            if self.frame >= len(self.animation):
                self.frame = 0
   
            center = self.rect.center
            self.image = self.animation[self.frame]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = center

        
        # Atualização da posição do heroi
        if  self.estado!=dash and self.estado!=defendendo :
            self.rect.x += self.speedx
        elif self.estado==defendendo:
            self.rect.x += self.speedx*0.25
        elif self.estado==dash:
            self.rect.x += self.speedx*41
            self.estado=indefeso
                  
        if self.hora_da_acao+self.acao_ticks*1.2<agora:
            if self.estado!=indefeso:
                self.estado=indefeso


        self.speedy += gravidade
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = caindo
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = espera
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = espera


        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
    def pulo(self):
        if self.state == espera:
            self.speedy -= tamanho_do_pulo
            self.state = pulando

    def ataque(self):
        if self.state==espera:
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = agora - self.hora_da_acao

        # Se já pode atirar novamente...
            
            if elapsed_ticks > self.acao_ticks*1.5:
            # Marca o tick da nova imagem.
                self.hora_da_acao = agora
                if self.estado == indefeso:
                    self.estado = ataque

    def defesa(self):
        if self.state==espera:
        # Verifica quantos ticks se passaram desde o último tiro.
            elapsed_ticks = agora - self.hora_da_acao

        # Se já pode atirar novamente...
            
            if elapsed_ticks > self.acao_ticks:
            # Marca o tick da nova imagem.
                self.hora_da_acao = agora
                if self.estado == indefeso:
                    self.estado = defendendo

    def dash(self):
        if self.quantdash>0:
            if self.speedx!=0:   
            # Verifica quantos ticks se passaram desde o último tiro.
                elapsed_ticks = agora - self.hora_da_acao

            # Se já pode atirar novamente...
                
                if elapsed_ticks > self.acao_ticks:
                # Marca o tick da nova imagem.
                    self.hora_da_acao = agora
                    if self.estado == indefeso:
                        self.estado = dash
                        self.quantdash-=1             
                    

def colisoes():
    
    if estado_do_jogo.aba=="jogando":
        if player.vida<=0:
            player.kill()
            barra.kill()
            estado_do_jogo.aba = "menu"
            
            
        else:
            if player.estado==indefeso:
                colisao=pygame.sprite.spritecollide(player,all_enemis,False, pygame.sprite.collide_mask)
                
                if len(colisao)>0:
                    if player.rect.bottom-inimigo.rect.top<0:
                        player.hora_do_dano=pygame.time.get_ticks()
                        player.estado=tomando_dano
                        player.vida-=10                       
                        player.rect.x-=90
                        

                    elif player.rect.right-inimigo.rect.centerx<0:
                        player.hora_do_dano=pygame.time.get_ticks()
                        player.estado=tomando_dano
                        player.vida-=10                       
                        player.rect.x-=60
                        
                    elif player.rect.left-inimigo.rect.centerx>0:
                        player.hora_do_dano=pygame.time.get_ticks()
                        player.estado=tomando_dano
                        player.vida-=10                       
                        player.rect.x+=60
                        
        
            if player.estado==ataque:
                colisao=pygame.sprite.spritecollide(player,all_enemis,False, pygame.sprite.collide_mask)   
                if len(colisao)>0:  
                    if player.rect.right-inimigo.rect.centerx<0:
                        inimigo.estado=tomando_dano
                        colisao.clear()
                        inimigo.dano()
                        player.estado=indefeso
                        barra_vermelha.diminuir()                    
                        player.rect.x-=40
                        
                    elif player.rect.left-inimigo.rect.centerx>0:
                        inimigo.estado=tomando_dano
                        colisao.clear()
                        inimigo.dano()
                        player.estado=indefeso
                        barra_vermelha.diminuir()                      
                        player.rect.x+=40
                        


            if player.estado==defendendo:
                colisao=pygame.sprite.spritecollide(player,all_enemis,False, pygame.sprite.collide_mask)   
                if len(colisao)>0:
                    colisao.clear()
                    inimigo.dano()
                    

class inimigos(pygame.sprite.Sprite):
    def __init__(self,vida_inimigo,player,assets):
        pygame.sprite.Sprite.__init__(self)
        #spritesheet = carrega_spritesheet(inimigo_sheet, 4, 5)
        self.image = assets[INIMIGOS_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura-300
        self.rect.bottom = random.randint(0,altura)
        self.speedx_inimigo = 0
        self.speedy_inimigo= 0
        self.vida=vida_inimigo
        self.estado=espera
    def update(self):
        if self.vida==0:
            self.kill()
            barra_vermelha.kill()
            fase=2
        if self.estado==espera:
            self.rect.x += self.speedx_inimigo
            self.rect.y += self.speedy_inimigo
        elif player.hora_da_acao+player.acao_ticks*0.3<agora:
            self.estado=espera
        if player.rect.x-self.rect.x>0 :
            self.speedx_inimigo = 1
            
        if player.rect.x-self.rect.x<0 :
            self.speedx_inimigo = -1

        
        
        if player.rect.y-self.rect.y>0 :
            self.rect.y != altura
            self.speedy_inimigo = 1 

        if player.rect.y-self.rect.y<0 :
            self.speedy_inimigo = -1
    def dano(self):
        if player.estado==ataque:
            inimigo.vida-=10
            if player.rect.right-inimigo.rect.centerx<0:
                inimigo.rect.x+=40
                inimigo.rect.y-=20             
            elif player.rect.left-inimigo.rect.centerx>=0:    
                inimigo.rect.x-=40
                inimigo.rect.y-=20                   
        if player.estado==defendendo:
            if player.rect.right-inimigo.rect.centerx<0:
                inimigo.rect.x+=60
                inimigo.rect.y-=25             
            elif player.rect.left-inimigo.rect.centerx>=0:    
                inimigo.rect.x-=60
                inimigo.rect.y-=25   
        

class modo_de_jogo():
    def __init__(self,player):
        self.aba="menu"
        self.timer_do_tutorial = pygame.time.get_ticks()
        self.duracao_do_tutorial=1000

    def esta_dentro(self,pos,x,y):
        self.posicaox=x
        self.posicaoy=y
        
        if pos[0]> self.posicaox and pos[0]<self.posicaox+playapertado_largura:
            if pos[1]>self.posicaoy and pos[1]<self.posicaoy+playapertado_altura:
                return True
        else:
            return False
        

    def jogando(self,qual_a_fase):
        fases(qual_a_fase)
              
        text = font.render(('{0}'.format(player.vida)), True, (0, 0, 255))
        text2= font.render(('{0}'.format(player.quantdash)), True, (255, 255, 0))
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit() 
        # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True 
                
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player.speedx -= 4.0
                if event.key == pygame.K_d:                  
                    player.speedx += 4.0
                if event.key == pygame.K_SPACE:
                    player.pulo()
                if event.key == pygame.K_ESCAPE:
                    self.aba = 'main menu'
                if event.key == pygame.K_l:
                    player.dash()
                
        # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
            # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_a:   
                        player.speedx += 4.0
                    if event.key == pygame.K_d:
                        player.speedx -= 4.0
                    if event.key == pygame.K_k:   
                        player.ataque()
                    if event.key == pygame.K_j:
                        player.defesa()
            
                
     
    # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor preta
        all_sprites.draw(window)
        window.blit(text,(10,10))
        window.blit(text2,(70,10))
        colisoes()
                
        all_sprites.update()
        
    # ----- Atualiza estado do jogo
        pygame.display.update()  


    def menu(self):
        global sequencia
        
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                pygame.quit()
       
        
        #tentativa de tutorial
        
            if sequencia==1:
                window.blit(assets[TELA_INICIAL_IMG], (0,0))
                window.blit(assets[PLAY], ((largura/2)-(play_largura/2), altura-100))
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button==1 and self.esta_dentro(pos,(largura/2)-(play_largura/2), altura-100):
                        sequencia=2
                        self.timer_do_tutorial=agora
            tempo=agora-self.timer_do_tutorial                
            if sequencia==2:
                
                window.blit(assets[TELA_INICIAL_IMG], (0,0))
                window.blit(assets[PLAYAPERTADO],((largura/2)-(play_largura/2), altura-100))  
                if  tempo> self.duracao_do_tutorial:
                    self.timer_do_tutorial=agora
                    sequencia=3
            if sequencia==3 :                
                window.blit(assets[TUTORIAL], (0, 0))
                if  tempo> self.duracao_do_tutorial:
                    window.blit(assets[PLAY], ((largura-300, altura-100)))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button==1 and self.esta_dentro(pos,(largura)-300, altura-100):
                            window.fill((0, 0, 0))
                            self.aba="jogando"

        pygame.display.update()
       

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
            self.jogando(fase)
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
            if self.quem_ta_seguindo.estado==ataque or self.quem_ta_seguindo.estado==defendendo :
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
                self.largura-=8
                self.image=pygame.transform.scale(self.image, (self.largura, barra_altura))


# ----- Inicia estruturas de dados
player_sheet = pygame.image.load(path.join(img_dir, 'hp existindo.png')).convert_alpha()
sequencia=1
clock = pygame.time.Clock()
vida=100
vida_inimigo=40
FPS = 60
all_sprites = pygame.sprite.Group()
all_enemis = pygame.sprite.Group()
assets=load_assets(img_dir)
blocks = pygame.sprite.Group()
# Cria tiles de acordo com o mapa
fase=1



player= heroi(vida,player_sheet,blocks)
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
mouse_pres=[]
game=True


agora=pygame.time.get_ticks()

# ===== Loop principal =====
while game:
    
    clock.tick(FPS)
    estado_do_jogo.controlador_menu()
    agora=pygame.time.get_ticks() 
   