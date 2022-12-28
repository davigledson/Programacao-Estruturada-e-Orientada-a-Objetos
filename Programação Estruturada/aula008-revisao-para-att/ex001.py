def mostralinha():
    print('-'*50)
def bemvindo():
    print('Seja bem vindo!')
    print("Espero que goste.")

mostralinha()
bemvindo()
mostralinha()

def cadastrar(nome):
    print(nome,'foi cadastrado')


cadastrar('davi')
cadastrar('vida')
cadastrar('iavd')
mostralinha()
def operacoes(n1,n2):
    print('soma',n1+n2)
    print('Subração =',n1-n2)
    print('Multiplicação',n1*n2)
    print('Divisão',n1/n2)


operacoes(6,8)

mostralinha()
print(len('davi'))
mostralinha()
def triplo(num):
    return num * 3

total = triplo(3) * triplo(3)
print(total)
mostralinha()

def rendimento(deposito,taxa):
    for x in range(24):
        deposito +=deposito*taxa/100
    return deposito

print(rendimento(500,0.5))

def mul(n1,n2):
    return n1*n2
mostralinha()
print(mul(5,5))
mostralinha()
def modulo(num):
    if num>=0:
        return num
    else:
        return num *-1

print(modulo(-9))