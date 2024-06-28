# config.py

# Cenário
WIDTH, HEIGHT = 800, 600
FPS = 60
chao = HEIGHT - 250
posicao_cenario = 0
frame_atual = FPS
velocidade_cenario = 3  # Velocidade do cenário
chao = HEIGHT - 250

# Obstaculo
largura_pedra, altura_pedra = 200, 200
pos_x_pedra = 2000
pos_y_pedra = chao - altura_pedra / 4
largura_cacto, altura_cacto = 200, 200
pos_x_cacto = 2000
pos_y_cacto = chao - altura_cacto / 4

# Personagem
largura, altura = 150, 100
velocidade_x = 5
velocidade_y = 10
altura_do_pulo = chao - 250
pulando = False
pulo = False
pulou = False
jump = False
fim_do_pulo = False
tempo_no_ar = 0
descendo = False
pos_x, pos_y = 50, chao
em_movimento = False
direcao = "direita"
player_images = []

pontos = 0
pause = False
restart_key_pressed = True

# Cores
WHITE = (255, 255, 255)

