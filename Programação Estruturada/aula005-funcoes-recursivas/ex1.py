def soma(n):
    if n==1:
        return 1
    else:
        return n + soma(n-1)

print(soma(5))

def fatorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(4))

def potencia(base,expoente):
    if expoente==0:
        return 1
    else:
        return base * potencia(base,expoente-1)

print(potencia(2,3))