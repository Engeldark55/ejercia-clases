class Monitor:
    contador_order = 0
    def __init__(self, marca:str, tamano:str) -> None:
        Monitor.contador_order += 1
        self._id:int = Monitor.contador_order
        self._marca:str = marca
        self._tamano:str = tamano
        
    def __str__(self) -> str:
        return f"id:{self._id} marca: {self._marca} Tipo:{self._tamano}"
    
    @property
    def id(self):
        return self._id
    @property
    def marca(self):
        return self._marca
    @property
    def tamano(self):
        return self._tamano
    
    @id.setter
    def id(self,id):
        self._id = id
    @marca.setter
    def marca(self,mar):
        self._marca = mar
    @tamano.setter
    def tamano(self,tam):
        self._tamano = tam