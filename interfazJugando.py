import pygame
from ajustes import *
from nivel import Nivel
class interfazJugando:
    def __init__(self,capa) -> None:
        self.bombas= 1
        self.potenciadores= 0
        self.capa=capa
        self.statsPirata=False
        self.nivel = Nivel(self.bombas,self.potenciadores,self.capa,self.statsPirata)
    def aumentar_objetos(self):
        self.bombas+=1
        if self.bombas>=2:
            if (self.bombas+1)%3==0:
                self.potenciadores+=1
    def evaluar_nivel(self):
        if self.nivel.terminado:
            self.statsPirata= self.nivel.player.sprite.get_stats()
            self.aumentar_objetos()
            self.nivel = Nivel(self.bombas,self.potenciadores,self.capa,self.statsPirata)

    def run(self):
        self.evaluar_nivel()
        self.nivel.run()
        
                                    