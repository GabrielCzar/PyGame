# -*- coding: utf-8 -*-
"""
@author: Gabriel

@Bug Ao bater nas laterais do retangulo a um aumento extra
"""

import sys, pygame

pygame.init()

WIDTH, HEIGHT, EXTRA = 800, 600, 200
BACKGROUND_COLOR = (255, 255, 255)
SCREEN = pygame.display.set_mode([WIDTH + EXTRA, HEIGHT])
pygame.display.set_caption("Bounce")

kill = 0
death = 0

# Ball
ball = {
    "pos" : {
        "x" : 400,
        "y" : 300
    },
    "vel" : {
        "x" : 1,
        "y" : 1
    },
    "color" : (255, 0, 0),
    "raio" : 15
}
 
retangulo = {
    'pos' : {
        'x' : 480,
        'y' : 550
    },
    'tam' : {
        'largura' : 160,
        'altura' : 35
    },
    'color' : (0, 0, 255),
    'deslocamento' : 160
}

def retanguloMove(retangulo, key):
    if key == pygame.K_LEFT and not \
        retangulo['pos']['x'] - retangulo['deslocamento'] < 0 :                
        retangulo['pos']['x'] -= retangulo['deslocamento']

    if key == pygame.K_RIGHT and not \
        retangulo['pos']['x'] + retangulo['tam']['largura'] + retangulo['deslocamento'] > WIDTH:
        retangulo['pos']['x'] += retangulo['deslocamento']
def limitarBola(bola):
    # Limitando a bola para nao ultrapassar bordas
    if ball['pos']['x'] - ball['raio'] < 0 or ball['pos']['x'] + ball['raio'] > WIDTH:
            ball['vel']['x'] = -ball['vel']['x']
    if ball['pos']['y'] - ball['raio'] < 0 or ball['pos']['y'] + ball['raio'] > HEIGHT:
            ball['vel']['y'] = -ball['vel']['y']

def bolaMove(ball):
    ball['pos']['x'] += ball['vel']['x']
    ball['pos']['y'] += ball['vel']['y']

def colisao(ball, retangulo):
    ball_retangulo = pygame.Rect(ball['pos']['x'] - ball['raio'], ball['pos']['y'] - ball['raio'], \
                     ball['raio'] * 2,  ball['raio'] * 2)
    r = pygame.Rect(retangulo['pos']['x'], retangulo['pos']['y'], retangulo['tam']['largura'], retangulo['tam']['altura'])
    if r.colliderect(ball_retangulo):
        ball['vel']['y'] = -ball['vel']['y']
        return True
    return False

def dead(bola):
    if ball['pos']['y'] + ball['raio'] > HEIGHT:
        ball['pos']['x'], ball['pos']['y'] = 400, 300
        ball['vel']['y'] = -ball['vel']['y']
        return True
    return False

def mostrar(kill, death):
    fonte = pygame.font.SysFont("Arial", 26)
    gameName = 'Bounce'
    acertos = 'Acertos: ' + str(kill) 
    morte = 'Mortes: ' + str(death)
    tam1 = fonte.size(gameName)
    tam2 = fonte.size(acertos)
    tam3 = fonte.size(morte)

    cor = 0, 0, 0
    fundo = BACKGROUND_COLOR

    render1 = fonte.render(gameName, 0, cor, fundo)
    render2 = fonte.render(acertos, 0, cor, fundo)
    render3 = fonte.render(morte, 0, cor, fundo)
   
    posicao1 = WIDTH + 10, 100
    posicao2 = WIDTH + 10, 140
    posicao3 = WIDTH + 10, 180
    
    SCREEN.blit(render1, posicao1)
    SCREEN.blit(render2, posicao2)
    SCREEN.blit(render3, posicao3)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            retanguloMove(retangulo, event.key)
                
    limitarBola(ball)
    bolaMove(ball)

    if colisao(ball, retangulo):
        kill += 1
    if dead(ball):
        death += 1

    SCREEN.fill(BACKGROUND_COLOR)

    # Desenha bola e retangulo
    pygame.draw.circle(SCREEN, ball['color'], (ball['pos']['x'], ball['pos']['y']), ball['raio'], 1)
    pygame.draw.rect(SCREEN, retangulo['color'], (retangulo['pos']['x'], retangulo['pos']['y'], retangulo['tam']['largura'], retangulo['tam']['altura']))

    # Desenhar bordas
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 2)

    mostrar(kill, death)

    pygame.display.flip()

pygame.quit()

