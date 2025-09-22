def fibonacci_T(n):
    return 2**n

def programacionD_T(n):
    return 10*n

for n in range(2,1_000_000):
    Tf=fibonacci_T(n)
    Tp=programacionD_T(n)
    if Tp<Tf:
        print(f"el cruce se da en igual a {n}")
        break

for n in[2,4,6,8,10,20]:
    Tf=fibonacci_T(n)
    Tp=programacionD_T(n)
    if Tp<Tf:
        mejor="Programación dinámica"
    else:
        mejor="Fibonacci"
    print(f"el mejor es {mejor}")
    