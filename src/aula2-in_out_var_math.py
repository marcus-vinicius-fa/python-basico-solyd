#/
# BLOCO DE COMENTÁRIOS
# 
# /#

'''
BLOCO DE COMENTÁRIOS
'''

# OUTPUT:

# print() # função para imprimir na tela (console)

# para rodar no console -> Ctrl+Alt+n / no console -> python arquivo.py

print('Hello World!\nSegundo print') # pula linha
print('Hello World!\tSegundo print') # tabulação 'tab'

nome = 'Marcus Vinicius' # variável chamada 'nome' # atribuição do string a variável 'nome' 

print (nome)

# TIPOS DEVARIÁVEIS:

print(type(nome)) # tipo da variável nome = str -> String

idade = 25
print(type(idade)) # tipo da variável nome = int -> 'Inteiro'
# print só imprime texto. O python faz a conversão automatica no caso da função print

altura = 1.85
print(type(altura)) # tipo da variável nome = float = '.'flutuante

#/
# str(string)
# int
# float
# /#

# CONCATENAÇÃO:

# pode ser com '+' ou com ','. Atentar para os espaçamentos e para os tipos
# o python não converte automaticament int para string se usar o simbolo + para concatenar!
print('Olá!\nMe chamo '+ nome +', tenho' ,idade, 'anos de idade e' ,altura, 'de altura.')
print('Olá!\nMe chamo '+ nome +', tenho ' + str(idade) + ' anos de idade e ' + str(altura) + ' de altura.')
# resultados no console são iguais! 
# usando o '+' é possivel salvar a concatenação numa variável!

# INPUT:

print('\n')
nome = input('Qual é o seu nome? -> ')
idade = input('Qual é a sua idade? -> ')
altura = input('Qual é a sua altura? -> ')
print('\n')
print('Olá!\nMe chamo '+ nome +', tenho' ,idade, 'anos de idade e' ,altura, 'de altura.')

print('\n')
# a função input sempre vai retornar um objeto do tipo string! 
print(type(nome), type(idade), type(altura),'\nTodos strings!\n')

# OPERAÇÕES MATEMÁTICAS:

num1 = 20 # poderia ser 20.5 -> float
num2 = 10

# a precedência é: / ou * depois + ou - 
# porém isso pode ficar mais explicito ou 
# para priorizar a gosto uma operação usa-se os parênteses 
# ex: print((num1 + num2) / (num2 - 5))

# operações mais simples

resultado = num1 + num2
print ('Adição -> 20 + 10 =', resultado, '\n') # = 30

resultado = num1 - num2
print ('Subtração -> 20 - 10 =', resultado, '\n') # = 10

resultado = num1 * num2
print ('Multilicação -> 20 * 10 =', resultado, '\n') # = 200

resultado = num1 / num2
print ('Divisão -> 20 / 10 =', resultado, 'ou 2\n') # = 2
# Obs: Não é possível fazer divisão por 0(zero)
# colocar zero no lugar de num2 para ver a saída

resultado = num1 % num2
print ('Resto da divisão -> 20 / 10 = resto', resultado, '\n') # = 0 

resultado = num2 ** 2
print ('Expoente -> 10 **(elevado a) 2 = (10 ao quadrado) =', resultado, '\n') # = 100

resultado = 16 ** (1/2) # num1 elevado a meio = raiz quadrada de 16
print ('Expoente -> 16 **(elevado a) 1/2 = raiz quadrada de 16 =', resultado, '\n') # = 100
# existem outras formas de fazer raiz quadrada 
# porém é usando uma biblioteca