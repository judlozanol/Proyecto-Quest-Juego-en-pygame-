import pygame
from ajustes import *
from utilidades import calcular_distancia
"recibe un SingleGroup y un grupo de sprites, y muestra la distancia del sprite mas cercano al SingleGroup"
class Brujula(pygame.sprite.Sprite):
    def __init__(self, sGrupo, grupo, pos):
        super().__init__()
        self.sGrupo = sGrupo
        self.grupo = grupo
        self.texto= "0 m"
        self.font= pygame.font.Font(pygame.font.get_default_font(),TAMANO_RECUADRO//5)
        self.image= self.font.render(self.texto, 1, "black", None)
        self.rect=self.image.get_rect(topleft= pos )
        
    def objeto_mas_cercano(self):
        posSGrupo = self.sGrupo.sprite.rect.center
        menor_distancia= -1
        for sprite in self.grupo:
            pos=sprite.rect.center
            if calcular_distancia(posSGrupo,pos)>menor_distancia:
                menor_distancia=calcular_distancia(posSGrupo,pos)
        
        self.texto= str(menor_distancia//100)+" m"

    def update(self):
        self.objeto_mas_cercano()
        self.image= self.font.render(self.texto, 1, "white", None)