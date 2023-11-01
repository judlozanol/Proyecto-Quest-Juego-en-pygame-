import pygame
from utilidades import imagen_redimensionada
from ajustes import *
class Suelo(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image= imagen_redimensionada("sprites/arena/arena.png", TAMANO_RECUADRO, TAMANO_RECUADRO)
        self.rect= self.image.get_rect(topleft= pos)
        
    def update(self):
        pass
    
    
class SueloBomba(Suelo):
    def __init__(self, pos):
        super().__init__(pos)

class SueloTesoro(Suelo):
    def __init__(self, pos):
        super().__init__(pos)
        
class SueloPotenciador(Suelo):
    def __init__(self, pos):
        super().__init__(pos)