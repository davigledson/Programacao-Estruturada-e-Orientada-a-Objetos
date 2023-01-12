class Copo:
    material = ""
    cor = ""
    capacidade = 0
    atual = 0

    def __init__(self, mat, cor, cap):
        self.material = mat
        self.cor = cor
        self.capacidade = cap

    def info(self):
        print(f"Copo de {self.material} {self.cor} {self.capacidade} ml tem {self.atual} ml agora.")

    def encher(self):
        self.atual = self.atual + 50
        if self.atual > self.capacidade:
            print("Derramou.")
            self.atual = self.capacidade
        print(f"Atual: {self.atual}/{self.capacidade} ml.")

    def esvaziar(self):
        self.atual = self.atual - 50
        if self.atual < 0:
            self.atual = 0
        print(f"Atual: {self.atual}/{self.capacidade} ml.")
        if self.atual <= 0:
            print("Acabou.")


####################################

c1 = Copo("Plástico", "Vermelho", 300)  # criar o objeto
c1.info()

c1.encher()
c1.encher()

c1.esvaziar()
c1.esvaziar()
c1.esvaziar()