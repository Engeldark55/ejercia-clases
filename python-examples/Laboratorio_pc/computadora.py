
class Computadora:
    contador = 0
    def __init__(self,nombre,raton,teclado, monitor) -> None:
        Computadora.contador += 1
        self._id = Computadora.contador
        self._nombre = nombre
        self._raton  = raton
        self._teclado = teclado
        self._monitor = monitor
    def __str__(self) -> str:
        return f"""
            Nombre: {self._nombre}
            Monitor: {self._monitor}
            teclado: {self._teclado}
            raton: {self._raton}
        """
    #Metodos GET
    @property
    def nombre(self):
        return self._nombre
    @property
    def raton(self):
        return self._raton
    @property
    def teclado(self):
        return self._teclado
    @property
    def monitor(self):
        return self._monitor
    #GET solo lectura
    @property
    def id(self):
        return self._id
    
    #metodos SET
    @nombre.setter
    def nombre(self,nom):
        self._nombre = nom
    @raton.setter
    def raton(self,raton):
        self._raton = raton
    @teclado.setter
    def teclado(self,tec):
        self._teclado = tec
    @monitor.setter
    def monitor(self,moni):
        self._monitor = moni