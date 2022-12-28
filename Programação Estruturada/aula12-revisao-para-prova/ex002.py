#arquivos
# w - gravação
# r - leitura
# a - acrescentar

try:
    arquivo=open('lista.txt','r')

    arquivo.write('Besouro')
    print(arquivo.read())

    arquivo.close()

except FileNotFoundError:
    print('Arquivo não existe')
except:
    print('Arquivo não existe')
