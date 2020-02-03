[home](../README.md) | [resumo](./resumo.md)

# Ferramentas e Produtividade

>Configurando um ambiente mais agradável no Windows

## Sumário

1. [Instalação Python](##instalação-python)
1. [Cmder](##cmder)
1. [VSCode](##vscode)
1. [Fira Code](##fira-code)
1. [Lint ](##lint) _(em construção)_
1. [Cmd básico](##cmd-básico)
1. [Bash básico](##bash-básico)

## Instalação Python

Para instalar o Python a melhor maneira é fazendo uso do gerenciador de pacotes [Chocolatey](https://chocolatey.org/), é quase um _apt-get_ em sistemas unix baseados no Ubuntu. Tenho um repositório com pacotes que são importantes para mim como usuário comum e também desenvolvedor, caso queira conhecer está [aqui](https://github.com/marcus-vinicius-fa/meu-chocolatey). Neste repositório eu também ensino como instalar o Chocolatey além de falar sobre alguns comandos (os mais utilizados).

Com o Chocolatey instalado, abra um prompt(cmd)/powershel (linha de comando windows) como adiministrador e digite o seguinte comando, pressionando _enter_ em seguida.

~~~powershell
# instalando o python na versao mais recente
> choco install -y python
~~~

Aguarde o processo de download e instalação e ao finalizar verifique a instalação com o comando.

~~~powershell
# verificando a instalacao
> python --version
~~~

E ai, deu certo?

---

## Cmder

O [Cmder](https://cmder.net/) é basicamente um emulador de console para Windows, isso quer dizer ele funciona de forma igual ao **cmd**, porém possui recursos a mais que ajudam na produtividade no ambiente Windows. Ele consegue capturar e traduzir muitos comandos Unix o que facilita e poupa bastate trabalho além de ajudar você a se familiarizar com o **bash** dos sistemas desse tipo. Possui integração com o Git oferecendo marcalçao de cores e informações a respeito dos seus repositorios.

### Instalação

Vamos instala-lo a partir do gerenciador Chocolatey também

~~~powershell
# instalando o cmder na versao mais recente
> choco install -y cmder
~~~

Após a instalação use o atalho **"tecla win + q"** e digite: **"cmder"**. Clique com o botão direito no programa e selecione a opção: **"Fixar na barra de tarefas"**. E pronto, você já têm uma linha de comando nova e melhorada. Mexa no tamanho da fonte caso esteja pequena demais e mude para iniciar por padrão com o cmd caso esteja abrindo com o powershell, essas configuração você encontra clicando no ícone presente no canto direito inferior e depois em **"Settings"**.

---

## VSCode

O [Visual Studio Code](https://code.visualstudio.com/) é um editor código criado pela Microsoft. Ele é muito versátil por ser orientado a "plugins". Nele você encontra extensões para muitas linguagens entre outras de ferramenas para tornar a codificação mais fácil e o seu código melhor. Eu tenho utilizado o VSCode já a bastante tempo e ele tem sido um grande companheiro. Você pode utilizá-lo para trabalhar com Python, nada de reenventar a roda e de programação em bloco de notas, isso definitivamente não vai fazer de você um programador melhor. Existem ferramentas criadas com muito esforço para auxiliar novos programdores e você deve abraçar isso com gratidão e não se aventurar em busca de construir tudo do zero, com o minimo ou zero de ajuda.

### Instalação

Podemos instalar o VSCode da mesma forma que os programas anteriores, com o Chocolatey.

~~~powershell
# instalando o vscode na versao mais recente
> choco install -y vscode
~~~

### Conhecendo o Editor

#### Configurações

As configurações do vscode ficam em um arquivo chamado de **settings.json**, ou seja ele obedece a estrura de arquivos **.json**. Para abrir esse arquivo pressione as teclas de atalho **"ctrl + shift + p"** e digite: **"settings.json"**.

_Outra maneira de chegar as configuraçõs do editor..._

Clique no ícone de engrenagem no canto inferior esquerdo e selecione **"Configurações"**. Agora basta pesquisar o que se quer utilizando palavras chaves ou abrindo a estrutura de níveis no lado esquerdo.

#### Barra de atividades

- **Explorador:** Aqui você encontrará as suas pastas ou seus arquivos ou seu workspace-vscode.

- **Pesquisar:** Aqui você poderá fazer pesquisas inteligentes por arquivos e pastas.

- **Controle de código fonte:** Você utiliza o Git ou outra ferramenta para versionamento de código, aqui você poderá verificar como está o seu versionamento.

- **Depuração:** Essa aba serve para fazer a verificação do seu código com a ajuda da ferramenta de depurar.

- **Extensões:** Aqui você encontras as suas extensões.

#### Alguns atalhos

- **"Ctrl + k + s" :** Mostra todos os atalhos.

- **"Ctrl + shift + p":** Digite alguma ação para realizar com o editor ou alguma extensão.

- **"Ctrl + p":** Pesquise arquivos utilizando comandos inteligentes.

- **"Ctrl + ' ":** Abre um novo terminal integrado ao vscode. Para abrir em uma pasta no explorador clique com o o botão direto na pasta e selecione **"Abrir no Terminal"**.

- **"Ctrl + shift + k":** Deleta a linha corrente em um arquivo.

- **"alt + setas up/down":** Move a linha corrente para cima e para baixo.

- **"alt + shift + seta para baixo":** Duplica linha corrente.

- **"Ctrl + d":** Marca palavras semelhantas a que está marcada pelo cursor, ou onde ele está parado. Para ir marcando basta continuar clicando no atalho.

- **"Ctrl + alt + setas up/down":** Marca linhas juntas para escrever ou deletar. Pressione **esc** para sair da seleção.

- **"alt + mouse clique esquerdo":** Marca linhas separadas para escrever ou deletar. Pressione **esc** para sair da seleção.

- **"Ctrl + shift + O":** Para procurar elementos em um arquivo.

- **"Ctrl + ; ":** Comenta um linha inteira

### Extensões

#### Para trabalhar com Python

- Python
- Magic Python
- Python Extended

*Podem ser instaladas juntas, funcionam bem assim.

#### Melhor interação

- **Portuguese (Brazil):** Modifica o idioma do editor.

- **Dracula Oficial:** Um tema dark para o seu editor não cansar a sua vista.

- **Material Icon Theme:** Um tema de icones para deixar suas pastas e arquivos mais compreensíveis e belos.

- **TodoTree:** Comente o que é que precisa resolver e encontre mais facilmente.

Cole essa estrutura no seu arquivo **settings.js**

~~~js
{
    "todo-tree.highlights.enabled": true,
    "todo-tree.highlights.defaultHighlight": {
        "foreground": "green",
        "type": "tag"
    },
    "todo-tree.highlights.customHighlight": {
        "TODO": {
        "icon": "pin",
        "foreground": "green"
        },
        "FIXME": {
        "icon": "alert",
        "foreground": "yellow"
        },
        "BUG": {
        "icon": "bug",
        "foreground": "red"
        }
    },
}
~~~

Agora use o comando **"Ctrl + ; "** dentro de um arquivo para comentar uma linha inteira vazia e escreva dentro do comentário uma das três linhas abaixo (teste uma de cada vez)

~~~powershell
# para marcar tarefas
# TODO: texto...

# para marcar urgencia para conserto
# FIXME: texto...

# para marcar um bug
# BUG: texto...
~~~

Na barra de ativiade clique no novo ícone do TodoTree para ver todos os arquivos marcados, assim você não se perde mais.

- **Bracket Pair Colorizer 2:** Extensão para colorir essas "( { [ ] } )" estruturas em níveis ajuda muito a visualizar o seu código.

- **Editor Config:** Essa extensão serve para padronizar o seu código caso esteja codificando em equipe ou caso utilize dualboot na sua máquina.

Para Python creio que essa seja a melhor configuração no arquivo **.editorconfig** criado na pasta raiz dos seus arquivos **.py**

~~~js
root = true

[*]
indent_style = space
indent_size = 4
charset = utf-8
end_of_line = lf
trim_trailing_whitespace = true
insert_final_newline = true
~~~

Este arquivo é muito simples e para entender melhor o que significa cada linha de configuração veja no [site oficial do projeto](https://editorconfig.org/#overview).

---

## Fira Code

O [Fira Code](https://github.com/tonsky/FiraCode) nada mais é do que uma fonte especial para programadores. Ela dispõe de ligações de caracteres para formar os símbolos que utilizamos no dia-a-dia da programação. Por exemplo `>=`, `<=`, `==` e `!=`.

Vamos instala-la também com o Chocolatey

~~~powershell
# instalando a fonte fira code na versao mais recente
> choco install -y firacode
~~~

Instalação concluída vamos dizer para o VSCode que queremos fazer uso dessa fonte e que desejamos habilitar a ligação de caracteres a partir de agora. Com o VSCode aberto pressione as teclas de atalho **"ctrl + shift + p"** e digite: **"settings.json"**, copie as linhas abaixo, dentro dos colchetes, para o seu arquivo **settings.json**.

~~~powershell
# arquivo em formato json, com as configuracoes do editor
{
    "editor.fontFamily": "Fira Code",
    "editor.fontLigatures": true,
}
~~~

_Outra maneira..._

Clique no ícone de engrenagem no canto inferior esquerdo e selecione **"Configurações"**. Clique em **"Editor de texto"** > **"Fonte"**. Em **"Font Family"**, apague o conteúdo e preencha com: **"Fira Code"**, sem aspas. Marque a opção para ativar as ligações de caracteres chamadas de **"Font Ligatures"**. E pronto, agora você têm mais clareza na leitura dos códigos.

---

<!-- ## Lint

TODO: fazer essa parte

Lint é um programa que checa o código a procura de erros de sintaxe ou de estilo.

Para "Lintar" o código Python você pode fazer uso da ferramenta [pylint](https://www.pylint.org/) e

~~~js
{
    "python.pythonPath":"C:\\Python38\\python",
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    // "python.linting.pep8Enable": true,
    "python.formatting.provider": "autopep8",
    "[python]": {
        "editor.tabSize": 4,
        "editor.detectIndentation": true,
        "editor.formatOnSave" : true,
        "editor.formatOnPaste": true,
    }
}
~~~ -->

## Cmd básico

Com o uso do [Cmder](##cmder) acho mais interessante aprender os comandos unix. Abaixo seguem alguns comandos principais do windows para usos mais básicos.

[dir](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#DIR): lista arquivos e pastas

**cd**: entra em uma pasta

[md](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#MKDIR): cria uma pasta

[copy](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#COPY): copia uma arquivo ou pasta

[move](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#MOVE): move um arquivo ou pasta

[deltree](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#DELTREE): deleta pasta e subpastas

**del**: deleta um arquivo

[ren](https://pt.wikibooks.org/wiki/MS-DOS/Lista_de_comandos#RENAME): renomeia arquivos

---

## Bash básico

*Esses comandos são interpretados pelo [Cmder](##cmder).

A sintaxe dos comandos geralmente é essa:

**comando [parametro]... []...**

Digite um dos comandos abaixo seguido de **--help** (um parâmetro) para descobrir as possibilidades do comando inserido.

<br/>

**[PWD](http://guialinux.uniriotec.br/pwd/)**: Comando para saber qual é o diretório corrente/atual.

~~~bash
$ pwd

> C:/Users/usuario
~~~

**[CD](http://guialinux.uniriotec.br/cd/)**: Comando para entrar e sair de diretórios.

~~~bash
# entra no diretorio
$ cd "nome-do-diretorio/"

# volta um diretoria na cadeia
$ cd ..

# volta dois diretorios na cadeia
$ cd ../..
~~~

**WHICH**: Comando para verificar o local de instalação de um binário (executável de um programa).

~~~bash
# onde o python esta instalado
$ which python

> /C:/Python38/python
~~~

**[TOUCH](http://guialinux.uniriotec.br/touch/)**: Comando para criar um novo arquivo vazio.

~~~bash
# cria um arquivo chamado teste com a extensao .txt
$ touch "teste.txt"

# use o "ls" para verificar a criacao do arquivo
~~~

**[LS](http://guialinux.uniriotec.br/ls/)**: Comando para listar os arquivos de um diretório.

~~~bash
# listar arquivos
$ ls

# listar todos os arquivos inclusive os ocultos
$ ls -a
~~~

**[MKDIR](http://guialinux.uniriotec.br/mkdir/)**: Comando para criar pastas/diretorios.

~~~bash
# cria um diretorio chamado nome-da-pasta
$ mkdir "nome-do-diretorio"

# verifique o novo diretorio com o comando "ls"
~~~

**NANO**: Comando para abrir um editor de texto dentro da linha de comando.

~~~bash
# se o arquivo nao existem ele sera aberto mesmo assim
# caso deseje salva-lo apos a escrita o arquivo sera criado
$ nano "nome-do-arquivo.txt"
~~~

**[RM](http://guialinux.uniriotec.br/rm/)**: Comando para remover um arquivo ou diretorio (caso precedido de parametro)

~~~bash
# exclui o arquivo
$ rm nome-do-arquivo.txt

# -r para remover de forma recursiva
# -f para forcar a remorcao
# deleta o diretorio e subdiretorios
$ rm -rf "nome-do-diretorio/"
~~~

**[CP](http://guialinux.uniriotec.br/cp/)**: Comando para copiar arquivos ou diretórios.

~~~bash
# copia arquivo para a pasta
cp "arquivo.txt" "/nome-do-dir/nome-do-dir"
~~~

**[MV](http://guialinux.uniriotec.br/mv/)**: Comando para mover ou renomear arquivos ou diretórios.

~~~bash
# move arquivo para a pasta
mv arquivo.txt "/nome-do-dir/nome-do-dir"

# renomeia arquivo
mv "arquivo.txt" "novo-arquivo.txt"
~~~

**"Ctrl + c**": Comando para cancelar uma ação corrente.

**"Ctrl + l"**: "Sobe" a linha de comando.

**CLEAR**: Limpa a linha de comando.

~~~bash
$ clear
~~~

**RESET**: Reinicia a linha de comando.

~~~bash
$ reset
~~~

**EXIT**: Comando para sair da linha de comando.

~~~bash
$ exit
~~~
