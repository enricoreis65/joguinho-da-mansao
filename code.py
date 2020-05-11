import pygame


pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('mansao')
cor=(255,0,0)
heroi_largura=38
heroi_comprimento=50
vertices=[(50,0),(88,0),(0,0),(0,38)]
heroisquare=pygame.draw.polygon(window, cor, vertices)
class heroi(pygame.sprite.Sprite):
    def __init__(self,heroisquare):
        pygame.sprite.Sprite.__init__(self)
        self.heroisquare=heroisquare
        
        
    

# ----- Inicia estruturas de dados

clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()

player= heroi(heroisquare)
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

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca
    
    all_sprites.draw(window)

    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


