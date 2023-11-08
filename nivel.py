import pygame
from random import randint
from ajustes import TAMANO_RECUADRO
from pirata import Pirata
from suelo import *
from brujula import Brujula
class Nivel:
    def __init__(self,bombas, potenciador, capa):
        self.estructura=["          ",
                        "          ",
                        "          ",
                        "          ",
                        "          ",
                        "          "]
        self.capa=capa
        self.tesoro=1
        self.jugador=1
        self.bombas=bombas
        self.potenciador=potenciador
        self.generar_nivel()
        self.ubicar_nivel()


    def ubicar_elemento(self,elemento,letra:type[str]):
        while elemento>0:
            row_c=randint(0, len(self.estructura)-1)
            column_c=randint(0,len(self.estructura[row_c])-1)
            for row_index,row in enumerate(self.estructura):
                if row_index==row_c:
                    nueva_linea=""
                    for column_index,column in enumerate(row):  
                        agregar=column
                        if column_index==column_c and column==" ":
                            agregar=letra
                        nueva_linea=nueva_linea+agregar
                    self.estructura[row_index]=nueva_linea
                    elemento-=1
    def generar_nivel(self):
        self.ubicar_elemento(self.bombas,"B")
        self.ubicar_elemento(self.potenciador,"P")
        self.ubicar_elemento(self.tesoro,"T")
        self.ubicar_elemento(self.jugador,"J")

    def ubicar_nivel(self):
        self.tiles_bomb = pygame.sprite.Group()
        self.tiles_booster = pygame.sprite.Group()
        self.tiles_treasure = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        self.tiles_sand=pygame.sprite.Group()

        self.suelos=pygame.sprite.Group()
        self.sueloInter=pygame.sprite.Group()
        for row_index,row in enumerate(self.estructura):
            for column_index,column in enumerate(row):
                x= column_index * TAMANO_RECUADRO
                y= row_index * TAMANO_RECUADRO
                if column=="B":
                    tile= SueloBomba((x,y), self.capa)
                    self.tiles_bomb.add(tile)
                    self.suelos.add(tile)
                    self.sueloInter.add(tile)
                elif column=="P":
                    tile= SueloPotenciador((x,y), self.capa)
                    self.tiles_booster.add(tile)
                    self.suelos.add(tile)
                    self.sueloInter.add(tile)
                elif column=="T":
                    tile= SueloTesoro((x,y), self.capa)
                    self.tiles_treasure.add(tile)
                    self.suelos.add(tile)
                    self.sueloInter.add(tile)
                elif column=="J" or column==" ":
                    tile= Suelo((x,y), self.capa)
                    self.tiles_sand.add(tile)
                    self.suelos.add(tile)
                if column=="J":
                    player= Pirata((x,y))
                    self.player.add(player)

    def validar_colisiones(self):
        if self.player.sprite.estado.get_status()=="cavando":
            for suelo in self.suelos:    
                if self.player.sprite.rect.colliderect(suelo.rect):
                    suelo.desenterrar()
                    if self.sueloInter.has(suelo):
                        self.sueloInter.remove(suelo)
        
    def run(self):
        #dibujar mapa
        
        self.tiles_bomb.draw(self.capa)
        self.tiles_booster.draw(self.capa)
        self.tiles_treasure.draw(self.capa)
        self.tiles_sand.draw(self.capa)
        self.suelos.update()

        brujula=Brujula(self.player, self.sueloInter,(0,0))
        self.brujulas=pygame.sprite.GroupSingle()
        self.brujulas.add(brujula)

        self.brujulas.update()
        self.brujulas.draw(self.capa)
        
        #dibujar jugador
        self.player.update()
        self.player.draw(self.capa)

        self.validar_colisiones()
        