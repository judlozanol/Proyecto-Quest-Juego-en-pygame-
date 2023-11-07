import pygame, sys
import ajustes
from nivel import Nivel
class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla= pygame.display.set_mode((ajustes.ANCHO_PANTALLA, ajustes.ALTO_PANTALLA))
        self.clock = pygame.time.Clock()
        self.activo=True
        self.nivel= Nivel(3,5, self.pantalla)
    def correr(self):
        while self.activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.pantalla.fill('black')
            self.nivel.run()

            pygame.display.update()
            self.clock.tick(ajustes.FPS)