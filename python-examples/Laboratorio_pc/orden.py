class Orden:
    Contador_id = 0
    def __init__(self,computadoras:str) -> None:
        Orden.Contador_id += 1
        self._id:int = Orden.Contador_id 
        self._computadoras:list = computadoras
        
    def add_pcu(self,computadora):
        self._computadoras.append(computadora)
    def __str__(self) -> str:
        cpu_str = ''
        for cpu in self._computadoras:
            cpu_str += cpu.__str__()
        return f"""
                order: {self._id} 
                cpu`s: -> {cpu_str}
                """
    @property
    def id(self):
        return self._id
    @property
    def computadoras(self):
        return self._computadoras