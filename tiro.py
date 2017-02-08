# -*- coding: utf-8 -*-
"""
@author: Gabriel
"""
import sys, pygame
import math
from random import *

pygame.init()
# pygame.mixer.music.load("sound.mp3") CARREGAR 
# pygame.mixer.music.play(1) TOCAR 

DIMENSAO = (LARGURA, ALTURA) = (800, 600)
TELA = pygame.display.set_mode(DIMENSAO)

# Dados
pause = True
dead = False
win = False
usuario = {
    "pos": {
        "x": 40,
        "y": 300
    },
    "vel": {
        "x": 0,
        "y": 0
    },
    "raio": 15,
    "cor": (0,0,255)
}

inimigos = []

for i in range(5):
    inimigo = {
        "pos":{
            "x": randint(50, 750),
            "y": 50
        },
        "vel":{
            "x": 0,
            "y": randint(1, 4)
        },
        "raio": 15,
        "cor": (255,0,0)
    }
    inimigos.append (inimigo)

balas = []
ang = 45
vel = 30
maxBalas = 5

def desenhaPersonagem (personagem):
    pygame.draw.circle(TELA, personagem["cor"], (personagem["pos"]['x'], personagem["pos"]['y']), personagem["raio"], 0)

def desenhaBala (bala):
    cor = (100,100, 0)
    raio = 5
    pygame.draw.circle(TELA, cor, (bala["pos"]['x'], bala["pos"]['y']), raio, 0)

def atualizaPersonagem (personagem):
    personagem["pos"]["x"] += personagem["vel"]["x"]
    personagem["pos"]["y"] += personagem["vel"]["y"]

def atualizaBala( bala ):
    bala["vel"]["y"] += 1
    bala["pos"]["x"] += bala["vel"]["x"]
    bala["pos"]["y"] += bala["vel"]["y"]

def limitaPersonagem( personagem ):
    #borda superior
    if personagem["pos"]["y"] - personagem["raio"] < 0:
        personagem["pos"]["y"] = 0 + personagem["raio"]
        personagem["vel"]["y"] *= -1
    #borda inferior
    if personagem["pos"]["y"] + personagem["raio"] > 600:
        personagem["pos"]["y"] = 600 - personagem["raio"]
        personagem["vel"]["y"] *= -1
    #borda esquerda
    if personagem["pos"]["x"] - personagem["raio"] < 0:
        personagem["pos"]["x"] = 0 + personagem["raio"]
        personagem["vel"]["x"] *= -1
    #borda direita
    if personagem["pos"]["x"] + personagem["raio"] > 800:
        personagem["pos"]["x"] = 800 - personagem["raio"]
        personagem["vel"]["x"] *= -1

def limitaBala (bala):
    raio = 5
    #borda superior
    if bala["pos"]["y"] - raio < 0:
        bala["pos"]["y"] = 0 + raio
        bala["vel"]["y"] *= -1
    #borda inferior
    if bala["pos"]["y"] + raio > ALTURA:
        bala["pos"]["y"] = ALTURA - raio
        bala["vel"]["y"] *= -1
    #borda esquerda
    if bala["pos"]["x"] - raio < 0:
        bala["pos"]["x"] = 0 + raio
        bala["vel"]["x"] *= -1
    #borda direita
    global maxBalas
    if bala["pos"]["x"] + raio > LARGURA:
        bala["pos"]["x"] = LARGURA - raio
        bala["vel"]["x"] *= -1
        balas.remove(bala)
        maxBalas -= 1

def dist (ponto1, ponto2):
    cH = ponto2["x"] - ponto1["x"]
    cV = ponto2["y"] - ponto1["y"]
    d = math.sqrt( cH * cH + cV * cV )
    return d

def colisao (pers1, pers2):
    if dist(pers1["pos"], pers2["pos"]) <= pers1["raio"] + pers2["raio"]:
        return True
    return False

def colisaoBala (bala, personagem ):
    if dist(bala["pos"], personagem["pos"]) <= personagem["raio"]:
        return True
    return False

def atirar (personagem):
    if len (balas) < maxBalas:
        b = {
            "pos": {
                "x": personagem["pos"]["x"] + personagem["raio"],
                "y": personagem["pos"]["y"]
            },
            "vel": {
                "x": int (vel * math.cos((math.pi / 180) * ang)),
                "y": -int(vel * math.sin((math.pi / 180) * ang))
            }
        }
        balas.append(b)


contIni = 1
tempo = 200

#funcoes principais
def atualiza():
    #atualizando o usuario
    atualizaPersonagem (usuario)
    limitaPersonagem (usuario)
    #atualizando os inimigos
    for inimigo in inimigos:
        atualizaPersonagem (inimigo)
        limitaPersonagem (inimigo)
    #colisao entre os inimigos
    for i in range(len(inimigos)):
        for j in range(i + 1, len (inimigos)):
            if colisao (inimigos[i], inimigos[j]):
                aux = inimigos[i]["vel"]
                inimigos[i]["vel"] = inimigos[j]["vel"]
                inimigos[j]["vel"] = aux
    #atualizando as balas
    for bala in balas:
        atualizaBala (bala)
        limitaBala (bala)
    #colisao entre as balas e os inimigos
    global maxBalas
    for b in balas:
        for ini in inimigos:
            if colisaoBala (b, ini):
                inimigos.remove(ini)
                balas.remove(b)
                maxBalas += 1
                print "maxBalas", maxBalas
    #surgindo inimigos
    global contIni
    if contIni % tempo == 0:
        inimigo = {
            "pos": {
                "x": 760,
                "y": 250 + 50 * randint(-2,6)
            },
            "vel": {
                "x": randint(-4, -1),
                "y": 0
            },
            "raio": randint(10, 20),
            "cor": (255,0,0)
        }
        inimigos.append(inimigo)
    contIni += 1
    #derrota
    #colisao entre o usuario e os inimigos
    global pause, dead, win
    
    for ini in inimigos:
        if colisao(usuario, ini) or maxBalas == 0:
            dead = True
    #vitoria
    if len (inimigos) == 0:
        win = True

def desenha():
    desenhaPersonagem (usuario)
    for inimigo in inimigos:
        desenhaPersonagem (inimigo)
    for b in balas:
        desenhaBala (b)

def show(background, texto):
    pygame.draw.rect(TELA, background, (200, 200, 400, 200))
    fonte = pygame.font.SysFont("Arial", 54)
    size = fonte.size(texto)
    color = (0, 0, 0)
    render = fonte.render(texto, 0, color, background)
    posicao = 280, 270
    TELA.blit(render, posicao)

def interacao_usuario():
    desl = 20
    global pause, vel, ang
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                usuario["pos"]['y'] -= desl
            elif event.key == pygame.K_DOWN:
                usuario["pos"]['y'] += desl
            elif event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_RETURN:
                atirar (usuario)
            elif event.key == pygame.K_a:
                ang += 5
            elif event.key == pygame.K_d:
                ang -= 5
            elif event.key == pygame.K_w:
                vel += 3
            elif event.key == pygame.K_s:
                vel -= 3

cont = 0
framerate = 20

while True:
    interacao_usuario()

    cor_fundo = (255, 255, 255)
    TELA.fill(cor_fundo)

    #atualiza todo o cenario    
    if not pause and not dead and not win:
        if cont % framerate == 0:
            atualiza()
        cont += 1
    #desenha todo o cenario    
    

    if dead:
        show((255, 0, 0), 'You Lose!')
    elif win:
        show((0, 255, 0), 'You Win!')
    else:
        desenha()

    pygame.display.flip()
