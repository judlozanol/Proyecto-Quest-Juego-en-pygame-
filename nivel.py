import pygame
from tiles import Tile
from random import randint
from ajustes import tamaño_recuadro
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
        
    def ubicar_nivel(self):
        self.tiles_bomb = pygame.sprite.Group()
        self.tiles_booster = pygame.sprite.Group()
        self.tiles_treasure = pygame.sprite.Group()
        self.tiles_sand=pygame.sprite.Group()
        for row_index,row in enumerate(self.estructura):
            for column_index,column in enumerate(row):
                if column=="B":
                    x= column_index * tamaño_recuadro
                    y= row_index * tamaño_recuadro
                    tile= Tile((x,y),tamaño_recuadro, "red")
                    self.tiles_bomb.add(tile)
                elif column=="P":
                    x= column_index * tamaño_recuadro
                    y= row_index * tamaño_recuadro
                    tile= Tile((x,y),tamaño_recuadro, "dark green")
                    self.tiles_booster.add(tile)
                elif column=="T":
                    x= column_index * tamaño_recuadro
                    y= row_index * tamaño_recuadro
                    tile= Tile((x,y),tamaño_recuadro, "green")
                    self.tiles_treasure.add(tile)
                else:
                    x= column_index * tamaño_recuadro
                    y= row_index * tamaño_recuadro
                    tile= Tile((x,y),tamaño_recuadro, "yellow")
                    self.tiles_sand.add(tile)
    def run(self):
        self.tiles_bomb.draw(self.capa)
        self.tiles_booster.draw(self.capa)
        self.tiles_treasure.draw(self.capa)
        self.tiles_sand.draw(self.capa)