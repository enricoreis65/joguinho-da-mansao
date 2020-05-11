import pygame


pygame.init()
WIDTH = 480
HEIGHT = 600

# ----- Gera tela principal

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('mansao')

heroi_largura=38
heroi_comprimento=50
livro_img = pygame.image.load('img/livro2.png').convert_alpha()
livro_img = pygame.transform.scale(livro_img, (heroi_comprimento, heroi_largura))

class heroi(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
        
    

# ----- Inicia estruturas de dados

clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()

player= heroi(livro_img)
all_sprites.add(player)

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
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
    all_sprites.update()
    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    
    all_sprites.draw(window)

    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


