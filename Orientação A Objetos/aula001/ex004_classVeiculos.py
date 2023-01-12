class veiculos:

    def __init__(self, fabricante, modelo,ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano=ano

v1=veiculos('uno','novo',2000)
v2=veiculos('gol','neymar',2022)
v3=veiculos('tesla','cybertruck',2225)

print(f'Eu comprei um {v1.fabricante} modelo {v1.modelo} em {v1.ano}')
print(f'Eu comprei um {v2.fabricante} modelo {v2.modelo} em {v2.ano}')
print(f'Eu comprei um {v3.fabricante} modelo {v3.modelo} em {v3.ano}')