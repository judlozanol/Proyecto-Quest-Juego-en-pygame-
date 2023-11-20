import pygame
from random import randint
from ajustes import TAMANO_RECUADRO
from pirata import Pirata
from suelo import *
from brujula import Brujula
from puntaje import Puntaje
from barraVida import BarraVida

class Nivel:
    def __init__(self,bombas, potenciador, capa, statsPirata=False):
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
        
        if statsPirata:
            self.statsPirata=statsPirata
        else:
            self.statsPirata=False

        self.generar_nivel()
        self.ubicar_nivel()

        brujula=Brujula((0,0))
        self.brujulas=pygame.sprite.GroupSingle()
        self.brujulas.add(brujula)
        
        puntaje=Puntaje((ANCHO_PANTALLA-TAMANO_RECUADRO/2,(TAMANO_RECUADRO/4)+ALTO_PANTALLA))
        self.puntaje=pygame.sprite.GroupSingle()
        self.puntaje.add(puntaje)
        
        self.barraVida= BarraVida((TAMANO_RECUADRO/2,(TAMANO_RECUADRO/4)+ALTO_PANTALLA))

        self.terminado=False

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
        self.ubicar_elemento(self.jugador,"J")
        self.ubicar_elemento(self.tesoro,"T")
        self.ubicar_elemento(self.bombas,"B")
        self.ubicar_elemento(self.potenciador,"P")
        
    def ubicar_nivel(self):
        self.tiles_bomb = pygame.sprite.Group()
        self.tiles_booster = pygame.sprite.Group()
        self.tiles_treasure = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        self.objJugador = pygame.sprite.GroupSingle()
        self.tiles_sand=pygame.sprite.Group()

        self.suelos=pygame.sprite.Group()
        self.sueloBruj=pygame.sprite.Group()
        self.sueloObj=pygame.sprite.Group()
        
        for row_index,row in enumerate(self.estructura):
            for column_index,column in enumerate(row):
                x= column_index * TAMANO_RECUADRO
                y= row_index * TAMANO_RECUADRO
                
                if column=="T":
                    tile= SueloTesoro((x,y), self.capa)
                    self.tiles_treasure.add(tile)
                    self.suelos.add(tile)
                    self.sueloBruj.add(tile)
                    self.sueloObj.add(tile)
                elif column=="B":
                    tile= SueloBomba((x,y), self.capa)
                    self.tiles_bomb.add(tile)
                    self.suelos.add(tile)
                    self.sueloBruj.add(tile)
                    self.sueloObj.add(tile)
                elif column=="P":
                    tile= SueloPotenciador((x,y), self.capa)
                    self.tiles_booster.add(tile)
                    self.suelos.add(tile)
                    self.sueloBruj.add(tile)
                    self.sueloObj.add(tile)
                
                elif column=="J" or column==" ":
                    tile= Suelo((x,y), self.capa)
                    self.tiles_sand.add(tile)
                    self.suelos.add(tile)
                if column=="J":
                    player= Pirata((x,y),self.statsPirata)
                    self.player.add(player)

    def validar_colisiones(self):
        if self.player.sprite.estado.get_status()=="cavando":
            for suelo in self.suelos:    
                if suelo.rect.collidepoint(self.player.sprite.rect.bottomleft) or suelo.rect.collidepoint(self.player.sprite.rect.bottomright) :
                    suelo.desenterrar()
                    if self.sueloBruj.has(suelo):
                        self.sueloBruj.remove(suelo)
        for suelo in self.sueloObj:
            if suelo.desenterrado:
                if suelo.objetos.sprite.interactuable and suelo.objetos.sprite.rect.colliderect(self.player.sprite.rect):
                    if type(suelo.objetos.sprite).__name__=="Tesoro":
                        self.terminado=True
                    if type(suelo.objetos.sprite).__name__=="Escudo":
                        self.objJugador.add(suelo.objetos.sprite)
                    suelo.objetos.sprite.interaccion_jugador(self.player.sprite)
                    self.sueloObj.remove(suelo)
                    
    def validar_objJugador(self):
        if self.player.sprite.objMano:
            if self.player.sprite.flip:
                self.objJugador.sprite.rect.center=self.player.sprite.rect.midleft
            else:
                self.objJugador.sprite.rect.center=self.player.sprite.rect.midright
        else:
            self.objJugador.empty()

    def run(self):
        #dibujar mapa
        self.tiles_bomb.draw(self.capa)
        self.tiles_booster.draw(self.capa)
        self.tiles_treasure.draw(self.capa)
        self.tiles_sand.draw(self.capa)
        self.suelos.update()

        #dibujar jugador
        self.player.update()
        self.player.draw(self.capa)

        self.validar_objJugador()
        self.objJugador.draw(self.capa)
        
        #actualiza la brujula
        self.brujulas.sprite.objeto_mas_cercano(self.player,self.sueloBruj)
        self.brujulas.update()
        self.brujulas.draw(self.capa)
        
        self.puntaje.sprite.actualizar_puntaje(self.player.sprite)
        self.puntaje.update()
        self.puntaje.draw(self.capa)
        
        self.barraVida.analizar_vida(self.player.sprite)
        self.barraVida.draw(self.capa)

        self.validar_colisiones()
        