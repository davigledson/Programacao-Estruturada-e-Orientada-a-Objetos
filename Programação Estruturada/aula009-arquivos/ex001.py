
try:
    arquivo = open("d:\\Users\\20221024110001\\Documents\\2°Período\\alunos.txt",'r')
    print(arquivo.read())

except FileNotFoundError:
    print('Arquivo não encontrado')

except:
    print('ERRO DESCONHECIDO')

finally:
    arquivo.close()

