import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos,tamaño, color:type[str]):
        super().__init__()
        self.image= pygame.Surface((tamaño,tamaño))
        self.image.fill(color)
        self.rect= self.image.get_rect(topleft= pos)