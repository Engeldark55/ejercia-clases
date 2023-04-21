class Dev:
    def __init__(self) -> None:
        self._nombre:str = "engel"
        self._edad:int = 26
        self.nivelDev:float = 7.0
        self._lenguajes:list = ["Python","JS","html","css"]
        self.tipoDesarrollador:str = "junior"
    
    #encampulamiento de los atributos
    #NOTA de datos privados: el gion bajo indica una restriccion media para que no modifiqur el dato 
    #el doble guion es una restriccion extrema para que no se modifique nada el dato, 
    #NoTA2: los publicos no hay guion 
    
    #metodos GET obtener o campturar
    @property
    def nombre(self):
        return self._nombre
    def edad(self):
        return self._edad
    def lenguejes(self):
        return self._lenguajes
    
    #metodos SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    #metodo str
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, desarrollador: {self.tipoDesarrollador}"
    
    
dev_obj = Dev()
dev_obj.nombre = "lele"
print(dev_obj.nombre)


#en listar lenguajes 
"""print(f"los lenguajes con los que a trabajado son: ")
for index, texto in enumerate(dev_obj.lenguajes):  
    print(index, texto)"""
