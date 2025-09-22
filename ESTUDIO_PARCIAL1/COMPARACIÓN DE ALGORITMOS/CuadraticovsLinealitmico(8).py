import math
def cuadratico_T(n):
    return n**2

def linealitmico_T(n):
    return 50*n*math.log2(n)

for n in range(2,1_000_000):
    Tc=cuadratico_T(n)
    Tl=linealitmico_T(n)

    if Tl<Tc:
        print(f"el cruce se da en n igual a {n}")
        break

for n in[10,100,1000,10000,1_000_000]:
    Tc=cuadratico_T(n)
    Tl=linealitmico_T(n)

    if Tl<Tc:
        mejor="algoritmo B"
    else:
        mejor="algoritmo A"
    print(f"el mas rapido es {mejor}")