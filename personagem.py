# personagem.py
import pygame
from cenario import *
from config import *

def carregar_personagem():
    player_images = [
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/1.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/2.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/3.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/4.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/5.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/6.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/7.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png'),
        pygame.image.load('C:/Users/wesle/Downloads/ImagensJogo2DPython/PersonagemAndando/8.png')
    ]

    largura, altura = 150, 100
    player_images = [pygame.transform.scale(image, (largura, altura)) for image in player_images]
    player_images_direita = [pygame.transform.flip(image, True, False) for image in player_images]

    return player_images, player_images_direita

def movimento_personagem(pos_x,  em_movimento, frame_atual, keys, direcao):

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:        
        pos_x -= velocidade_x
        direcao = "esquerda"
        em_movimento = True
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pos_x += velocidade_x
        direcao = "direita"
        em_movimento = True
    else:
        em_movimento = False

    return pos_x, em_movimento, frame_atual
