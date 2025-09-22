import math
def solucionIngenua_T(n):
    return n**2

def divideyVencer_T(n):
    return 25*n*math.log2(n)

for n in range(2,1_000_000):
    Tsi=solucionIngenua_T(n)
    Td=divideyVencer_T(n)
    if Td<Tsi:
        print(f"el cruce se da en n igual a {n}")
        break

for n in[100,200,300,400,1_000_000]:
    Tsi=solucionIngenua_T(n)
    Td=divideyVencer_T(n)
    if Td<Tsi:
        mejor="Divide y vencerás"
    else:
        mejor="soluciín ingenua"
    print(f"el mas rapido es {mejor}")
    
    