from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado
from orden import Orden

if __name__ == "__main__":
    #creando componenetes
    Monitor_1:object = Monitor("HP","25P")
    Teclado_1:object = Teclado("HP","USB")
    Raton_1:object = Raton("HP","USB")
    #computadoras echas
    cpu_01:object = Computadora("HP-2305p",Raton_1,Teclado_1,Monitor_1)
    cpu_02:object = Computadora("HP00p",Raton_1,Teclado_1,Monitor_1)
    #creando listados cpu`s
    computadoras:list = [cpu_01, cpu_02]
    orden_01:object = Orden(computadoras)
    #visualizar orden
    print(orden_01)