# python

#Etapa 1 Aula 3

Apresentar prática da semana anterior.
Para as linguagens foco, pesquisar sintaxe e semântica.
Palavras reservadas,Literais,Operadores, etc.

A sintaxe da linguagem de programação Python é o conjunto de regras que definem como um programa em Python será escrito e interpretado (tanto pelo sistema de tempo de execução como pelo ser humano). Python foi concebido para ser uma linguagem altamente legível.Ela possui um layout visual relativamente organizado e usa palavras em Inglês com freqüência, quando outras linguagens usam pontuação. 
Python objetiva a simplicidade e generalidade na concepção da sua sintaxe, encapsulados no mantra "Deve haver um - e preferencialmente só um - modo óbvio de fazer isso", do "The Zen of Python".Observe que este mantra é deliberadamente oposto ao mantra do Perl de "há mais de uma maneira de fazê-lo". 

O Python tem as seguintes palavras-chave ou palavras reservadas; eles não podem ser usados como identificadores.

    and
    as
    assert
    break
    class
    continue
    def
    del
    elif
    else
    except
    exec[note 1]
    False[note 2]
    finally
    for
    from
    global
    if
    import
    in
    is
    lambda
    None
    nonlocal[note 2]
    not
    or
    pass
    print[note 1]
    raise
    return
    True[note 2]
    try
    while
    with
    yield

No Python 3.5 ela vem com as seguintes palavras adicionais: async and await.

Literais Numéricos

Literais Numéricos são imutáveis ​​(imutáveis). 
Os literais numéricos podem pertencer a 3 tipos numéricos diferentes: Integer, Float e Complex.

Exemplos:

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

O que são operadores em python?
Operadores são símbolos especiais em Python que executam cálculos aritméticos ou lógicos. O valor em que o operador opera é chamado de operando.

Por exemplo:

>>> 2+3
5
Aqui +está o operador que realiza a adição. 2e 3são os operandos e 5é a saída da operação.

Operadores aritméticos
Operadores aritméticos são usados ​​para executar operações matemáticas como adição, subtração, multiplicação etc.

Operadores aritméticos em Python
Operador	Significado	Exemplo
+	Adicione dois operandos ou unário mais	x + y 
+2
-	Subtrair operando à direita da esquerda ou unário menos	x - y 
-2
*	Multiplique dois operandos	x * y
/	Divide o operando esquerdo pelo direito (sempre resulta em float)	x / y
%	Módulo - restante da divisão do operando esquerdo pela direita	x% y (restante de x / y)
//	Divisão de piso - divisão que resulta em número inteiro ajustado à esquerda na linha numérica	x // y
**	Expoente - operando esquerdo elevado ao poder do direito	x ** y (x para o poder y)

Quando você executa o programa, a saída será:

Exemplo:

x = 15
y = 4

x + y = 19
x - y = 11
x * y = 60
x / y = 3,75
x // y = 3
x ** y = 50625

#Etapa 2 - Aula 4

Prática:

Listar principais versões  do Python:

Versão 2.x e 3.x.

Use Python 2 somente quando estiver trabalhando com um software que ainda não foi migrado para Python 3 ou caso precise manter algum sistema legado.

Python 2 foi o padrão da linguagem por muito tempo.
Python 2 receberá atualizações de segurança até 2020 quando seu suporte será descontinuado.
Python 3 está constantemente evoluindo e recebendo novas funcionalidades, que não estarão presentes na versão anterior.
Python 3 introduziu algumas mudanças que quebraram a compatibilidade com a versão anterior o que criou a nessecidade de se manter duas versões da linguagem.


Para cada versão, listar conjunto de ferramentas de desenvolvimento.
Ferramentas de Desenvolvimento

Veja aqui uma listagem de ferramentas para te auxiliar no desenvolvimento python:

Editores de texto

Atom
Atom é open source e feito pelo Github e com suporte para várias linguagens, dentre elas o Python. É integrado ao Git e Github, sendo possível mexer com o Git e Github através da interface do editor de texto. Ótimo para iniciantes.

Visual Studio Code
O VSCode é open source e free, desenvolvido pela Microsoft. Suporta inúmeras linguagens de programação.

Vim
Tem em todo GNU/Linux e é altamente configurável. Uma forma de transformar o vim em uma IDE Python completa é seguindo o tutorial em vim a ide para programadores python.

