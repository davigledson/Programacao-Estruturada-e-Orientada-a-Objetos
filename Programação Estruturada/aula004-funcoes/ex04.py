def diadasemana(dia):
    if dia==1:
        return ('Domingo')
    elif dia ==2:
        return('Segunda-feira')
    elif dia==3:
        return('Terça feira')
    elif dia==4:
        return('Quarta-feira')
    elif dia==5:
        return('Quinta-feira')
    elif dia==6:
        return('Sexta-feira')
    elif dia==7:
        return('Sabado-feira')
    else:
        return('numero invalido')

diadasemana(6)
import datetime
hj=datetime.datetime.today().weekday()+2
print(diadasemana(hj))