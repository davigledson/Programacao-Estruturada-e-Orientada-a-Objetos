# modifique o programa anterior para escrever, por extenso, numeros de 1 até 100
def unidade(uni):
    if uni ==1: return 'um'
    elif uni ==2: return 'dois'
    elif uni == 3: return 'tres'
    elif uni == 4: return 'quatro'
    elif uni == 5: return 'cinco'
    elif uni == 6: return 'seis'
    elif uni == 7: return 'sete'
    elif uni == 8: return 'oito'
    elif uni == 9: return 'nome'

def dezena(de):

    if de ==2: return 'vinte'
    elif de == 3: return 'trinta'
    elif de == 4: return 'qurenta'
    elif de == 5: return 'cinquenta'
    elif de == 6: return 'sesseta'
    elif de == 7: return 'setenta'
    elif de == 8: return 'oitenta'
    elif de == 9: return 'noventa'

def dezdezenove(num):
    if num == 10: return 'dez'
    if num ==11: return 'onze'
    elif num==12: return 'doze'
    elif num == 13: return 'treze'
    elif num == 14: return 'quatoze'
    elif num == 15: return 'quinze'
    elif num == 16: return 'dezesseis'
    elif num == 17: return 'dezessete'
    elif num == 18: return 'dezoito'
    elif num == 19: return 'dezenove'

def extenso(num):
    if 0 < num < 10: return unidade(num)
    elif num < 20: return dezdezenove(num)
    elif num < 100:
        deze = num // 10 #separa a dezena
        unid = num%10 # separa a unidade
        if unid==0: return dezena(deze)
        else: return dezena(unid) +' e ' + unidade(unid)
    elif num==100: return 'cem'
    else: return 'Numero invalido'


print(extenso(13))