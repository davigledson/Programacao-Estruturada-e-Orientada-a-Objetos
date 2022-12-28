def sequencia(num):
    for c in range(1,num+1,1):
        print(c,end=' ')
    print()

sequencia(7)

def dobro(num):
    return num*2

print(dobro(8))

def quadrado(num):
    return num**2

print(quadrado(10))




def qtdlista(lista):
    contador=0
    for c in lista:
        contador+=1
    return contador

lista=[0,1,2,3,4,5,6,78,8,9,7]
print(qtdlista(lista))