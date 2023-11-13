import pygame
from ajustes import *
from stateM import StateM
from utilidades import imagen_redimensionada, rotar_imagen_redimensionada
from pirataStats import PirataStats
class Pirata(pygame.sprite.Sprite):
    def __init__(self,pos,stats = False):
        super().__init__()

        self.cavando=False
        self.flip=False
        self.escudo=False
        self.objMano=False
        
        self.estado= StateM('idle')
        self.preEstado = StateM('idle')

        self.rapidez=(TAMANO_RECUADRO/10)-((TAMANO_RECUADRO/100)*2)
        self.velocidad_animacion=0.3 #un numero mayor a cero y menor a uno

        #sera el encargado de la direccion de movimiento del pj
        self.direction= pygame.math.Vector2(0,0)

        self.anchoSprite= (TAMANO_RECUADRO/4)*3
        self.altoSprite=(TAMANO_RECUADRO/4)*3

        self.numSprite=0
        self.animar()
        self.rect = self.image.get_rect(topleft=pos)
        
        self.objeto=pygame.sprite.GroupSingle()

        if stats:
            self.stats=stats
        else:
            self.stats=PirataStats()

    def get_stats(self):
        return self.stats
    """guarda el estado anterior y analiza el nuevo estado del pirata"""
    def analizar_estado(self):
        self.preEstado.set_status(self.estado.get_status())
        if self.stats.vidas<=0:
            self.estado.set_status('muerto')
            self.direction.x=0
            self.direction.y=0
        elif self.cavando:
            self.estado.set_status('cavando')
        else:
            if self.direction.x==0 and self.direction.y==0:
                self.estado.set_status('idle')
            else:
                self.estado.set_status('caminando')

    """captura el teclado para las acciones del pirata"""
    def get_input(self):
        if self.cavando==False and self.estado.get_status()!='muerto':
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
        
    """validara el conjunto de animaciones del pirata, el index solo lo cambiara si este ha cambiado de estado"""
    def cambiar_animaciones(self):
        if self.estado.currentState=='caminando':
            self.animaciones=[imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite), imagen_redimensionada("sprites/pirata/movimiento/caminando2.png",self.anchoSprite,self.altoSprite)]
        elif self.estado.currentState=='idle':
            self.animaciones=[imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite)]
        elif self.estado.currentState=='cavando':
            self.animaciones=[imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite),imagen_redimensionada("sprites/pirata/movimiento/caminando1.png",self.anchoSprite,self.altoSprite)]
        elif self.estado.currentState=='muerto':
            self.animaciones=[rotar_imagen_redimensionada(imagen_redimensionada("sprites/pirata/idle/idle1.png",self.anchoSprite,self.altoSprite),90)]
        
        if self.preEstado.get_status() != self.estado.get_status():
            self.numSprite=0

    """aplica el conjunto de animaciones al pj"""
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
        if self.rect.top < 2:
            self.rect.top = 2
        elif self.rect.bottom > ALTO_PANTALLA-2:
            self.rect.bottom = ALTO_PANTALLA-2

        print(self.stats.vidas,self.stats.puntaje,self.escudo)