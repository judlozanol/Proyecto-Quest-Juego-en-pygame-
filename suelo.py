import pygame
from utilidades import imagen_redimensionada
from ajustes import *
from objeto import *
import random
class Suelo(pygame.sprite.Sprite):
    def __init__(self, pos, capa):
        super().__init__()
        self.capa=capa
        self.desenterrado=False
        self.image= imagen_redimensionada("sprites/arena/arena.png", TAMANO_RECUADRO, TAMANO_RECUADRO)
        self.rect= self.image.get_rect(topleft= pos)
        self.objetos = pygame.sprite.GroupSingle()
        self.objeto = None
    def desenterrar(self):
        if not self.desenterrado:
            self.image= imagen_redimensionada("sprites/arena/revolcada.jpg", TAMANO_RECUADRO, TAMANO_RECUADRO)
            self.objetos.add(self.objeto) 
            self.desenterrado=True
        
    def update(self):
        if self.objetos.sprite:
            if self.objetos.sprite.usado:
                self.objetos.remove(self.objetos.sprite)
        self.objetos.update()
        self.objetos.draw(self.capa)

class SueloBomba(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)
        self.objeto = Bomba((pos[0]+TAMANO_RECUADRO/2, pos[1]+TAMANO_RECUADRO/2))
        

class SueloTesoro(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)
        self.objeto = Tesoro((pos[0]+TAMANO_RECUADRO/2, pos[1]+TAMANO_RECUADRO/2))
        
class SueloPotenciador(Suelo):
    def __init__(self, pos, capa):
        super().__init__(pos, capa)
        potenciadores=[Fruta((pos[0]+TAMANO_RECUADRO/2, pos[1]+TAMANO_RECUADRO/2)),Escudo((pos[0]+TAMANO_RECUADRO/2, pos[1]+TAMANO_RECUADRO/2))]
        self.objeto=random.choice(potenciadores)