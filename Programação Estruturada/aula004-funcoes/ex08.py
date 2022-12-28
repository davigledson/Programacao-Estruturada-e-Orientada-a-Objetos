def multiplos(num):
    lista=[]
    for c in range(1,11,1):
        lista.append(c*num)
    return lista


print(multiplos(19))