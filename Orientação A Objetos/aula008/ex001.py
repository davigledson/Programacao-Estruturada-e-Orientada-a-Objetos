# Passou uma lista de exercicios para fazer
'''
PROGRAMAÇÃO ORIENTADA A OBJETOS - EXERCÍCIOS SOBRE HERANÇA – PROF. ABRAHÃO LOPES
1. Crie uma classe chamada Ingresso que possua um atributo valor e um método info() que retorne à informação
do valor do ingresso.
a. Crie uma classe IngressoVIP, que herda de Ingresso e possui um atributo valorAdicional. O método info()
da classe IngressoVIP deve considerar que o valor do ingresso é o valor da superclasse somado ao valor
Adicional do IngressoVIP.
b. Crie uma classe para testar os objetos das classes Ingresso e IngressoVIP.
c. Desenhe o diagrama de classes que representa essa herança.
2. Crie uma classe chamada Empregado com os atributos nome e salário. Crie os métodos get e set para esses
atributos e um método info() que imprime os dados do empregado.
a. Crie uma classe Gerente que herda de empregado e possui o atributo departamento. Crie os métodos
get e set, o método __init__() para preencher todas as informações e o método info() para imprimir os
dados do gerente, incluindo as informações herdadas.
b. Crie uma classe Vendedor que também herda de empregado e possui o atributo percentualComissao.
Essa classe deve ter um método chamado calcularSalario(), que retorna o valor do salário acrescido do
percentual de comissão. O método __init__() deve receber todos dos dados ao criar um objeto. O método
info() deve mostrar o nome, o salário sem comissão, o percentual da comissão e o salário total (com a
comissão).
c. Desenhe o diagrama de classes que representa essa herança.
3. Crie uma classe chamada Transporte com os atributos fabricante, ano e modelo. Métodos get/set, init e info
que exibe todos os dados do objeto.
a. Crie a classe Carro que herda de transporte e tem o atributo qtdPortas e o método abrirPortaMalas() que
exibe uma mensagem informando que o porta-malas foi aberto. *
b. Crie a classe Moto que herda de transporte e tem o atributo cilindradas e o método empinarRoda() que
exibe uma mensagem informando que a roda dianteira foi erguida. *
c. Crie a classe Avião que herda de transporte e tem os atributos qtdPassageiros e posição (registra se o avião
está no chão ou no ar, ao criar o objeto, sempre estará no chão) e os métodos decolar() e pousar(). O avião
só pode decolar se estiver no chão e só pode pousar se estiver no ar. *
* Adicione métodos get/set, init e info em todas as classes a fim de contemplar todos os dados.
d. Desenhe o diagrama de classes que representa essa herança.
4. Crie uma classe Imóvel que possui os atributos tipo (casa, apartamento, loja, etc.), endereço, valor. Crie
métodos get/set, init e info.
a. Crie uma classe ImóvelNovo que herda de imóvel e acrescenta o atributo construtora.
b. Crie uma classe ImóvelUsado que herda de imóvel e acrescente os atributos proprietário e tempoDeUso.
c. Desenhe o diagrama de classes que representa essa herança.
'''