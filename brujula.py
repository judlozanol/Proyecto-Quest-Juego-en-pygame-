import pygame
from ajustes import *
from utilidades import calcular_distancia
"recibe un SingleGroup y un grupo de sprites, y muestra la distancia del sprite mas cercano al SingleGroup"
class Brujula(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.texto= "0 m"
        self.distancia= 0
        self.color="black"
        self.font= pygame.font.Font(pygame.font.get_default_font(),TAMANO_RECUADRO//3)
        self.image= self.font.render(self.texto, 1, self.color, None)
        self.rect=self.image.get_rect(topleft= pos )
    def analizar_color(self):
        if self.distancia==0:
            self.color="red"
        elif self.distancia==1:
            self.color="orange"
        elif self.distancia==2:
            self.color="yellow"
        elif self.distancia==3:
            self.color="green"
        elif self.distancia>=4 and self.distancia<10:
            self.color="darkgreen"
        else:
            self.color="black"
    
    def objeto_mas_cercano(self, sGrupo, grupo):
        posSGrupo = sGrupo.sprite.rect.midbottom
        menor_distancia= 10000
        
        if len(grupo)==0:
            self.texto="(-w-')"
            self.distancia=10
        else:
            for sprite in grupo:
                pos=sprite.rect.center
                if calcular_distancia(posSGrupo,pos)<menor_distancia:
                    menor_distancia=calcular_distancia(posSGrupo,pos)

            self.distancia=menor_distancia//TAMANO_RECUADRO
            self.texto= str(self.distancia)+" m"

    def update(self):
        self.analizar_color()
        self.image= self.font.render(self.texto, 1, self.color, None)