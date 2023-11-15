import pygame
from ajustes import *
from utilidades import imagen_redimensionada
class Corazon(pygame.sprite.Sprite):
    def __init__(self,pos,activo=True):
        super().__init__()
        self.estado=activo
        self.analizar_estado()
        self.rect=self.image.get_rect(topleft=pos)
    def analizar_estado(self):
        if self.estado:
            self.image=imagen_redimensionada("sprites/barraVida/corazon/activo.png", TAMANO_RECUADRO/2,TAMANO_RECUADRO/2)
        else:
            self.image=imagen_redimensionada("sprites/barraVida/corazon/inactivo.png", TAMANO_RECUADRO/2,TAMANO_RECUADRO/2)
    def update(self):
        self.analizar_estado()
            
        
        
    