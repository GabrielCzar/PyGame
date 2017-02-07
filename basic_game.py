# -*- coding: utf-8 -*-
import sys, pygame

# Iniciar
pygame.init()

# Objects
ball = {
    'x': 400,
    'y': 300,
    'raio': 15,
    'color': (255, 0, 0),
}

# Definir tela 
WIDTH = 800
HEIGTH = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
BACKGROUND_COLOR = (255, 255, 255)

cont = 0
while True:
    deslocamento = 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball['x'] += deslocamento
            elif event.key == pygame.K_LEFT:
                ball['x'] -= deslocamento
            elif event.key == pygame.K_UP:
                ball['y'] -= deslocamento
            elif event.key == pygame.K_DOWN:
                ball['y'] += deslocamento
            elif event.key == pygame.K_RETURN: # Diagonal para baixo e a direita
                ball['x'] += deslocamento
                ball['y'] += deslocamento
            elif event.key == pygame.K_a: # Diagonal para cima e a esquerda
                ball['x'] -= deslocamento
                ball['y'] -= deslocamento
            elif event.key == pygame.K_z: # Diagonal para cima e a direita
                ball['x'] -= deslocamento
                ball['y'] += deslocamento
            elif event.key == pygame.K_f: # Diagonal para baixo e para esquerda
                ball['x'] += deslocamento
                ball['y'] -= deslocamento
            elif event.key == pygame.K_s:
                raio += 1
            elif event.key == pygame.K_d:
                raio -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #botao esquerdo
                ball['x'] += deslocamento
                ball['y'] += deslocamento
            elif event.button == 3: #botao direito
                ball['x'] -= deslocamento
                ball['y'] -= deslocamento
        elif event.type == pygame.MOUSEMOTION:
            ball['x'], ball['y'] = event.pos

    SCREEN.fill(BACKGROUND_COLOR)

    pygame.draw.circle(SCREEN, ball['color'], (ball['x'], ball['y']), ball['raio'], 0)

    if cont % 10 == 0:
        ball["x"] += 1
    cont += 1

    pygame.display.flip()
