import pygame
from ajustes import *
"recibe un SingleGroup y un grupo de sprites, y muestra la distancia del sprite mas cercano al SingleGroup"
class Brujula(pygame.sprite.Sprite):
    def __init__(self, sGrupo, grupo, pos):
        super().__init__()
        self.sGrupo = sGrupo
        self.grupo = grupo
    def update(self):
        pass