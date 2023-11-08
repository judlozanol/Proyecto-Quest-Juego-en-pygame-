import pygame
from ajustes import *
from stateM import StateM
from utilidades import imagen_redimensionada
class Pirata(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.anchoSprite= (TAMANO_RECUADRO/4)*3
        self.altoSprite=(TAMANO_RECUADRO/4)*3
        self.cavando=False
        self.flip=False
        self.rapidez=(TAMANO_RECUADRO/10)-((TAMANO_RECUADRO/100)*2)
        self.velocidad_animacion=0.1 #un numero mayor a cero y menor a uno

        self.estado= StateM('idle')
        self.preEstado = StateM('idle')
  
        self.numSprite=0
        self.animar()

        self.rect = self.image.get_rect(topleft=pos)
        self.direction= pygame.math.Vector2(0,0)
    
    "guarda el estado anterior y analiza el nuevo estado del pirata"
    def analizar_estado(self):
        self.preEstado.set_status(self.estado.get_status())
        if self.cavando:
            self.estado.set_status('cavando')
        else:
            if self.direction.x==0 and self.direction.y==0:
                self.estado.set_status('idle')
            else:
                self.estado.set_status('caminando')
    
    def get_input(self):
        if self.cavando==False:
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
            
            if teclas[pygame.K_SPACE]:
                self.direction.y = 0
                self.direction.x = 0
                self.cavando=True
        else:
            if int(self.numSprite)==len(self.animaciones)-1:
                self.cavando=False
        
    "cambiara el conjunto de animaciones del pirata solo si este ha cambiado de estado"
    def cambiar_animaciones(self):
        if self.estado.currentState=='caminando':
            self.animaciones=[imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite), imagen_redimensionada("sprites/pirata/movimiento/caminando2.png",self.anchoSprite,self.altoSprite)]
        elif self.estado.currentState=='idle':
            self.animaciones=[imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite)]
        elif self.estado.currentState=='cavando':
            self.animaciones=[imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite)]
        
        if self.preEstado.get_status() != self.estado.get_status():
            self.numSprite=0
                 
    def animar(self):
        self.cambiar_animaciones()
        if self.flip:
            self.image=pygame.transform.flip((self.animaciones[int(self.numSprite)]),True,False)
        else:
            self.image=self.animaciones[int(self.numSprite)]

        self.numSprite+= self.velocidad_animacion
        if int(self.numSprite)>len(self.animaciones)-1:
            self.numSprite=0

    def update(self):
        self.get_input()
        self.analizar_estado()
        self.animar()
        
        self.rect.x+= self.direction.x*self.rapidez
        self.rect.y+= self.direction.y*self.rapidez
        
        if self.rect.right < 0:
            self.rect.left = ANCHO_PANTALLA
        elif self.rect.left > ANCHO_PANTALLA:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = ALTO_PANTALLA
        elif self.rect.top > ALTO_PANTALLA:
            self.rect.bottom = 0  