Emacs
Um editor (ou um sistema operacional com capacidades de edição?!) poderoso e amplamente extensível em eLisp (um dialeto Lisp). Vencida a curva de aprendizado (considerada difícil por algumas pessoas) é possível torná-lo em uma IDE Python poderosíssima. O python-mode.el prove diversas funcionalidades para edição, debug e desenvolvimento de programas em Python e o Ropemacs funcionalidades de refactoring. Mais "Emacs Goodies" na própria Wiki em PythonComEmacs.

SciTE
Excelente editor de texto voltado para programação. Suporta uma grande lista de linguagens, pode rodar e debugar os programas, é fácil de usar e é facilmente configurável. Disponível para Windows e X (ambiente gráfico dos UNIXes).

jext
Muito bom editor! Suporta muitas linguagens e possui plugins para Python (executar, por exemplo).

joe
Editor de texto para dinossauros :-) Utiliza os mesmos comandos do WordStar, SideKick, etc. Disponivel via apt-get e emerge.

sublime
Editor de texto proprietário e pago, porém disponibiliza uma versão beta para uso sem custo. Atualmente na versão 3, a compra de sua licensa permite o uso de ambas as versão existentes.

PS Pad
Grátis (freeware) para Windows. Colore código Python e suporta edição com vários encodings. Tem também utilitários para HTML/XML, tabela ASCII e conversão DOS/UNIX. O Hex view quebra um galho na hora de procurar erros em arquivos com encoding incorreto.

IDEs gratuitas

Idle
A IDLE vem com o Python. É feita com Tkinter e se você se acostumar pode lhe ajudar bastante. É bem simples de ser usada também.
PyCharm community
É desenvolvido pela companhia JetBrains. Esta edição é liberada sob a licença da Apache. É multiplataforma. Essa IDE fornece análise de código, um depurador gráfico, um testador de unidade integrado, integração com sistemas de controle de versão (VCSes), e suporta desenvolvimento de web com Django.

Komodo-Edit
Também desenvolvido pela ActiveState o Komodo-Edit é uma excelente opção de editor, bastante rico em recursos tais como autocomplete, calltips, multi-language file support, syntax coloring, syntax checking, Vi emulation, Emacs key bindings e outros.

NetBeans
Analogamente ao Eclipse, o NetBeans também oferece suporte ao Python através de plugins.

NINJA-IDE
Do acrônimo recursivo: "Ninja-IDE Is Not Just Another IDE", é uma IDE multi-plataforma de desenvolvimento integrado. NINJA-IDE é executado em Linux/X11, Mac OS X e sistemas operacionais de desktop Windows, e permite aos desenvolvedores criarem aplicações para diversas finalidades, utilizando todas as ferramentas e utilitários de NINJA-IDE, tornando a tarefa de escrever software mais fácil e agradável.

SPE
Desenvolvido com wxPython é livre e tem algumas funcionalidades interessantes. Tem wxGlade como plugin para desenho de telas gráficas.

Spyder 2
Spyder (também conhecido como Pydee) é um poderoso ambiente de desenvolvimento interativo para a linguagem Python com edição avançada, testes interativos, recursos de depuração e introspecção

Pida
É um IDE desenvolvido com PyGTK e visa a integração com o Vim. Oferece recursos como project management, source code management, code browser, code refactor, profiler, debugger entre outros.
Eric4

É feito com a biblioteca QT e se integra às ferramentas da QT e com outros softwares como o Bicycle Repair Man (refactoring) e TabNanny (verificação de indentações). O autor dos bindings python para o Qt4, lançou um instalador para Windows que contém as bibliotecas e os programas de desenvolvimento do Qt4, o pyqwt e o Eric4, o que facilita bastante a instalação no Windows.
Boa-Constructor

Essa é a "única" IDE ao estilo RAD do Delphi/VB. Funciona com o wxPython na versão 2.4 e acho que é a mais fácil de ser usada apesar de não promover boas práticas de desenvolvimento como a de separar lógica de negócios de apresentação (telas). As outras IDEs não possuem mecanismos para desenho de telas gráficas mas podem usar ferramentas como Glade e/ou wxGlade.

Eclipse
Diferente de todos os outros. Pesado, grande, monstruoso mas muito poderoso. É feito em Java e é ideal para desenvolvimento Java. Mas existem plugins para se desenvolver em Python com ele (e detalhe: atualmente é um brasileiro quem o mantém) que é o ppydev.

