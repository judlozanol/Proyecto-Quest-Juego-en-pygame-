import pygame

class Pirata(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((50,75))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction= pygame.math.Vector2(0,0)
    def get_input(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direction.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if teclas[pygame.K_UP]:
            self.direction.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
    def update(self):
        self.get_input()
        self.rect.x+= self.direction.x*5
        self.rect.y+= self.direction.y*5