# Uma superclasse, funciona como uma interface

class Veiculo: # convenção iniciar class com a primeira letra maiúscula

  def __init__(self, cor, marca, dono): # essa função é um construtor ele passa ele mesmo (self) pra dentro, semelhante ao this
    self.cor = cor
    self.marca = marca
    self.dono = dono
    self.tanque = 0

  def toString(self):
    print('O veículo pertence a '+str(self.dono)+', a marca é '+str(self.marca)+', de cor '+str(self.cor))

  def abastecer(self, litros):
    self.tanque += litros