# Type Bool -> Boolean = true-false / Tipo Booleano verdadeiro-falso

var_verdadeiro = True
var_falso = False

print (type(var_verdadeiro), type(var_falso))
print (var_verdadeiro)

# Usado para tomar decisões atraves da estrutura 'if'
# IF -> 'se'
# ELSE -> 'senão'
# ELIF -> ELIF + IF -> 'senão se'

if var_verdadeiro == True: # 2 iguais não é para atribuir mas sim comparar valores
  print('var_verdade é verdadeiro!')
  # Notar estrutura de identação (o espaçamento)

# Outros tipos de comparação: 
# 
# <=, >=, <, >, ==, !=

# Operadores lógicos:
# 
# and, or, not
#
# 1 == 1 and 1 != 2 = True
# True and True = True
#
# And -> exclusivo (satisfazer os 2 requisitos)
# Or -> inclusivo (1 requisito basta)
# Not -> negação (nega valor ex: not True = False)

print('\n')

if 2 > 1:
  print (True)

else: # Basta aninhar identações para permanescer na estrutura de decisão if
  print (False)

a = 50
b = 20

if a > b and 'abacaxi' == 'uva': # troque 'uva' por 'abacaxi'
  print (True)

else: # O else funciona como um default(padrão) vai cair nele caso não caia nas comparações acima
  print (False)

# MENU:

print('\nMenu:\n1 = Escreve Python\n2 = Escreve JavaScript\n3 = Escreve NodeJS\n')
opcao = input('Escolha uma opção: ')

# Lógica do pograma (como ele funciona)
if opcao == '1': # Lembrando: O retorno de um input é sempre um STRING!
  print ('Go Python!')
elif opcao == '2':
  print ('Go JavaScript!')
elif opcao == '3':
  print ('Go Node!')
else:
  print ('Opção inválida!')

# Poderiam ser vários ifs ao invés do elif, 
# porém o programa verificaria todos os ifs 
# mesmo que a primeira condição fosse a correta

# O uso do NOT:

verdade = True

# tirar o not para ver o resultado
if not verdade: # O resultaod é False (negação do True)
  print ('Entrou no if')
else:
  print ('Entrou no else')