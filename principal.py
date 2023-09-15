import pygame, sys
from ajustes import *
from nivel import Nivel

#Ajustes de pygame
pygame.init()
pantalla=pygame.display.set_mode((ancho_pantalla, alto_pantalla))
clock= pygame.time.Clock()
jugando=True

nivel = Nivel(2,1,pantalla)#Un nivel especifico
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pantalla.fill('black')
    nivel.run()

    pygame.display.update()
    clock.tick(60)