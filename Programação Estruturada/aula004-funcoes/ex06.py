def primo(num):

    contador=0
    for c in range(num,1,-1):
        if num%c==0:
            contador+=1



    if contador>=2:
        print(f'Não é primo tem {contador} divisores')
    else:
        print('é primo')



primo(7)