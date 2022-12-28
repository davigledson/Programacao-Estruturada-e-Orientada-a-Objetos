#erros
try:
    v1=int(input('Digite um numero:'))
    v2=int(input('Digite outro numero:'))
    print('A divisão é',v1/v2)

except ValueError:
    print('erro de digitação')

except ZeroDivisionError:
    print('Divisão por zero não é aceita')

except:
    print('Erro Desconhecido')

finally:
    print('Até a proxima')