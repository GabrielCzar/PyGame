#-*- coding=utf-8 -*-

import pygame

pygame.init()

resolution = 400, 200
screen = pygame.display.set_mode(resolution)
screen.fill((255, 255, 255))

fonte = pygame.font.SysFont("Arial", 60)
texto = 'BIRL'
tamanho = fonte.size(texto)
cor = 0, 0, 255
fundo = 233, 233, 233

render = fonte.render(texto, 0, cor, fundo)
posicao = 100, 100
screen.blit(render, posicao)

pygame.display.flip()

while True:
    if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
        break