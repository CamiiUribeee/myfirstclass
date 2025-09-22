import math
def lineal_T(n):
    return 200*n

def log_T(n):
    return 500*math.log2(n)

for n in range(2, 1_000_000):
    Tl=lineal_T(n)
    Tlog=log_T(n)

    if Tlog<Tl:
        print(f"el cruce se da en n igual a {n}")
        break

for n in[1,10,1000,10000,1_000_000]:
    Tl=lineal_T(n)
    Tlog=log_T(n)

    if Tlog<Tl:
        mejor="Logaritmico"
    else:
        mejor="Lineal"
    print(f"el mas rapido es {mejor}")