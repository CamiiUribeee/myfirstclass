def hay_duplicados(a):
    vistos = set()  # Conjunto para almacenar elementos únicos  # 1) estructura para recordar lo ya visto
    for elemento in a: # 2) recorremos la lista una vez
        if elemento in vistos:  # 3) ¿ya lo vimos antes?
            return True  # Si ya estaba en el conjunto, hay duplicado    #    sí → hay duplicado
        vistos.add(elemento) # 4) no → lo marcamos como visto
    return False  # Si no se encontró duplicado   # 5) terminamos sin repetir → no hay duplicados

a = [1, 2, 3, 4, 5, 1]
print(hay_duplicados(a))  # True

a2 = [10, 20, 30, 40]
print(hay_duplicados(a2))  # False

a3= [0,0,0,0]
print(hay_duplicados(a3)) 