EasyEclipse
EasyEclipse é open source e hospedado pela Sourceforge que fornece muitas distribuições empacotadas do Eclipse pré-configuradas com plug-ins para Python, Ruby, etc.

DrPython
Usa wxPython. Criado para ser utilizado em escolas.

IPython
Um shell com muitos recursos, através das comandos "mágicos". Bastante útil, modo texto apenas. Você pode usá-lo como um shell "acoplado" aos seus programas também.

KDevelop
IDE livre para GNU/Linux e outros *nixes-like.

PythonWin
IDE que acompanha as extensões Win32 para Python (PyWin32). Oferece auto-completion e debugging, e tem recursos extras voltados à programação Windows (coletor de exceções para componentes COM criados, COM browser, geração de arquivos .py com informações sobre objetos COM (static dispatch), etc.).

PythonCard
É uma GUI para construção de aplicações multiplataforma em Windows, Mac OS X e Linux, usando a linguagem de programação Python. O lema de PythonCard é "coisas simples devem ser simples de fazer e coisas complexas devem devem ser possiveis". É a ferramenta para quem deseja desenvolver aplicações gráficas de maneira rápida e fácil, com um mínimo de esforço e codificação; simples mas poderoso. Utiliza a biblioteca wxPython, mas separa a lógica do código da apresentação utilizando um tipo de arquivo de definição de recursos. (RômuloCampelo - 08/04/2005)

PyScripter
Acompanha o conjunto de componentes python para Delphi (embora não requira que o Delphi esteja instalado para funcionar). Suporta debugging, auto-completion, navegação no código entre outros recursos.

PyPE
Não se trata de uma IDE propriamente dita, mas é um editor Python, leve, funcional e rico em recursos interessantes e multiplataforma. Além disso, é desenvolvido utilizando wxPython.

Rodeo
Rodeo é uma IDE leve e intuitiva voltada para análise de dados. Com suporte a Jupyter Notebook, navegador de arquivos, busca de packages e visualização de gráficos, além de suporte a comandos VIM.

IDEs (pagas)

Wing
A empresa wingware recentemente lançou o wingide101 para auxiliar no ensino de Python e é uma versão com menos recursos que as versões professional e personal, mas que tem funcionalidades interessantes, como depurador gráfico, shell interativo. Segue o link: http://wingware.com/wingide-101/index

Komodo
Essa é outra IDE bem poderosa também. Trabalha com outras linguagens além de Python e roda em Linux e Windows. Existe uma licença gratuita que pode ser usada para aprendizado

PyCharm
Possui um conjunto de ferramentas úteis para um desenvolvimento produtivo. Além disso, a IDE fornece capacidades de alta classe para o desenvolvimento Web profissional com framework Django e Flask, Google AppEngine. Possui suporte a diversos sistemas de controle de versão, integração com Github e atraves de plugin, com o Heroku. Possui gerador de Diagramas de Classe e ORM. Suporte para interpretador Python remoto. Criação de gerência de ambientes (virtualenv). Mais informações sobre funcionalidades e desenvolvimento do PyCharm veja http://confluence.jetbrains.net/display/PYH/PyCharm+IDE+and+Python+Plugin+for+IntelliJ+IDEA

Visual Studio 2010+
IDE completa para o mundo .NET que com o IronPython se torna uma excelente IDE.

Refactoring
Bycicle Repair Man
Automatiza algumas operações básicas de refactoring para Python. Tem integração com vários editores, como o PyDev e o Emacs.

