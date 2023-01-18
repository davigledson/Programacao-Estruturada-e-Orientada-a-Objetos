from ex010_classImovel import  Imovel

class ImovelVelho(Imovel):
    def __init__(self, tipo, endereco, valor, construtora,proprietario, tempoDeUso ):
        super().__init__(tipo, endereco, valor)
        self.construtora = construtora
        self.proprietario = proprietario
        self.tempoDeUso =  tempoDeUso

    def setConstrutora(self, construtora):
        self.construtora = construtora

    def getConstrutora(self):
        return self.construtora

    def setProprietario(self, proprietario):
        self.proprietario = proprietario

    def getProprietario(self):
        return self.proprietario

    def setTempoDeUso(self, tempoDeUso):
        self.tempoDeUso = tempoDeUso

    def getTempoDeUso(self):
        return self.tempoDeUso
    def info(self):
        super().info()
        print('Construtora:',self.construtora)
        print('Proprietario:',self.proprietario)
        print('Tempo de uso:',self.tempoDeUso)

casavelha=ImovelVelho('casa','centro',30000,
                      'Contruçoes 3d','banco','30 anos')

casavelha.info()