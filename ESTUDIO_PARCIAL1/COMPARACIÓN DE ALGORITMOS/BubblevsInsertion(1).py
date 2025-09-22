def bubble_T(n):
    return 5*n**2

def Insertion_T(n):
    return 2*n**2+20*n

for n in range(1, 1_000_000):
    Tb=bubble_T(n)
    Ti=Insertion_T(n)

    if Ti<Tb:
        print(f"el cruce se da en n igual a {n}")
        break

for n in (1, 10, 1000, 10000, 1_000_000):
    Tb = bubble_T(n)
    Ti = Insertion_T(n)

    if Ti < Tb:
        mejor = "Insertion Sort"
    else:
        mejor = "Bubble Sort"

    print(f"En n={n}, el más rápido es: {mejor}")