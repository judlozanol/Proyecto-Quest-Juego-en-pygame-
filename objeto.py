import pygame
from utilidades import imagen_redimensionada
from ajustes import *
class Objeto(pygame.sprite.Sprite):
    def __init__(self,posInicial):
        super().__init__()
        self.posInicialX= posInicial[0]
        self.posInicialY= posInicial[1]
        self.rapidez=(TAMANO_RECUADRO/10)-((TAMANO_RECUADRO/100)*2)

        self.image = imagen_redimensionada("sprites/bomba/inactiva.png",(TAMANO_RECUADRO/2),(TAMANO_RECUADRO/2))
        self.rect= self.image.get_rect(center=posInicial)
        self.direction= pygame.math.Vector2(0,-1)
        
    def desenterrar(self):
        if self.rect.y>=self.posInicialY+TAMANO_RECUADRO:
            self.direction.y=1
        if self.rect.y<=self.posInicialY-1:
            self.direction.y=0
            
    def update(self):
        self.rect.x+= self.direction.x*self.rapidez
        self.rect.y+= self.direction.y*self.rapidez
        self.desenterrar()