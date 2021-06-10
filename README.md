<img src="https://img.icons8.com/color/48/000000/python.png"/>

### Conversão de Polegadas

Como dito por um importante personagem de um igualmente memorável filme: *"palavras são, na minha nada humilde opinião, nossa inesgotável fonte de magia [...]"*. Evidentemente, seria difícil formar palavras se não houve uma alfabeto bem estabelecido e divulgado, assim como em nosso alfabeto latino.

O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres diferentes, se desconsiderarmos as acentuações e as diferenças entre letras maiúsculas e minúsculas.

Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. Em um dos desenhos, Harry escreve na primeira linha de uma folha o primeiro caractere do alfabeto, na segunda linha escreve duas vezes o segundo caractere, na terceira linha escreve três vezes o terceiro caractere e assim por diante. Harry percebeu que com isso consegue formar um triângulo alfabético.

Como Harry precisa estudar para realizar uma prova de programação (que para ele também é uma forma de magia!), pediu para você ajudá-lo a automatizar os desenhos de "triângulos alfabéticos", criando um programa que receba como entrada um número inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a mesma estratégia descrita no texto.

### Entrada

Um número inteiro N (1 <= N <= 26).

### Saída

Um triângulo alfabético com exatas N linhas e com a mesma estratégia de construção mencionada no texto. Note que as letras são sempre maiúsculas.

<hr>

### Intervalo de primos!

Os números primos têm diversas aplicações, principalmente na criptografia utilizada pelo aplicativo de seu banco e nos sites de compra que nos trazem tanta comodidade.

Um número natural é considerado primo quando possui somente dois divisores, o número um e ele próprio. O número zero e o número um não são primos e o número dois é o único primo par.

Seu objetivo é criar um programa que receba como entrada dois números naturais, INÍCIO e FIM, e exibe os números primos que existem no intervalo fechado [ INÍCIO..FIM ]. Ao final, o programa também deve exibir a quantidade de primos encontrados no intervalo.

### Entrada

Dois números naturais, INÍCIO e FIM, respectivamente, um por linha. Adote (INICIO <= FIM <= 5000).

### Saída

Os números primos presentes no intervalo fechado [ INÍCIO..FIM ] e a quantidade de números primos do intervalo, conforme o padrão exibido nos exemplos.

<hr>

### Tabuada

Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

### Entrada

Um número natural N (0 <= N <= 10).

### Saída

Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos.

<hr>

### Doação

Ao perceber que um de seus amigos estava com dificuldades financeiras, Victória, uma garota muito inteligente, decidiu ajudá-lo com uma "vaquinha digital", em que todos poderiam doar quanto pudessem para ajudar seu amigo.

Para isso, Victória criou uma criptomoeda, a *Vic Coin*, em que cada unidade equivale à R$ 2,50. Assim, as pessoas que doarão primeiro compram a criptomoeda e, em seguida, depositam uma parte delas para doação. A parte que não foi doada pode ficar guardada em uma carteira digital e poderá ser usada no futuro para outras doações. Genial!

Victória está ocupada implementando o que é necessário para o funcionamento do ambiente de doações, por isso pediu para que você a ajudasse com uma das partes essenciais: a contabilização de doações e a conversão para reais.

Seu papel é criar um programa que receba como entrada diversas doações feitas em *Vic Coin* e, ao final, exiba o total em *Vic Coin* (VC$) e o total convertido para reais (R$).

### Entrada

Diversos números reais, um por linha, que representam os valores das doações feitas em *Vic Coin*. A entrada será finalizada com o valor de doação -1.0 que não deverá ser contabilizado na soma das doações.

### Saída

Duas linhas. A primeira linha será um valor real com duas casas decimais indicando o total doado em Vic Coin (VC$); a segunda linha será um valor real com duas casas decimais que indica o total doado em reais (R$). Veja nos exemplos o formato de saída.

<hr>

### Pague o aluguel!

Ramón está com problemas para pagar o aluguel de sua casa, o pior é que total da dívida é enorme, pois ele tem muitos pagamentos em atraso, atualmente são mais de 14 meses atrasados!

A casa de Ramón está em uma vila em que todas as casas pertencem a uma única pessoa, o Senhor Édgar. Para quitar a dívida, Ramón fez um acordo com Senhor Édgar, prometendo pagar mensalmente um valor que será descontado da dívida total. Ele se comprometeu a sempre pagar o mesmo valor até que a dívida seja encerrada. Porém, se o valor que ele puder pagar superar o valor da dívida, ele pagará exatamente o que deve e não mais, evidentemente.

Como Ramón não tem um controle adequado para atualizar o valor da dívida de acordo com os valores pagos, pediu sua ajuda para construir um programa que receba como entrada o valor da dívida e o valor que se comprometeu a pagar mensalmente, o programa deve exibir, mês a mês, o valor da dívida antes e depois do pagamento.



#### Entrada

Dois números inteiros positivos, o primeiro representa o valor total da dívida e o segundo o valor que Ramón poderá pagar mensalmente.

### Saída

O número do pagamento, o valor restante da dívida antes do pagamento mensal e o valor restante da dívida após o pagamento mensal, conforme o padrão exibido nos exemplos. A exibição deve continuar até que a dívida seja quitada.

<hr>

### Anos bissextos

Você sabe o que são anos bissextos? Resumidamente, em anos bissextos o mês de fevereiro é mais extenso, passando de 28 para 29 dias. O cálculo para descobrir se um ano é bissexto também é bastante simples, pois um ano é bissexto se é divisível por 4 e não por 100, ou se é divisível por 400.

Claudia adora anos bissextos, porque ela nasceu em um! Mais precisamente, Claudia nasceu no dia 29 de fevereiro, por isso sente que seu aniversário só ocorre "de verdade" nos anos que são bissextos, afinal pode projetar a festa sem ter que explicar aos amigos se comemorará no dia 28 de fevereiro ou no dia 01 de março.

Você foi convidado para a comemoração de Claudia, mas para isso ela pediu um presente especial, solicitou que você construa um programa que a ajude a ficar menos ansiosa para saber quais são os anos em que ela poderá realizar festas na data correta. Para isso, seu programa deverá receber um ano INÍCIO e um ano FIM e exibir todos os anos bissextos do intervalo fechado [ INÍCIO..FIM ]. Ao final, o programa também deve exibir a quantidade de anos bissextos do intervalo.

### Entrada

Dois números naturais, um em cada linha, que representam o ano INÍCIO e o ano FIM do intervalo considerado. Adote que (0 <= INÍCIO <= FIM <= 9999) sempre será verdade.

### Saída

Todos os anos bissextos do intervalo fechado [ INÍCIO..FIM ], um por linha. Ao final, o programa deve exibir a quantidade de anos bissextos, conforme os exemplos.

