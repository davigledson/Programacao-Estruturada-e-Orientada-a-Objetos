try:
    n=int(input('Digite um número:'))
    print(n+'legal')
except (TypeError,ValueError):
    print('ERRO')