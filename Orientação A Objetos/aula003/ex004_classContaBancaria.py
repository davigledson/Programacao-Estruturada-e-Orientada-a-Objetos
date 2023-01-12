'''depositar() – pergunta o valor e acrescenta ao saldo.
sacar() – pergunta o valor, pergunta a senha, se a senha estiver correta e o saldo for suficiente, efetua o
saque, caso contrário, exibe as mensagens “senha incorreta” ou “saldo insuficiente”.
extrato() – exibe o nome do titular e o saldo atual.
Desenhe o diagrama da classe.
Obs: Se desejar, use o seguinte código para solicitar a senha sem exibi-la na tela:
import getpass
senha = getpass.getpass(prompt="Senha: ")'''
class ContaBancaria():
    titular=''
    saldo=0
    senha=''

    def __init__(self, ptitular, psaldo, psenha):
        self.titular= ptitular
        self.saldo = psaldo
        self.senha = psenha

    def depositar(self):
        pvalor=float(input('Qual o valor?'))

        self.saldo=self.saldo+pvalor

    def sacar(self):
        pvalor=float(input('Qual o valor a ser sacado?'))

        psenha = int(input('qual a senha?'))
        if psenha != self.senha:
            print('Senha incorreta')
        else:
            print('dinheiro sacado!')

        if pvalor > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saldo = self.saldo - pvalor



    def extrato(self):
        print(f'Titular = {self.titular}')
        print(f'Saldo Atual = {self.saldo}')

banco=ContaBancaria('davi',20,1234)
banco.extrato()
banco.sacar()
banco.extrato()
banco.depositar()
banco.extrato()