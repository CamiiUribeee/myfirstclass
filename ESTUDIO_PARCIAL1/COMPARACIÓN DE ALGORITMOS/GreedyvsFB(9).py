def fuerzaB_T(n):
    return 2**n

def greedy_T(n):
    return 20*n**2

for n in range(2,1_000_000):
    Tfb=fuerzaB_T(n)
    Tg=greedy_T(n)

    if Tg<Tfb:
        print(f"el cruce se da en n igual a {n}")
        break
    