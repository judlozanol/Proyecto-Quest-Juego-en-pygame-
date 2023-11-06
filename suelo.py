import pygame
from utilidades import imagen_redimensionada
from ajustes import *
from objeto import *
class Suelo(pygame.sprite.Sprite):
    def __init__(self, pos, capa):
        super().__init__()
        self.capa=capa
        self.image= imagen_redimensionada("sprites/arena/arena.png", TAMANO_RECUADRO, TAMANO_RECUADRO)
        self.rect= self.image.get_rect(topleft= pos)
        self.objetos = pygame.sprite.GroupSingle()
        self.objeto = Objeto((pos[0]+TAMANO_RECUADRO/2, pos[1]+TAMANO_RECUADRO/2))
        self.desenterrado=False
        
    def desenterrar(self):
        if not self.desenterrado:
            self.image= imagen_redimensionada("sprites/arena/revolcada.jpg", TAMANO_RECUADRO, TAMANO_RECUADRO)
            self.objetos.add(self.objeto) 
            self.desenterrado=True
        
    def update(self):
        self.objetos.update()
        self.objetos.draw(self.capa)

    
    
class SueloBomba(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)

class SueloTesoro(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)
        
class SueloPotenciador(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)