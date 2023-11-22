import pygame
from ajustes import *
"uestra el numero de ronda de un nivel"
class Ronda(pygame.sprite.Sprite):
    def __init__(self, pos,ronda):
        super().__init__()
        self.texto= "RONDA "+ str(ronda)
        self.color="red"
        self.font= pygame.font.Font(pygame.font.get_default_font(),TAMANO_RECUADRO//2)
        self.image= self.font.render(self.texto, 1, self.color, None)
        self.posicion=pos
        self.rect=self.image.get_rect(center= self.posicion )
    def update(self):
        self.rect=self.image.get_rect(center= self.posicion )
    