Rope
Uma biblioteca de refactoring para Python. Pode ser usada em outras IDEs.
*Boa parte deste conteúdo foi retirado do link (http://wiki.python.org.br/IdesPython)

Identificar diferenças entre as principais versões da linguagem

ponto é que as duas maiores versões major do Python (2 e 3, as únicas em uso) têm diferenças cruciais. O Python 3 não é retrocompatível, e isso acaba trazendo algumas confusões e dúvidas para nós desenvolvedores.

Mas o que essa “retroincompatibilidade” significa? Basicamente, indica que código escrito em Python 2 pode não funcionar rodando no interpretador do Python 3.
O Python 3 foi lançado no final de 2008, pouco mais de 8 anos depois do Python 2, e veio com intenções claras – retificar as falhas de design que a linguagem trazia.

Fonte: http://blog.caelum.com.br/quais-as-diferencas-entre-python-2-e-python-3/


Diferenças mais impactantes
Dito isso, não sei dizer quais são todas essas diferenças, mas dentre as principais segundo a documentação as que considero mais impactantes são as seguintes:
print no 3 é uma função, e não uma instrução:
print 42  # Python 2
print(42) # Python 3
Várias funções built-in e métodos dos principais tipos, que antes retornavam listas, agora retornam iteradores. Isso não é um problema nos usos mais corriqueiros, mas se em algum momento você realmente precisar de uma lista, acostume-se a criar uma explicitamente:
x = list(range(10)) # No Python 2 range já retorna uma lista, você apenas a copia
                    # No Python 3 range retorna um iterador, é preciso criar a lista

for i in range(10): # Igual em ambos (mais eficiente no 3)
Strings no 3 são Unicode por padrão, e sequências de bytes devem estar prefixadas por b:
x = "Olá" # No 2, sem o "import unicode_literals", seria inválido

x = u"Olá" # Como era no 2, NÃO RECOMENDADO usar em códigos novos

y = b"\x80" # Só existe a partir do 3; note que 0x80 não é um caractere ASCII válido
Inteiro dividido por inteiro é inteiro no 2, mas é ponto flutuante no 3:
x = 3/2  # 1.5 no Python 3, 1 no Python 2 sem o "import division"

y = 3//2 # 1 em ambos ("//" é a divisão inteira)

Fonte: https://pt.stackoverflow.com/questions/103322/diferen%C3%A7as-entre-as-vers%C3%B5es-do-python - -

#Etapa 3 - Aula 5 08/03/2019 PRÁTICA PRIMITIVO e PRIMITIVO COMPOSTO PYTHON

Resumo:

Tipos primitivos: são aqueles já embutidos no núcleo da linguagem
Simples: números (int, long, float, complex) e cadeias de caracteres (strings)
Compostos: listas, dicionários, tuplas e conjuntos(sets)

FONTE: https://www.dcc.ufrj.br/~fabiom/mab225/02tipos.pdf

TIPOS

O tipo é uma forma de classificar as informação. As linguagens de programação normalmente trazem implementado o que é chamado de tipos primitivos, isto é, o tipo de dado mais genérico possível.

Toda informação que manipularemos será, por definição, de um tipo.

Na informática tudo é manipulado como sendo bits. Quando manipulamos letras estamos trabalhando também com bits, porém, numa camada acima. Então, vamos definir agora, que num primeiro momento, toda informação é de fato um caractere, seja ele uma letra, um número, um simbolo ou então, um caractere especial.

Assim, definimos num primeiro momento que tudo são caracteres.
String

Na programação String representa um conjunto de caracteres disposto numa determinada ordem. A partir de agora, todas as vezes em que falarmos o termo String, estaremos nos referindo a um conjunto de caracteres.
Inteiro

Um segundo tipo de informação são os dados compostos por caracteres numéricos (algarismo). Os números são divididos em 2 partes:

        inteiros - chamados de integer ou int
        ponto flutuante - chamado de float ou double

Exemplos de informação

A título de exemplo, vamos citar alguns tipos de informação e em seguida, vamos definir o tipo que precisaríamos utilizar para armazenar um valor correspondente a informação.

        Nome - dado tipo String
        Idade - dado tipo Integer
        Conta bancária - dado composto por números, pontos e traços

As informações são classificadas devido ao fato de seguirem regras e estruturas iguais. Ou seja, um número de telefone possui uma regra para todo o território nacional, logo, é possível classificar esse tipo de dado, até porque, há uma regra que o define.
	

Atualmente, os números de telefones no estado de São Paulo contém 9 digitos, enquanto os demais estados e capitais utilizam somente 8 digitos. Essa é uma situação que já ocorreu há anos e voltou a acontecer. Por isso, devemos estar certos de que irá acontecer novamente no futuro. Assim, é prudente que nossos softwares sejam capazes de lidar com essa variação, seja para o momento atual, seja para estarem preparados para futuras modificações.

Um outros exemplo que possibilita a classificação é o número das contas bancárias que, geralmente, é composto por números e um digito verificador. O nome das pessoas, normalmente, é constituído somente por letras. A idade das pessoas é representado por números inteiros. Datas são a junção de números com alguns caracteres especiais e assim por diante.
	

Digito verificar é aquele número contido no final, geralmente após um traço ou então, após um ponto. A função deste digito é proporcionar um meio para chegar se os digitos anteriores estão corretos, até porque, o digito verificador é obtido através de uma fórmula matemática que utiliza todos os números e no final, gera um digito de confirmação. Por exemplo, o CPF é composto de 9 digitos, mais 2 digitos verificador, por exemplo: ``CPF: 123.456.789-09``.

A última parte do CPF acima, no caso, o número 09 é o digito verificador e o mesmo foi obtido através de uma fórmula que utilizou todos os 9 digitos e resultou no digito verificador 09. Exemplos de informações que possuem digito verificador são: o número da conta corrente de alguns bancos, o CPF dentre outras informações.

Os tipos de dados são uma forma de classificação que facilita o processamento e a manipulação das informações.
TIPOS PRIMITIVOS

Tipo Primitivo são os tipos de dados mais simples, isto é, a informação em sua forma mais primitiva. Bons exemplos de valores primitivos são os caractere, os número, o valor True e o False e etc. A documentação do Python não trata os tipos de dados elementares (primitivos) com a nomenclatura normalmente encontrada na documentação da maioria das linguagens: Tipo Primitivo. Na documentação oficial, os tipos primitivos são chamados de tipos built-ins ou então, tipos construídos. Essa nomenclatura é utilizada para indicar que estamos utilizando informações que foram definidas, por padrão, através de classes dentro da Máquina Virtual do Python.

Nesse momento, chamaremos de Tipos Primitivos as informações em sua forma mais simples, porém, é importante saber que para o Python, não há tipo primitivos, mas sim, estruturas de dados que estão definidas, na maior parte das vezes, dentro da própria Máquina Virtual do Python.

É normal que as linguagens de programação tenham um conjunto de tipos chamados de: tipos primitivos. Devemos pensar nessa classificação como sendo os tipos primários de informações, como por exemplo, o tipo numérico. Como sabemos, todo número é constituído por algarismos. Dessa forma, o tipo numérico pode ser qualquer valor que seja composto por 1 ou mais caracteres numéricos.

Dessa forma, isto é, tendo a certeza de que uma variável declarada como sendo do tipo numérico inteiro sempre terá um valor numérico válido, somos capazes de desenvolver funções especificas que manipulam esse tipo de dado de maneira muito mais eficiente e sem a necessidade de verificação se o tipo da informação contida em determinada variável é válido.

Da mesma forma, temos o tipo de dado que representa conjuntos de caracteres, que na programação, é comumente chamado de String e o Python o chama de str. As String são capazes de armazenar conjuntos de caracteres que estão dispostos numa determinada ordem. Todas as vezes que estivermos manipulando dados que contenha caracteres - o tipo mais primitivo, isto é, a maneira mais abstrata para representarmos caracteres - estaremos utilizando uma variável definida como sendo do tipo str.

O fato de o Python não trabalhar com tipo primitivos diretamente, deve-se ao fato de que em Python, tudo são objetos. Dessa forma, o que chamaríamos de primitivo é, em Python, representado como uma e toda informação será, um objeto propriamente dito. A seguir, temos a lista dos principais tipos built-ins da linguagem Python:

        int - para números inteiros
        str - para conjunto de caracteres
        bool - armazena True ou False
        list - para agrupar um conjunto de elementos
        tupla - semelhante ao tipo list, porém, imutável
        dic - para agrupar elementos que serão recuperados por uma chave

O Python fornece um conjunto de tipos básicos bastante amplo e que normalmente, atendem a maioria das necessidades. Cada tipo citado, possui um conjunto de funções e métodos que permitem manipularmos as informações, contidas na variável, de maneira bastante eficiente.

Sempre que formos criar um novo tipo de dados, acabaremos utilizando os tipos básicos da linguagem, como por exemplo, o tipo `int`, ou então, o tipo `str` e assim por diante.
DIFERENÇA ENTRE TIPO E VALOR

O valor é qualquer informação, seja um número, texto, música, vídeo e etc. O tipo por sua vez, é a estrutura da informação e a forma de classificarmos os dados.

Todo valor numérico deve ser capaz de ser somado a outro valor, ou então, subtraido. Da mesma forma que todo texto, deve ser capaz de ser concatenado a outro, isto é, ser juntado a outro conjunto de caracteres.

O tipo da informação deve ser pensado como uma forma de classificarmos as diferentes informações e assim, termos a disposição um conjunto de funções para tratarmos e modificarmos os valores.

É importante saber que somos capazes de criar novos tipos de dados a qualquer momento, e a programação orientada a objetos é, em sua definição mais primitiva, uma maneira de criarmos novos tipos abstratos e definirmos, na estrutura da classe, funções, métodos, verificações que busquem tratar valores que tenham uma mesma estrutura.
CONVERSÃO DE DADOS OU COERÇÃO DE TIPOS

Se as informações possuem tipos, logo, temos de ser capazes em converter um tipo de informação num outro tipo de dado. Essa ação de conversão é comumente chamada de Coerção de Tipos.

Linguagem tipada é aquela que permite a classificação das informações pelo uso de tipos de dados, por exemplo, o Python trata um conjunto de caracteres como sendo do tipo String, logo, o Python é uma linguagem tipada, no caso, uma linguagem dinamicamente tipada.

Se existem diferentes tipos de informação, temos de ser capazes de converter, por exemplo, um número para o tipo texto. Ou seja, a conversão de valores é essencial para que possamos trabalhar com informações tipadas, até porque, há diversas situações onde desejaremos manipular um número como sendo um texto.

Essa conversão é comumente chamada de Conversão de Dados ou então, Coerção de Tipos. É importante observar, que uma informação do tipo texto, pode ser constituida de letras e números, ou seja, o grupo de caracteres alfanuméricos. Então, um número pode ser representado como um texto, mas o contrário, nem sempre será possível.

Pra convertermos, por exemplo, um texto para o tipo numérico, devemos especificar o tipo a ser convertido e passarmos o valor através de parêntesis, como podemos ver a seguir:

tipo_a_ser_convertido( informação )

A seguir, declararemos uma variável de nome texto e atribuimos um valor numérico a mesma. Em seguida, declaramos outra variável, de nome num e atribuimos a esta o resultado da Coerção de Tipos. Isto é, dissemos que o valor da variável texto deve ser convertido num tipo numérico num = int(texto).

#coding: utf-8

texto = "10"
num = int(texto)

print( texto + str(10) )#o sinal de + concatena duas informações
print( num + 10 )#o sinal de + soma dois números

>>> 1010
>>> 20

No exemplo acima, podemos observar que a utilização do operador + funciona de maneira diferente conforme o tipo de dado que esteja sendo utilizado. Quando o sinal de adição estiver entre dois valores numéricos, estes serão somados. Quando o sinal adição estiver entre dois valores do tipo String, estes serão concatenados (juntados) e quando o sinal de adição estiver entre um valor do tipo numérico e do tipo String, uma exceção será levantada dizendo que não é possível utilizar o operador de adição entre tipos distintos.

Por fim, temos 4 tipos para classificação para os tipos de informações.

        Tipos simples - constituidos por simples blocos, como int() e float()
        Tipos de contêiner - objetos capazes de conter outros objetos
        Tipos de código - objetos encapsuladores de elementos dos nosso programas
        Tipos internos - tipos que serão utilizados durante a execução do nosso programa

Fonte: http://excript.com/python/tipos-de-dados-python.html
Fonte2: https://e17aeternus.wordpress.com/2015/07/26/listas-tuplas-set-e-dicionarios/

#Etapa 3 - Aula 5 - Prática conversão de composto e primitivo

Código shared de exemplo de conversão int para float: https://onlinegdb.com/HkNm8ugDV

Fonte para demais conversões: https://www.geeksforgeeks.org/type-conversion-python/

#Etapa 3 - Aula 5 - Prática coleções e Arrays

Código shared de exemplo de fila e tupla: https://onlinegdb.com/S17h2_gDV

#Etapa 3 - Aula 5 - Prática fluxo de controle

Código shared de exemplo de fluxo de controle: https://onlinegdb.com/rywweI-vV

#Etapa 3 - Aula 5 - Prática input output

Código shared de exemplo de input e output https://onlinegdb.com/HkFQktxvV

Fonte: https://cadernoscicomp.com.br/tutorial/introducao-a-programacao-em-python-3/funcoes-print-input-e-o-metodo-format/

#Etapa 4 - Aula 6 - Prática imprimindo os resultados do fatorial

Fonte: shared de função fatorial https://onlinegdb.com/Hy-_roKPN

#Etapa 4 - Aula 6 - Para a prática anterior, refaça utilizando funções anônimas.

Link: https://onlinegdb.com/BkRWV2Kw

#Etapa 4 - Aula 6 - Exercício hanoi.

Link: https://onlinegdb.com/HkoiH2YPN

#Etapa 4 - Aula 6 - Prática de Tipo Abstrato de Dados

Link: https://onlinegdb.com/H1WrrnFD4

#Etapa 4 - Aula 6 - Error Handling

Link pesquisa: https://code.tutsplus.com/pt/tutorials/error-handling-logging-in-python--cms-27932
Link código: https://onlinegdb.com/Bytgs2FwE

#Etapa 5 - Aula 7 - Gerenciamento de memória

Python (assim como C#, Java, Perl, Ruby e Lua) utiliza garbage collection ao invés de gerenciamento de memória manual. O gerenciador de memória procura periodicamente por qualquer objeto que não está mais sendo referenciados pelo programa.

O Python utiliza um heap privado contendo todos os objetos e estruturas de dados. Ele utiliza aspectos variados de gerenciamento de armazenamento dinâmico, como: compartilhamento, segmentação, pré-alocação ou caching.

O programador não possui acesso a este heap privado, ele é gerenciado pelo interpretador. A alocação do objetos no heap é feita sob demanda pelo gerenciador de memória do Python, a API core dá acesso a algumas ferramentas para o programador. Informações mais detalhadas podem ser encontradas na documentação do Python.

#Vantagens e Desvantagens

A grande e principal vantagem do gerenciamento de memória do Python é o seu Garbage Collector, que é um mecanismo responsável pela desalocação da memória uma vez que ela não é mais utilizada. Seu funcionamento ocorre através de contadores, que possuem a informação de quantas vezes um objeto é utilizado. Uma vez que esses contadores forem zerados, significa que o objeto já não é mais necessário, então o GC remove a referência do objeto da memória liberando espaço para outros recursos. Mesmo sendo uma técnica utilizada em outras linguagens bastante renomadas, o Python possui um problema com objetos globais: eles não deixam de existir ao decorrer do programa, fazendo com que o trecho de memória a ele alocado nunca seja liberado, desse modo recomenda-se que os objetos globais não sejam objetos muito robustos, para que a performance do algoritmo seja cada vez melhor.

#Etapa 5 - Aula 7 - Escopo

Link: https://onlinegdb.com/r1jv7Rz_4

#Etapa 5 - Aula 7 - Qualidade de Código

A primeira ferramenta pesquisada é o PEP8 Online Checker: http://pep8online.com/

Foi usado o seguinte código em python:
https://github.com/pythonprobr/objetos_pythonicos/blob/master/programacao_funcional/decorador/tempo.py

Ao analisar o código através da ferramenta, obtivemos o seguinte resultado:

Code: W292
Line: 31
Column: 26
Text: no newline at end of file

A segunda ferramenta é Pylint Online: http://www.pylintonline.com

Já nessa ferramenta o resultado foi: 

[C0304] [ 31] [missing-final-newline]  >> Final newline missing 
[C0111] [  1] [missing-docstring]  >> Missing module docstring 
[W1113] [  7] [keyword-arg-before-vararg]  >> Keyword argument before variable positional arguments list in the definition of logar function logar
[C0103] [  7] [invalid-name]  >> Argument name "f" doesn't conform to snake_case naming style logar
[C0111] [  7] [missing-docstring]  >> Missing function docstring logar
[C0111] [ 13] [missing-docstring]  >> Missing function docstring mochileiro
[E1120] [ 12] [no-value-for-parameter]  >> No value for argument 'f' in function call mochileiro
[C0111] [ 18] [missing-docstring]  >> Missing function docstring ola
[E1120] [ 17] [no-value-for-parameter]  >> No value for argument 'f' in function call ola

------------------------------------------------------------------
Your code has been rated at 1.05/10 (previous run: 5.00/10, -3.95)

Conclusão: Foram obtidos retornos bem diferentes com as ferramentas.

#Etapa 6 - Aula 8 - Módulos

Link: https://repl.it/repls/VisibleExtrasmallPackagedsoftware

#Etapa 7 - Aula 9 - APIs

Link: https://repl.it/@vitorpaes1/PraticaAPI

#Etapa 8 - Aula 10 - GUI

(OBS: Baixar os arquivos no link abaixo e importar o projeto em uma IDE local, como o PyCharm)
https://drive.google.com/open?id=1KXLOU8UlB5Ihmy7sh0_FYrtH57MTKLR0
