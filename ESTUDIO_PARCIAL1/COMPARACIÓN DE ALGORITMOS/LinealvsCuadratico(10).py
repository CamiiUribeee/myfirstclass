def lineal_T(n):
    return 1000*n

def cuadratico_T(n):
    return 0.5*n**2

for n in range(1,1_000_000):
    Tl=lineal_T(n)
    Tc=cuadratico_T(n)

    if Tl<Tc:
        print(f"el cruce se da en n igual a {n}")
        break