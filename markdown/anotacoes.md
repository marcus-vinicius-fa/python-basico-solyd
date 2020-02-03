[home](../README.md) < resumo

# Python

>O básico da linguagem e algumas coisas mais...

<br/>

*Uso no Windows

## Sumário

- Ferramentas e produtividade

    - [Instalação Python](##instalação-python)
    - [Cmder](##cmder)
    - [VSCode](##vscode)
    - [Fira Code](##fira-code)
    - [Lint ](##lint)
    - [Cmd básico](##cmd-básico)
    - [Bash básico](##bash-básico)

- Python
    - [Olá Mundo](##olá-mundo)
    - [Entrada e Saída](##entrada-e-saída)
    - [Variáveis](##variáveis)
    - [Operadores Matemáticos](##operadores-matemáticos)
    - [Operadores Condicionais](##operadores-condicionais)
    - [Controladores de Fluxo](##controladores-de-fluxo)
    - [Strings](##strings)
    - [Listas](##listas)
    - [Estruturas de Laço](##estruturas-de-laço)
    - [Dicionários](##dicionários)
    - [Tuplas](##tuplas)
    - [Sets ou Conjuntos](##sets-ou-conjuntos)
    - [Importação e Uso de Bibliotecas](##importação-e-uso-de-bibliotecas)
    - [Funções](##funções)
    - [Argumentos para CLI](##argumentos-para-cli)
    - [Trabalhando com Arquivos](##trabalhando-com-arquivos)
    - [Tratamento de erros](##tratamento-de-erros)
    - [Requisições HTTP](##requisições-http)
    - [Manipulação de JSON](##manipulação-de-json)

---

## Instalação Python

Para instalar o Python a melhor maneira é fazendo uso do gerenciador de pacotes [Chocolatey](https://chocolatey.org/), é quase um _apt-get_ em sistemas unix baseados no Ubuntu. Tenho um repositório com pacotes que são importantes para mim como usuário comum e também desenvolvedor. Caso queira conhecer está [aqui](https://github.com/marcus-vinicius-fa/meu-chocolatey). Neste repositório eu também ensino como instalar o Chocolatey além de falar sobre alguns comandos (os mais utilizados).

Com o Chocolatey instalado, abra um prompt(cmd)/powershel (linha de comando windows) como adiministrador e digite o seguinte comando, pressionando enter em seguida.

~~~powershell
# instalando o python na versao mais recente
choco install -y python
~~~

Aguarde o processo de download e instalação e ao finalizar verifique a instalação com o comando.

~~~powershell
# verificando a versao
python --version
~~~

E ai, deu certo?

---

## Cmder

O [Cmder](https://cmder.net/) é basicamente um emulador de console para Windows, isso quer dizer ele funciona de forma igual ao **cmd**, porém possui recursos a mais que ajudam na produtividade no ambiente Windows. Ele consegue capturar e traduzir muitos comandos Unix o que facilita e poupa bastate trabalho além de ajudar você a se familiarizar com o **bash** dos sistemas desse tipo. Possui integração com o Git oferecendo marcalçao de cores e informações a respeito dos seus repositorios.

### Instalação

Vamos instala-lo a partir do gerenciador Chocolatey também

~~~powershell
# instalando o cmder na versao mais recente
choco install -y cmder
~~~

Após a instalação use o atalho **"tecla win + q"** e digite: **"cmder"**. Clique com o botão direito no programa e selecione a opção: **"Fixar na barra de tarefas"**. E pronto, você já têm uma linha de comando nova e melhorada. Mexa no tamanho da fonte caso esteja pequena demais e mude para iniciar por padrão com o cmd caso esteja abrindo com o powershell, essas configuração você encontra clicando no ícone presente no canto direito inferior e depois em **"Settings"**.

---

## VSCode

O [Visual Studio Code](https://code.visualstudio.com/) é um editor código criado pela Microsoft. Ele é muito versátil por ser orientado a "plugins". Nele você encontra extensões para muitas linguagens entre outras de ferramenas para tornar a codificação mais fácil e o seu código melhor. Eu tenho utilizado o VSCode já a bastante tempo e ele tem sido um grande companheiro. Você pode utilizá-lo para trabalhar com Python, nada de reenventar a roda e de programação em bloco de notas, isso definitivamente não vai fazer de você um programador melhor. Existem ferramentas criadas com muito esforço para auxiliar novos programdores e você deve abraçar isso com gratidão e não se aventurar em busca de construir tudo do zero, com o minimo ou zero de ajuda.

### Instalação

Podemos instalar o VSCode da mesma forma que os programas anteriores, com o Chocolatey.

~~~powershell
# instalando o vscode na versao mais recente
choco install -y vscode
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

### Iniciando com Python

Para começar a trabalhar Python no VSCode siga os passos a seguir

1. Com o Cmder/cmd/powershell do aberto navegue até o diretório onde deseja guardar os seus códigos.

~~~powershell
# cd + "diretorio\" entra no diretorio
# cd .. volta um diretorio
cd "nome-do-diretorio\"
~~~

*Use a tecla **"tab"** para autocompletar.



---

## Fira Code

O [Fira Code](https://github.com/tonsky/FiraCode) nada mais é do que uma fonte especial para programadores. Ela dispõe de ligações de caracteres para formar os símbolos que utilizamos no dia-a-dia da programação. Por exemplo `>=`, `<=`, `==` e `!=`.

Vamos instala-la também com o Chocolatey

~~~powershell
# instalando a fonte fira code na versao mais recente
choco install -y firacode
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

## Lint


---

## Cmd básico


---

## Bash básico

- [pwd](http://guialinux.uniriotec.br/pwd/):

- [cd](http://guialinux.uniriotec.br/cd/):

- which:

- [touch](http://guialinux.uniriotec.br/touch/):

- [mkdir](http://guialinux.uniriotec.br/mkdir/):

- nano:

- [rm](http://guialinux.uniriotec.br/rm/):

- [cp](http://guialinux.uniriotec.br/cp/):

- [mv](http://guialinux.uniriotec.br/mv/):

- exit:

---

## Olá Mundo


---

## Entrada e Saída


---

## Variáveis


---

## Operadores Matemáticos


---

## Operadores Condicionais


---

## Controladores de Fluxo


---

## Strings


---

## Listas


---

## Estruturas de Laço


---

## Dicionários


---

## Tuplas


---

## Sets ou Conjuntos


---

## Importação e Uso de Bibliotecas


---

## Funções


---

## Argumentos para CLI


---

## Trabalhando com Arquivos


---

## Tratamento de erros


---

## Requisições HTTP


---

## Manipulação de JSON


---
