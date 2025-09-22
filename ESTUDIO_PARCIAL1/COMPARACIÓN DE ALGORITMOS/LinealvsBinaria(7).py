import math
def lineal_T(n):
    return 5*n

def binaria_T(n):
    return 100*math.log2(n)

for n in range(2,1_000_000):
    Tl=lineal_T(n)
    Tb=binaria_T(n)

    if Tb<Tl:
        print(f"el cruce se da en n igual a {n}")
        break

for n in range(2,10000):
    if n> 20*math.log2(n):
        print(f"el cruce se da en n igual a {n}")
        break

for n in[10,100,1000,10000,1_000_000]:
    Tl=lineal_T(n)
    Tb=binaria_T(n)

    if Tb<Tl:
        mejor="Binario"
    else:
        mejor="Lineal"
    print(f"el mas rapido es {mejor}")