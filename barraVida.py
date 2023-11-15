import pygame
from ajustes import *
from corazon import *
class BarraVida(pygame.sprite.Group):
    def __init__(self,pos):
        super().__init__()
        self.posX=pos[0]
        self.posY=pos[1]
    def analizar_vida(self, jugador):
        self.empty()
        vidasActivas=jugador.stats.maxVidas-(jugador.stats.maxVidas-jugador.stats.vidas)
        posX=self.posX
        posY=self.posY
        for i in range(jugador.stats.maxVidas):
            if vidasActivas>0:
                self.add(Corazon((posX,posY)))
                vidasActivas-=1
            else:
                self.add(Corazon((posX,posY), False))
            posX+=(TAMANO_RECUADRO/4)*3
            