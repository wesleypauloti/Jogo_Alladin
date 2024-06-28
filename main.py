import pygame
import sys
from config import *
from personagem import *
from cenario import *
from random import randint
import os
from time import sleep

pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

musica_de_fundo = pygame.mixer.music.load(os.path.join(diretorio_sons, 'music.mp3'))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
som_pontuacao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'score_sound.wav'))
som_pontuacao.set_volume(1)
som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))
som_pontuacao.set_volume(1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meu Jogo 2D")

# Carregue as imagens do jogador (olhando para a direita)
player_images = [
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/2.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/3.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/4.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/5.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/6.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/7.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png')),
    pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/8.png'))
]

player_images = [pygame.transform.scale(image, (largura, altura)) for image in player_images]

# Espelhe as imagens do jogador para a esquerda
player_images_direita = [pygame.transform.flip(image, True, False) for image in player_images]

obstaculo_image = pygame.image.load(os.path.join(diretorio_imagens, 'cacto.png'))
obstaculo2_image = pygame.image.load(os.path.join(diretorio_imagens, 'pedra.png'))
obstaculo_image = pygame.transform.scale(obstaculo_image, (largura_pedra, altura_pedra))

clock = pygame.time.Clock()
running = True

# Carrega a imagem do cenário
background_image = pygame.image.load(os.path.join(diretorio_imagens, 'images.jpeg'))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
largura_do_cenario = background_image.get_width()

som_colisão = pygame.mixer.Sound(os.path.join(diretorio_sons, 'death_sound.wav'))
som_colisão.set_volume(1)
colidiu = False

def exibe_mensagem(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}' 
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

def pular():
    pulo = True
    som_pulo.play()

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'Aladin/1.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Cria uma máscara a partir da imagem
        self.rect.center = (WIDTH / 2, chao) # Defina a posição y do personagem

class Pedra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'cacto.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Cria uma máscara a partir da imagem
        self.rect.center = (WIDTH, chao)  # Defina a posição y da pedra

class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'pedra.png'))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)  # Cria uma máscara a partir da imagem
        self.rect.center = (WIDTH, chao)  # Defina a posição y da pedra
        

personagem_sprite = Personagem()

obstaculos_group = pygame.sprite.Group()
pedra_sprite = Pedra()
cacto_sprite = Cacto()

obstaculos_group.add(pedra_sprite, cacto_sprite)

all_sprites = pygame.sprite.Group()  # Crie um grupo para todos os sprites
all_sprites.add(personagem_sprite, pedra_sprite, cacto_sprite)  # Adicione o personagem e a pedra ao grupo

game_over = False  # Variável para controlar o estado de game over

def show_game_over_screen(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    
    restart_text = font.render("Pressione R para reiniciar ou Q para sair", True, (255, 0, 0))
    restart_rect = restart_text.get_rect()
    restart_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
    
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if not game_over:
        
        keys = pygame.key.get_pressed()
            
        if not pause:
            # Cenário
            screen.fill(WHITE)
            # Movimente o cenário (subtrai a velocidade do cenário da posição)
            posicao_cenario -= velocidade_cenario
            # Chame a função para desenhar o cenário (adicionada)
            desenhar_cenario(screen, posicao_cenario, background_image)
            # Desenhando a Pedra
            screen.blit(obstaculo_image, (pos_x_pedra, pos_y_pedra))
            screen.blit(obstaculo2_image, (pos_x_cacto, pos_y_cacto))
            pos_x_pedra -= velocidade_cenario
            
            if pos_x_pedra < -500:
                pos_x_pedra = WIDTH + randint(500, 1500)
                
            if pos_x_cacto < -500:
                pos_x_cacto = WIDTH + randint(500, 1000)
                
            # Controles
            # Pulo
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w] and not pulando:
                if pos_y < chao and pulou:
                    pass
                elif not pulou:
                    som_pulo.play()
                    pulando = True
                    
            if pulando:
                if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                    pass
                    
            if keys[pygame.K_DOWN] or keys[pygame.K_s] and pos_y < chao:
                pos_y += velocidade_y * 1.2
                pulando = False
                descendo = True            
                
            if pulando:
                pos_y -= velocidade_y
                if pos_y <= altura_do_pulo:
                    tempo_no_ar += 1
                    pulando = False
                    descendo = True
                    if tempo_no_ar > 30:
                        pulou = True
                    
            # if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w] and pos_y == altura_do_pulo:
            #     tempo_no_ar = 0
                    
            if descendo:
                pos_y += velocidade_y
                
            if pos_y >= chao:
                descendo = False
                pos_y = chao
                tempo_no_ar = 0
                pulou = False
                frame_atual = (frame_atual + 1) % (len(player_images))
                    
            if pos_y != chao:
                frame_atual = 0
            else:
                pulando = False
                descendo = False
                
            
            if not pulando and not descendo:
                pos_y = chao
                
            pos_x, em_movimento, frame_atual = movimento_personagem(pos_x, em_movimento, frame_atual, keys, "direita")
            
            if direcao == "esquerda":
                screen.blit(player_images_direita[frame_atual], (pos_x, pos_y))
            else:
                screen.blit(player_images[frame_atual], (pos_x, pos_y))
                
            # Colisões
            # Retângulo de colisão do personagem
            player_rect = pygame.Rect(pos_x, pos_y, 70, 40)

            # Retângulo de colisão da pedra
            obstaculo_rect = pygame.Rect(pos_x_pedra + 20, pos_y_pedra, 100, 70)
            
            if player_rect.colliderect(obstaculo_rect):
                som_colisão.play()
                colidiu = True
                game_over = True
            
            # Limitando os extremos do mapa
            if pos_x < -60:
                pos_x = -60
            if pos_x > WIDTH -140:
                pos_x = WIDTH -140
                
            # if pos_x == (pos_x_pedra - 30) and pos_y > (chao - 30):
            #     pos_x -= velocidade_cenario
            #     if pos_x == -59:
            #         game_over(screen)
            
            if not colidiu:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_KP_ENTER:
                            if pause:
                                pause = False
                            else:
                                pause = True
                if not pause:
                    all_sprites.update()
            
    if game_over:
        pygame.mixer.music.stop()
        show_game_over_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reiniciar o jogo
                    game_over = False
                    # Reinicie as posições do personagem e da pedra, ou recarregue seu estado inicial
                    pos_x = 50
                    pos_x_pedra = WIDTH
                    pygame.mixer.music.play()
                elif event.key == pygame.K_q:
                    # Encerrar o jogo                    
                    running = False
                    
    pygame.time.delay(10)
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
