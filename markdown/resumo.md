[home](../README.md) | [ferramentas](./ferramentas.md)

# Python

>O básico da linguagem...

<br/>

Utilize [esse tutorial](./ferramentas.md) para configurar um ambiente mais agradável para trabalhar com Python.

*Uso no Windows

### Sumário

1. [Iniciando no VSCode](##iniciando-no-vscode)
1. [Olá Mundo](##olá-mundo)
1. [Comentários](##comentários)
1. [Entrada e Saída](##entrada-e-saída)
1. [Tipos](##tipos)
1. [Variáveis](##variáveis)
1. [Operadores Matemáticos](##operadores-matemáticos)
1. [Operadores Condicionais](##operadores-condicionais)
1. [Controladores de Fluxo](##controladores-de-fluxo)
1. [Strings](##strings)
1. [Listas](##listas)
1. [Estruturas de Laço](##estruturas-de-laço)
1. [Dicionários](##dicionários)
1. [Tuplas](##tuplas)
1. [Sets ou Conjuntos](##sets-ou-conjuntos)
1. [Importação e Uso de Bibliotecas](##importação-e-uso-de-bibliotecas)
1. [Funções](##funções)
1. [Argumentos para CLI](##argumentos-para-cli)
1. [Trabalhando com Arquivos](##trabalhando-com-arquivos)
1. [Tratamento de erros](##tratamento-de-erros)
1. [Requisições HTTP](##requisições-http)
1. [Manipulação de JSON](##manipulação-de-json)

## Iniciando no VSCode

Para começar a trabalhar com Python no VSCode siga os passos a seguir

Com o Cmder/cmd/powershell aberto navegue até o diretório onde deseja guardar os seus códigos.

~~~powershell
# use o a tecla tab para autocompletar o nome das pastas
> cd "nome-do-dir/nome-do-dir/"
~~~

Na pasta digite

~~~powershell
# esse comando serve para abrir o vscode na pasta atual
> code .
~~~

Você também pode ir pela interface de usuário, navegando até a pasta desejada. Quando estiver nela clique com o botão direito do mouse no vazio e selecione **Open with Code (Abrir com o Code)** e pronto.

---

## Olá Mundo

Faz parte do "ritual de iniciação" escrever um código que não faça nada além de imprimir no console _"Hello World"_ .

Clique em novo arquivo ou dê um duplo clique na parte vazia do editor, em seguida use **Ctrl + s** para selvar o arquivo. pode ser **"ola-mundo\.py"**, essa é a extensão de um arquivo Python. Feito isso o editor já reconhece a extensão e está pronto para trabalhar com a linguagem.

Escreva:

~~~python
# pode usar aspas simples ou duplas
# o print serve para lançar no console
print('Olá Mundo!')
~~~

Dê um **Ctrl + s** para salvar e em seguida clique na pasta ou no arquivo com o botão direito e selecione **"Abrir no terminal"**. digite **"python ola-mundo\.py"**. Outra forma é com o comando **Ctrl + shift + p** e digitando **"Python: Executar Arquivo no Terminal"**, pressione enter. Ou próximos códigos serão executados de uma dessas duas formas.

---

## Comentários

A palavra reservada para comentarios simples é o hashtag (jogo da velha) e para um bloco de comentário usa-se três aspas simples como no exemplo.

~~~python
# comentario simples

'''
bloco
de
comentario
'''
~~~

---

## Entrada e Saída

~~~python
# exemplos de entradas (input) de dados
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")

# type serve para verificar o tipo do objeto
# a função input sempre vai retornar um objeto do tipo "str"
print(type(nome), type(idade), type(altura), '\nTodos strings!\n')

# saida (output)
print("Essa é uma saída")

# \n e a palavra reservada para "pular linha"
print("Essa é uma saída\nEssa é uma nova linha")

# \t da um tab antes da impressao
print('Essa é uma saída\tEssa é uma saída tabulada')
~~~

Usa-se "+" e "," para **concatenar (juntar)** textos.

~~~python
# resultados no console são iguais
# usando o "+" é possivel salvar a concatenação numa variável
# usando "," os tipos não presisam ser convertidos
# usa-se str(variavel) para convertar para um tipo, no caso para string
print('Olá!\nMe chamo ' + nome + ', tenho', idade,
      'anos de idade e', altura, 'de altura.')

print('Olá!\nMe chamo ' + nome + ', tenho ' + str(idade) +
      ' anos de idade e ' + str(altura) + ' de altura.')
~~~

---

## Tipos

~~~python
# bool - boolean
# True ou False - verdadeiro ou falso
print(type(True))

# int - inteiro
print(type(25))

# float - ponto flutuante
print(type(1.85))

# str - string - texto
print(type('texto 1'))
print(type("texto 2"))
~~~

## Variáveis

Variáveis são espaços alocados na memória para guardar dados. Python é uma linguagem dinâmicamente tipada, o que quer dizer que é possível modificar o tipo e o valor da variável a qualquer momento, e não há necessidade de impor um tipo, nem se deve fazer isso nessa linguagem. Logo uma variável não está amarrada a um tipo.

~~~python
# utiliza-se o operador "=" para atribuir valores
nome = 'Harry'
nome = 'Rony'
nome = 'Hermione'

print(nome)

altura = 1.85
altura = 2

print(altura)

idade = 25
print(idade)

idade = 'Vinte e cinco'
print(idade)
~~~

---

## Operadores Matemáticos

A precedencia de operadores matemáticos é a mesma da matemática. "/"(divisão) ou "*"(multiplicação) primeiro depois "+"(adição) ou "-"(subtração). Porém é uma boa prática usar parenteses para delimitar as operações tornando a precedência mais explícita.

~~~python
resultado = num1 + num2
print('Adição -> 20 + 10 =', resultado, '\n')  # = 30

resultado = num1 - num2
print('Subtração -> 20 - 10 =', resultado, '\n')  # = 10

resultado = num1 * num2
print('Multilicação -> 20 * 10 =', resultado, '\n')  # = 200

# nao e possivel fazer divisão por 0 (zero)
resultado = num1 / num2
print('Divisão -> 20 / 10 =', resultado, 'ou 2\n')  # = 2

resultado = num1 % num2
print('Resto da divisão -> 20 / 10 = resto = ', resultado, '\n')  # = 0

resultado = num2 ** 2
print('Expoente -> 10 **(elevado a) 2 = (10 ao quadrado) =',
      resultado, '\n')  # = 100
~~~

---

## Operadores Condicionais

Operadores condicionais são utilizados para tomar decisões e faz isso definindo fluxos de execução baseados em condições.

~~~python
# IF -> 'se'
# ELSE -> 'senão'
# ELIF -> ELIF + IF -> 'senão se'

var_verdadeiro = True

# 2 iguais não atribui mas sim compara valores
if var_verdadeiro == True:
    # Notar estrutura de identação (o espaçamento)
    print('var_verdade é verdadeiro!')

'''
Operadores de comparacao

==  | igual
!=  | diferente
<   | menor
>   | maior
<=  | menor ou igual
>=  | maior ou igual

Operadores logicos

and | exclusivo (satisfazer os 2 requisitos)
or  | inclusivo (1 requisito basta)
not | negação (nega o valor. Ex: not True = False)
'''

if 2 > 1:
    print(True)

# Basta aninhar identações para permanescer na estrutura de decisão if
else:
    print(False)

#==========

a = 50
b = 20

if a > b and 'abacaxi' == 'uva':  # troque 'uva' por 'abacaxi'
    print(True)

# O else funciona como um default(padrão) vai cair nele caso não caia nas comparações acima
else:
    print(False)

#==========

# Menu

print('\nMenu:\n"1" = Escreve Python\n"2" = Escreve JavaScript\n"3" = Escreve NodeJS\n')
opcao = input('Escolha uma opção: ')

# Lógica do pograma (como ele funciona)
if opcao == '1':  # Lembrando: O retorno de um input é sempre um STRING!
    print('Go Python!')
elif opcao == '2':
    print('Go JavaScript!')
elif opcao == '3':
    print('Go Node!')
else:
    print('Opção inválida!')

# Poderiam ser varios ifs ao inves do elif, porem o programa verificaria todos os ifs, mesmo que a primeira condicao fosse a correta

#==========

# O uso do not:

verdade = True

# tirar o not para ver o resultado
if not verdade:  # O resultado e False (negação do True)
    print('Entrou no if')
else:
    print('Entrou no else')
~~~

---

## Controladores de Fluxo

~~~python

~~~

---

## Strings

~~~python

~~~

---

## Listas

~~~python

~~~

---

## Estruturas de Laço

~~~python

~~~

---

## Dicionários

~~~python

~~~

---

## Tuplas

~~~python

~~~

---

## Sets ou Conjuntos

~~~python

~~~

---

## Importação e Uso de Bibliotecas

~~~python

~~~

---

## Funções

~~~python

~~~

---

## Argumentos para CLI

~~~python

~~~

---

## Trabalhando com Arquivos

~~~python

~~~

---

## Tratamento de erros

~~~python

~~~

---

## Requisições HTTP

~~~python

~~~

---

## Manipulação de JSON

~~~python

~~~

---
