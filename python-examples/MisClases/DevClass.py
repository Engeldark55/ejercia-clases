class Dev:
    def __init__(self, nombre:str,edad:int,nivel:float,lenguajes:list,tipodev:str) -> None:
        self._nombre:str = nombre
        self._edad:int = edad
        self.nivelDev:float = nivel
        self._lenguajes:list = lenguajes
        self.tipoDesarrollador:str = tipodev
    
    #encampulamiento de los atributos
    #NOTA de datos privados: el gion bajo indica una restriccion media para que no modifiqur el dato 
    #el doble guion es una restriccion extrema para que no se modifique nada el dato, 
    #NoTA2: los publicos no hay guion 
    
    #metodos GET obtener o campturar
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @property
    def lenguejes(self):
        return self._lenguajes
    
    #NOTA: si no queremos modidicar un atributo encapsulado eliminamos el SET y asi se combierte en un atributo de solo lectura
    #metodos SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    @lenguejes.setter
    def lenguajes(self, lenguajes):
        self._lenguajes = lenguajes
        
    #metodo str
    def __str__(self) -> str:
        return f"Nombre: {self._nombre}, desarrollador: {self.tipoDesarrollador}, Lenguajes: {self._lenguajes}"
    def __del__(self):
        print(f"el obj {self._nombre} se elimino")

#en listar lenguajes 
"""print(f"los lenguajes con los que a trabajado son: ")
for index, texto in enumerate(dev_obj.lenguajes):  
    print(index, texto)"""
#****************************************************
#               Ejercio de Herencia
#****************************************************
class Persona:
    def __init__(self,nom:str,edad:int) -> None:
        self._nombre:str = nom
        self._edad:int = edad
        
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @edad.setter
    def edad(self,edad):
        self._edad = edad
    
    def __str__(self) -> str:
        return f"Persona: {self._nombre} con {self._edad} años"
    
class Programador(Persona):
    def __init__(self,nom:str, edad:int,sueldo:float) -> None:
        super().__init__(nom, edad)
        self._sueldo:float = sueldo
    
    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo
    
    def __str__(self) -> str:
        return f"{super().__str__()} con sueldo de {self._sueldo}"
    
if __name__ == "__main__":
    person = Persona("lele",1)
    pythonista = Programador("lele",1,1000000)
    print(pythonista)    
    print(person)