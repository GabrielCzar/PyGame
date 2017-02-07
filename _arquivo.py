# -*- coding: utf-8 -*-
"""
@author: Gabriel
"""
import math
from random import *

angulo = 45
velocidade = 30
maxBalas = 5

personagem = {
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

inimigo = {
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

bala = {
    "pos": {
        "x": personagem["pos"]["x"] + personagem["raio"],
        "y": personagem["pos"]["y"]
    },
    "vel": {
        "x": int (velocidade * math.cos((math.pi / 180) * angulo)),
        "y": -int(velocidade * math.sin((math.pi / 180) * angulo))
    }
}

def salvarPersonagem(arquivo, personagem):
    arquivo.write (str (personagem["pos"]["x"]) + " " + \
                   str (personagem["pos"]["y"]) + " " + \
                   str (personagem["vel"]["x"]) + " " + \
                   str (personagem["vel"]["y"]) + " " + \
                   str (personagem["raio"]) + " " + \
                   str (personagem["cor"][0]) + " " + \
                   str (personagem["cor"][1]) + " " + \
                   str (personagem["cor"][2]) + "\n")

def salvarBala(arquivo, bala):
    arquivo.write (str (bala["pos"]["x"]) + " " + \
                   str (bala["pos"]["y"]) + " " + \
                   str (bala["vel"]["x"]) + " " + \
                   str (bala["vel"]["y"]) + "\n")

def salvarArquivo():
    arquivo = open("checkpoint", "w")
    arquivo.write (str (pause) + "\n")

    salvarPersonagem (arquivo, personagem)

    salvarPersonagem(arquivo, inimigo)

    salvarBala(arquivo, bala)

    arquivo.write (str (ang) + "\n")
    arquivo.write (str (vel) + "\n")
    arquivo.write (str (maxBalas) + "\n")
    
    arquivo.close()

def carregarArquivo():
    arquivo = open("checkpoint", "r")
    linhas = arquivo.readlines()

    global pause
    pause = (linhas[0] == "True\n")
    # Personagem
    infoUsuario = map(int, linhas[1].split())
    usuario["pos"]["x"] = infoUsuario[0]
    usuario["pos"]["y"] = infoUsuario[1]
    usuario["vel"]["x"] = infoUsuario[2]
    usuario["vel"]["y"] = infoUsuario[3]
    usuario["raio"] = infoUsuario[4]
    usuario["cor"] = (infoUsuario[5], infoUsuario[6], infoUsuario[7])
    
    # Inimigos
    # numeroInimigos = int (linhas[2])
    # del inimigos[:]
    infoInimigo = map (int, linhas[2].split())
    inimigo = {}
    inimigo["pos"] = {}
    inimigo["pos"]["x"] = infoInimigo[0]
    inimigo["pos"]["y"] = infoInimigo[1]
    inimigo["vel"] = {}
    inimigo["vel"]["x"] = infoInimigo[2]
    inimigo["vel"]["y"] = infoInimigo[3]
    inimigo["raio"] = infoInimigo[4]
    inimigo["cor"] = (infoInimigo[5], infoInimigo[6], infoInimigo[7])
    inimigos.append(inimigo)
    
    # Balas
    # numeroBalas = int (linhas[3 + nIni])
    # del balas[:]
    
    infoBala = map(int, linhas[3].split())
    bala = {}
    bala["pos"] = {}
    bala["pos"]["x"] = infoBala[0]
    bala["pos"]["y"] = infoBala[1]
    bala["vel"] = {}
    bala["vel"]["x"] = infoBala[2]
    bala["vel"]["y"] = infoBala[3]
    balas.append(bala)

    # Angulo
    global angulo
    angulo = int (linhas[4])
    # Velocidade
    global vel
    vel = int (linhas[5])
    # MaxBalas
    global maxBalas
    maxBalas = int (linhas[6])
    
    arquivo.close()
