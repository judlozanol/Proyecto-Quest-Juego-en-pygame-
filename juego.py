import pygame, sys
import ajustes
from interfazJugando import *
class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla= pygame.display.set_mode((ajustes.ANCHO_PANTALLA, ajustes.ALTO_PANTALLA+ajustes.TAMANO_RECUADRO))
        self.clock = pygame.time.Clock()
        self.activo=True
        self.estado= interfazJugando(self.pantalla)
    def correr(self):
        while self.activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.pantalla.fill('black')
            
            self.estado.run()
            
            pygame.display.update()
            self.clock.tick(ajustes.FPS)