
#****************************************************
#             Ejercio de Herencia multiple
#****************************************************

class Figura:
    def __init__(self, alto:int, ancho:int) -> None:
        self._alto:int = alto
        self._ancho:int = ancho
        
    @property
    def alto(self):
        return self._alto
    @property
    def ancho(self):
        return self._ancho
    @alto.setter
    def alto(self,alto):
        self._alto = alto
        
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
