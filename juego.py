import pygame, sys
import ajustes
from nivel import Nivel
class Juego:
    def __init__(self):
        pygame.init()
        self.pantalla= pygame.display.set_mode((ajustes.ancho_pantalla, ajustes.alto_pantalla))
        self.clock = pygame.time.Clock()
        self.activo=True
        self.nivel= Nivel(1,1, self.pantalla)
    def correr(self):
        while self.activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.pantalla.fill('black')
            self.nivel.run()

            pygame.display.update()
            self.clock.tick(ajustes.fps)