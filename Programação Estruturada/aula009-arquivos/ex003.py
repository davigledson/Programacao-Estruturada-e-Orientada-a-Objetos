arq =open("frutas.txt",'r')
for fru in arq:
    print('Eu gosto de',fru,end='')

arq.close()