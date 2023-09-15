from tiles import Tile
from random import randint
from ajustes import tamaño_recuadro
class Nivel:
    def __init__(self,bombas, capa):
        self.estructura=["          ",
                        "          ",
                        "          ",
                        "          ",
                        "          ",
                        "          "]
        self.capa=capa
        self.tesoro=1
        self.bombas=bombas
        self.generar_nivel()
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
        self.ubicar_elemento(self.tesoro,"T")
    def ubicar_nivel(self):
        pass
    def run(self):
        pass