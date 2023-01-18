from ex001_classIngresso import Ingresso

class IngressoVIP(Ingresso):
    valorAdicional =0
    def info(self):
        print('Valor VIP = R$', self.valor + self.valorAdicional)


vip1=IngressoVIP()
vip1.valor=30
vip1.valorAdicional = 60
vip1.info()

