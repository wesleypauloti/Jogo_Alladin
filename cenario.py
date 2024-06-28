# cenario.py
import pygame
from config import *
import sys

def desenhar_cenario(screen, posicao, background_image):
    # Use dois loops aninhados para renderizar várias cópias do cenário
    for x in range(posicao, WIDTH, background_image.get_width()):
        for y in range(0, HEIGHT, background_image.get_height()):
            screen.blit(background_image, (x, y))

def game_over(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(20000)  # Aguarde 2 segundos (ou o tempo desejado)
    pygame.quit()
    sys.exit()

