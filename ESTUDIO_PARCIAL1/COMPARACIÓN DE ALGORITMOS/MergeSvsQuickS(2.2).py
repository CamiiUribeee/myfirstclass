import math 
def merge_T(n):
    return 40*n*math.log2(n)

def quick_T(n):
    return n**2

for n in range(2, 1_000_000):
    Tm=merge_T(n)
    Tq=quick_T(n)

    if Tm<Tq:
        print(f"el cruce se da en n igual a {n}")
        break

for n in (10, 1000, 10000, 1_000_000):
    Tm=merge_T(n)
    Tq=quick_T(n)

    if Tm<Tq:
        mejor="Merge Sort"
    else:
        mejor="Quick"
    print(f"el mejor caso se da con {mejor}")
    