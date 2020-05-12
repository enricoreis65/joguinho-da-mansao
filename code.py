import pygame
from os import path
img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
import random
#-----------------dados iniciais
altura = 480
largura = 600
#----dados movimento
espera = 0
pulando = 1
caindo = 2
gravidade=2
chao = altura * 5 // 6
tamanho_do_pulo=20



# ----- Gera tela principal

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('mansao')
font = pygame.font.SysFont("comicsansms", 40)

#definindo o player

heroi_largura=30
heroi_altura=40
player_img = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
player_img = pygame.transform.scale(player_img, (heroi_largura, heroi_altura))
inimigos_img=pygame.image.load(path.join(img_dir, 'tile-block.png')).convert_alpha()
inimigos_img = pygame.transform.scale(inimigos_img, (heroi_largura, heroi_altura))


class heroi(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = chao
        self.speedx = 0
        self.speedy=0

    #update    
    def update(self):
        # Atualização da posição do heroi
        self.rect.x += self.speedx

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



class inimigos(pygame.sprite.Sprite):
    def __init__(self,img,player):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura-30
        self.rect.bottom = chao
        self.speedx_inimigo = 0
       
        self.speedy_inimigo= 0
    def update(self):
        self.rect.x+= self.speedx_inimigo
        self.rect.y += self.speedy_inimigo
        print(player.rect.y-self.rect.y)
        if player.rect.x-self.rect.x>0 :
            self.speedx_inimigo = 1
            
        if player.rect.x-self.rect.x<0 :
            self.speedx_inimigo = -1

        if self.rect.bottom > chao:
            # Reposiciona para a posição do chão
            self.rect.bottom = chao

        if player.rect.y-self.rect.y>0 :
            if self.rect.y != altura -80:
                self.speedy_inimigo = 1
            else: self.rect.y==360

            
        if player.rect.y-self.rect.y<0 :
            self.speedy_inimigo = -1


class modo_de_jogo():

    def __init__(self):

        self.aba="menu"


    def jogando(self):

        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                pygame.quit() 
        # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx -= 4
                if event.key == pygame.K_RIGHT:
                    player.speedx += 4
                if event.key == pygame.K_SPACE:
                    player.pulo()
        # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key in keys_down and keys_down[event.key]:
            # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx += 4
                    if event.key == pygame.K_RIGHT:
                        player.speedx -= 4
        all_sprites.update()
    # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        all_sprites.draw(window)
    # ----- Atualiza estado do jogo
        pygame.display.update()   



    def menu(self):
        text = font.render('Aperte P para jogar', True, (0, 0, 255))
        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key==pygame.K_p:
                    self.aba="jogando"
        window.fill((255, 255, 255))
        window.blit(text,(largura-455,altura-360))
        pygame.display.update() 

    def controlador_menu(self):
        if self.aba=="menu":
            self.menu()
        if self.aba=="jogando":
            self.jogando()

# ----- Inicia estruturas de dados

clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()
all_enemis=pygame.sprite.Group()
estado_do_jogo= modo_de_jogo()
player= heroi(player_img)
inimigo= inimigos(inimigos_img,player)
all_sprites.add(player)
all_sprites.add(inimigo)
all_enemis.add(inimigo)
keys_down = {}
game=True
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    estado_do_jogo.controlador_menu()
    



