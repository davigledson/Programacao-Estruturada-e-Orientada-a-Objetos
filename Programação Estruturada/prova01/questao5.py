def qtdPassageiros(num):
    num=int(input('Quantidade de Passageiros:'))
    if num == 1:
        return 'Motocicleta'
    elif num <= 4:
        return 'Automovel'
    elif num <= 8:
        return 'Minivan'
    elif num <= 14:
        return 'Van'
    elif num <= 20:
        return 'Micro-Ônibus'
    elif num <= 50:
        return 'Ônibus'
    else:
        return 'Digite numeros entre 0 e 50!'



print(qtdPassageiros(25))