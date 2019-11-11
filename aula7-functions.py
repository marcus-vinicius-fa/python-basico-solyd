# Funções Built-in -> Acopladas

print('Olá mundo') # print(parametros)

print(len('Olá mundo'))

# Fazer minhas próprias funções

# o próprio '+' é uma função soma

def soma(num1, num2):
  return num1 + num2 # ou colocar num1 + num2 numa variável e return na variavel

print(soma(20, 30))

# função sem retorno e sem argumento

def imprime_oi():
  print('Oi')

imprime_oi()

for i in range(5):
  imprime_oi()

def tem_set(num):
  if num == 7:
    return True
  else:
    return False

if tem_set(7):
  print('É 7')
else:
  print('Não é 7')

# PARÂMETROS DEFAULT

# Todos parametros default

# def mostrar_login(usuario='root', senha='123'):
#   print('Usuário', usuario)
#   print('Senha', senha)
#
# mostrar_login()
# mostrar_login(marcus)
# mostrar_login(marcus, 321)

# Mistura -> Parametro default + Parametro obrigatório

# def mostrar_login(sistema, usuario='root', senha='123'):
#   print('Sistema:', sistema)
#   print('Usuário:', usuario)
#   print('Senha:', senha)
#
# mostrar_login(nome_sistema)
# mostrar_login(nome_sitema, marcus)
# mostrar_login(nome_sistema, marcus, 321)

def login(usuario='root', senha='123'):
  if (usuario == 'root' or usuario == 'marcus') and (senha == '123' or senha == '321'):
    print('Acesso permitido!')
  else:
    print('Acesso negado!')

login('marcus', '321')

login()

login('outro', '456')

login('marcus', '123')
login('marcus')

login('marcus', '456')