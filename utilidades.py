import pygame
from math import sqrt,pow
def imagen_redimensionada(ruta, ancho, alto):
    return pygame.transform.scale(pygame.image.load(ruta).convert_alpha(),(ancho, alto))

def calcular_distancia(pos1,pos2):
    return sqrt(pow(pos1[0]-pos2[0], 2)+pow(pos1[1]-pos2[1], 2))