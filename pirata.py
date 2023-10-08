import pygame
from ajustes import *
from stateM import StateM
class Pirata(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.cavando=False
        self.flip=False
        self.rapidez=8
        self.velocidad_animacion=0.1 #un numero mayor a cero y menor a uno

        self.estado= StateM('idle')
        self.numSprite=0
        self.animar()

        self.rect = self.image.get_rect(topleft=pos)
        self.direction= pygame.math.Vector2(0,0)

    def animar(self):
        if self.estado.currentState=='caminando':
            self.animaciones=[pygame.transform.scale(pygame.image.load("sprites/pirata/movimiento/caminando1.png").convert_alpha(),(75, 75)), pygame.transform.scale(pygame.image.load("sprites/pirata/movimiento/caminando2.png").convert_alpha(),(75, 75))]
        elif self.estado.currentState=='idle':
            self.animaciones=[pygame.transform.scale(pygame.image.load("sprites/pirata/idle/idle1.png").convert_alpha(),(75,75))]
        elif self.estado.currentState=='cavando':
            self.animaciones=[pygame.transform.scale(pygame.image.load("sprites/pirata/movimiento/caminando3.png").convert_alpha(),(40,40)), pygame.transform.scale(pygame.image.load("sprites/pirata/movimiento/caminando4.png").convert_alpha(),(40,40))]
        if self.flip:
            self.image=pygame.transform.flip((self.animaciones[int(self.numSprite)]),True,False)
        else:
            self.image=self.animaciones[int(self.numSprite)]

    def get_input(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip=False
        elif teclas[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip=True
        else:
            self.direction.x = 0

        if teclas[pygame.K_UP]:
            self.direction.y = -1
        elif teclas[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if self.cavando:
            self.estado.set_status('cavando')
        elif self.direction.x==0 and self.direction.y==0:
            self.estado.set_status('idle')
        else:
            self.estado.set_status('caminando')

    def update(self):
        self.get_input()
        self.rect.x+= self.direction.x*self.rapidez
        self.rect.y+= self.direction.y*self.rapidez

        if self.rect.right < 0:
            self.rect.left = ancho_pantalla
        elif self.rect.left > ancho_pantalla:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = alto_pantalla
        elif self.rect.top > alto_pantalla:
            self.rect.bottom = 0

        self.numSprite+= self.velocidad_animacion
        if self.numSprite>=len(self.animaciones):
            self.numSprite=0
        self.animar()