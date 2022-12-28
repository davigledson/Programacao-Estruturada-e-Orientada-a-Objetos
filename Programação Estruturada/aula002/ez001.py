inicio = int(input('Inicio da sequencia'))
final = int(input('Final da sequencia'))
incr = int(input('Inccremento da sequencia'))

if incr<0:
    incr=incr*-1

if inicio <final:
    print(list(range(inicio,final+1,incr)))
else:
    print(list(range(inicio,final-1,-incr)))