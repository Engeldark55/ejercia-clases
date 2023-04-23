from Figuras import Figura 
from Colores import Color
class Cuadrado(Figura,Color):
    def __init__(self, lado: int, color: str) -> None:
        self._lado = lado
        self._color = color
        Figura.__init__(self,lado,lado)
        Color.__init__(self,color)
    @property
    def lado(self):
        return self._lado
    @property
    def color(self):
        return self._color
    @lado.setter
    def lado(self,lado):
        self._lado = lado
    @color.setter
    def color(self,color):
        self._color = color
        
    def __str__(self) -> str:
        return f"el lado ingresado es: {self._lado}"
    def cal_area(self):
        return self._lado * self._lado