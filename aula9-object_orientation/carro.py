from veiculo import Veiculo

# se define um objeto através de uma classe, ela é a receita do objeto

class Carro(Veiculo): # Herança, extends..

  def __init__(self, cor, marca, dono):
      super().__init__(cor, marca, dono) ## super referencia a classe pai no caso Veiculo # tô passando pro construtor da class pai.
      # se não colocar o super, usar Veiculo.__init__

#   def __init__(self, cor, marca, dono): # essa função é um construtor ele passa ele mesmo (self) pra dentro, semelhante ao this
#     self.cor = cor
#     self.marca = marca
#     self.dono = dono
#     self.tanque = 0
    # faz tipo injeção de dependência forçando os atributos na class?
    # basta adicionar atributos aqui (modularidade)

  # Override
  def toString(self): # As funções têm que ter o argumento self
    # bem semelhante ao this de java, o self
    print('O carro pertence a '+str(self.dono)+', a marca é '+str(self.marca)+', de cor '+str(self.cor))

  def abastecer(self, litros): # Sobrescrição de métodos da superclasse
    if (self.tanque + litros) > 50:
      print("O tanque está cheio.")
      self.tanque = 50
    else:
      self.tanque += litros