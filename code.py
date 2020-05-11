import pygame
from os import path
img_dir = path.join(path.dirname(__file__), 'img')
pygame.init()
altura = 480
largura = 600
STILL = 0
JUMPING = 1
FALLING = 2
GRAVITY=2
GROUND = altura * 5 // 6
JUMP_SIZE=20
# ----- Gera tela principal

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('mansao')

heroi_largura=30
heroi_altura=50
player_img = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
player_img = pygame.transform.scale(player_img, (heroi_largura, heroi_altura))

class heroi(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura -1
        self.speedx = 0
        self.speedy=0
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = STILL

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
    def pulo(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

        
    
        
    

# ----- Inicia estruturas de dados

clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()

player= heroi(player_img)
all_sprites.add(player)
keys_down = {}
game=True
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_SPACE:
                    player.pulo()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            if event.key in keys_down and keys_down[event.key]:
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx += 8
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 8
                if event.key == pygame.K_SPACE:
                    player.pulo()
    all_sprites.update()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    
    all_sprites.draw(window)

    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


