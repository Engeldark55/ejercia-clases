from dispositivo_entrada import DispositivoEntrada 

class Raton(DispositivoEntrada):
    contador_order = 0
    def __init__(self, marca:str, tipo_entrada:str) -> None:
        Raton.contador_order += 1
        self._id:int = Raton.contador_order
        super().__init__(marca, tipo_entrada)
        
    def __str__(self) -> str:
        return f"id:{self._id} marca: {self._marca} Tipo:{self._tipo_entrada}"
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id = id
        
if __name__ == "__main__":
    raton = Raton("HP","USB")
    print(raton)
    print(raton)