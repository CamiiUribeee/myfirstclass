def cuadratico_T(n):
    return n**2+100*n

def cubico_T(n):
    return n**3

for n in range(2,1_000_000):
    Tcua=cuadratico_T(n)
    Tcu=cubico_T(n)
    if Tcua<Tcu:
        print(f"el cruce se da en n igual a {n}")
        break

for n in[1,10,20,30,40,100]:
    Tcua=cuadratico_T(n)
    Tcu=cubico_T(n)
    if Tcua<Tcu:
        mejor="Cuadrático"
    else:
        mejor="Cúbico"
    print(f"el mas rapido es {mejor}")

