class PirataStats:
    def __init__(self):
        self.puntaje=0
        self.vidas=3
    def modificar_puntaje(self,puntaje):
        self.puntaje+=puntaje
    def modificar_vida(self,vida):
        self.vidas+=vida
