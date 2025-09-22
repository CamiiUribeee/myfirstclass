import math 

def lineal_T(n):
    return 200 * n

def logaritmico_T(n):
    return 500 * math.log2(n)

for n in range(2,1_000_000): #para un valor de cruce estrictamente puntual 
    Tli=lineal_T(n)
    Tlog=logaritmico_T(n)

    if Tlog<Tli:
        print(f"el cruce se da en n igual a {n}")
        break

for n in range(2, 100):
    if n/math.log2(n)>2.5:
        print(f"el cruce se da APROXIMADAMENTE en n igual a {n}")
        break


for n in[1, 5, 7, 8, 20, 100, 1_000_000]:
    Tli=lineal_T(n)
    Tlog=logaritmico_T(n)
    if Tlog<Tli:
        mejor="Logaritmico"
    else:
        mejor="Lineal"

    print(f"mas rapido: {mejor}")
