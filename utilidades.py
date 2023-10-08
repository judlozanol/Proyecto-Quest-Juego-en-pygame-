import pygame
def imagen_redimensionada(ruta, ancho, alto):
    return pygame.transform.scale(pygame.image.load(ruta).convert_alpha(),(ancho, alto))