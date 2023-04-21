#comparacuiones
def igualdad(a,b):
    print(f"el valor de a: {a}, y el valor de b: {b}")
    if a == b:
        return True
    
def Noigual(a,b):
    print(f"el valor de a: {a}, y el valor de b: {b}")
    return a,b

#V o F
def Is_vf_X(x):
    if x == True:
        print(f"valor es {x}")
        return True
    else: 
        print(f"valor es {x}")
        return False
        

#existe un elemento en lista
def veri_lis():
    l = [1,2,3,4]
    return l