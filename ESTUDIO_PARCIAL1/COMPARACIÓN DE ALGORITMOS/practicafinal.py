#Burbuja vs inserción 

def bubble_T(n):
    return 5*n**2

def insertion_T(n):
    return 2*n**2+20*n

for n in range(1,1_000_000):
    Tb=bubble_T(n)
    Ti=insertion_T(n)

    if Ti<Tb:
        print(f"El cruce se da en n igual a {n}")
        break

for n in[1,10,20,100,1000,10000]:
    Tb=bubble_T(n)
    Ti=insertion_T(n)

    if Ti<Tb:
        mejor="Insertion"
    else:
        mejor="Bubble"
    
    print(f"para n igual a {n} el mejor caso es {mejor}")