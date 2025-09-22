# Bublle vs insertion 

def bubble_T(n):
    return 5*n**2

def insertion_T(n):
    return 2*n**2+20*n

for n in range(2,1_000_000):
    Tb=bubble_T(n)
    Ti=insertion_T(n)

    if Ti<Tb:
        print(f"el cruce se da en n igual a {n}")
        break

for n in[1,5,10,20,100,1000]:
    Tb=bubble_T(n)
    Ti=insertion_T(n)

    if Ti<Tb:
        mejor="Insertion"
    else:
        mejor="Bubble"
    print(f"el mas rapido es {mejor}")
