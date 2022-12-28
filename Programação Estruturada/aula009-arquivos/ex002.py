try:
    arq = open("frutas.txt","w")
    while True:
        fru = input('Digite a fruta:')
        arq.write(fru +"\n")

        continua = input('Outra? (s/n)')
        if continua =='n':
            break
except :
    print('ERRO')
finally:

    arq.close()

