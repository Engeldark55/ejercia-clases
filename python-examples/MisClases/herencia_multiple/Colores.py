
#****************************************************
#             Ejercio de Herencia multiple
#****************************************************

class Color:
    def __init__(self, color:str) -> None:
        self._color:int = color

        
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color
        
