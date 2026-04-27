#Criando a classe Veiculo e definindo seus atributos
class Veiculo():
    def __init__ (self, ano, preco, modelo):
        self.ano = ano
        self.preco = preco
        self.modelo = modelo

    #Criano o método calcular imposto que será passado as classes filhas   
    def calcular_imposto(self):
        return 0.10 * self.preco

# Criando a classe filha Carro   
class Carro(Veiculo):
    def __init__ (self, ano, preco, modelo, marca):
        #Passando os atributos e o método calcular imposto para essa classe filha
        super().__init__(ano, preco, modelo)
        self.marca = marca
    
    #Criando o método desconto
    def desconto(self):
        return 0.05 * self.preco
    
class Moto(Veiculo):
    def __init__ (self, ano, preco, modelo, cilindrada):
        #Passando os atributos e o método calcular imposto para essa classe filha
        super().__init__(ano, preco, modelo)
        self.cilindrada = cilindrada
    
    #Reescrevendo o método calcular imposto
    def calcular_imposto(self):
        return 0.05 * self.preco
    
#Instanciando as classes
carro1 = Carro(1962, 38000000.00, "Ferrari 250 GTO", "Ferrari")
moto1 = Moto(1990, 139950.00, "Harley-Davidson Fat Boy", 1923)

#Criando uma lista
veiculos = [carro1, moto1]
#Usando a lista para imprimir o método calcular imposto de cada objeto
for veiculo in veiculos:
    print (f"Imposto do veículo {veiculo.modelo} R$: {veiculo.calcular_imposto()}")
