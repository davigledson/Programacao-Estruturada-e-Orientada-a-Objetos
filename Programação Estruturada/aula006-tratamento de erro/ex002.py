try:
    n1=int(input('Digite Numerador:'))
    n2=int(input('Digite o denominador:'))
    print('A divisão da:',n1/n2)
except ValueError:
    print('ERRO. O valor digitado não é válido')
except ZeroDivisionError:
    print('ERRO!. Divisão por zero')