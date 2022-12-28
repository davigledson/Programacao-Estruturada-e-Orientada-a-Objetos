lista=['cha','leite','agua','chá','refrigerante']


try:
    op = int(input('Digite um número 0 e 4:'))
    print('Você escolheu:', lista[op])
except IndexError:
    print('ERRO. Essa opção/ posição não existe')

except ValueError:
    print('ERRO. O valor digitado não é aceito')