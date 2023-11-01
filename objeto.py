import pygame
from utilidades import imagen_redimensionada
from ajustes import *
class Objeto(pygame.sprite.Sprite):
    def __init__(self,posInicial):
        super().__init__()
        self.posInicial= posInicial
        self.image = imagen_redimensionada("sprites/bomba/inactiva.png",(TAMANO_RECUADRO/2),(TAMANO_RECUADRO/2))
        self.rect= self.image.get_rect(center=posInicial)
        self.direction= pygame.math.Vector2(0,-1)
    def desenterrar(self):
        if self.rect.center>=self.posInicial+TAMANO_RECUADRO:
            self.direction.y=1
        if self.rect.center<=self.posInicial-1:
            self.direction.y=0
            self.rect= self.image.get_rect(center=self.posInicial) #Incompletooooooooooooooo
    def update()