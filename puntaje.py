import pygame
from ajustes import *
"muesta la puntuación de la partida que se este jugando"
class Puntaje(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.texto= "PUNTAJE: 0"
        self.color="red"
        self.font= pygame.font.Font(pygame.font.get_default_font(),TAMANO_RECUADRO//3)
        self.image= self.font.render(self.texto, 1, self.color, None)
        self.posicion=pos
        self.rect=self.image.get_rect(center= self.posicion )
        
    """actualiza el texto al acceder al puntaje de un jugador"""
    def actualizar_puntaje(self,jugador):
        self.texto= "PUNTAJE: "+str(jugador.stats.puntaje)
        
    def update(self): 
        self.image= self.font.render(self.texto, 1, self.color, None)
        self.rect=self.image.get_rect(center= self.posicion )