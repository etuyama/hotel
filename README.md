# Sistema de gerenciamento de hotel


Criamos um sistema de gerenciamento de hotel, no qual é possível cadastrar clientes, quartos, funcionários e serviços. 
Temos também um controle de reservas, no qual cada reserva associa um quarto com um cliente. 
Em todas essas funções, é possível fazer a inclusão, alteração, listagem, e exclusão dessas classes.

## Quartos

Há 3 tipos de quarto: Standard, Suíte e Luxo, que são *classes filhas da classe abstrata Quarto*. Além disso, cada quarto tem 3 status possíveis: Disponível, Ocupado e Manutenção.
Cada quarto possui um valor de diária e uma descrição. Ao incluir um quarto a classe TelaQuarto pede essas informações, com
exceção do status, que inicializa como Disponível. Na alteração dos dados de um quarto é possível mudar esses status, tanto quanto as
outras informações. É importante ressaltar que não é possível alterar o número do quarto para um número que já exista, o mesmo na inclusão de quarto.

## Clientes e Funcionários

Os clientes e funcionários possuem nome e cpf *herdados da classe abstrata Pessoa*, porém os clientes também possuem data de nascimento, telefone e
endereço, e o funcionários têm cargo, data de admissão e salário. As funções de inclusão, alteração, listagem e inclusão são parecidas, sendo a mesma
ideia dos quartos, não é possível incluir um funcionário ou cliente com cpf já existente, nem alterar o cpf para algum já existente. Além disso no
controlador dos funcionários há uma função que lista todos os funcionários de um cargo específico inserido pelo usuário.


## Serviços

Temos os serviços que são fornecidos pelo hotel, cada serviço detém um nome, descrição, preço e id. Havendo a mesma ideia do CRUD citado
nas classes acima, fazendo as verificações se o nome e o id já existem.


## Reservas


A classe reserva é a classe chave de *Registro* do sistema, ela faz uma *associação* com a classe Quarto, e com a classe Cliente. Além disso, essa classe
possui um tempo de estadia dessa reserva, uma lista com os serviços utilizados(objetos da classe Serviço), um valor total que inicialmente
é calculado pelo valor da diária do quarto multiplicado pelo atributo tempo de estadia da reserva, a data que foi efetuada, e sua situação, que
inicia como Pendente, mas pode ser trocada para Finalizada.

As Reservas e todos esses atributos são controlados pelo ControladorReservas, no qual há diversas funções importantes para o funcionamento e consistência
do sistema. Temos a função "efetuar reserva", na qual utiliza-se o ControladorClientes e ControladorQuartos para ter acesso à essas classes,
pedindo ao usuário(através da TelaReserva) selecionar um cliente e um quarto, fazendo essa associação dos dois. Além disso também é pedido ao
usuário o tempo de estadia. A data e o id são gerados automaticamente, sendo a data gerada com a **data REAL** do dia que a reserva foi efetuada.
Após todos esses passos, a reserva é efetuada de fato, instanciando um objeto da classe Reserva(caso de *composição*), depois disso, o status
do quarto da reserva é trocado para Ocupado. Na função de alteração de reserva, seleciona-se uma reserva, porém só é possível alterar uma reserva
se sua situação estiver como Pendente e se o quarto que for selecionado estiver disponível. Há uma função que lista as reservas pendentes(usada em
praticamente todas as outras funções), caso não haja nenhuma reserva pendente é mostrada uma mensagem de aviso ; porém há também uma função que lista
todas as reservas independente da situação. Além disso há uma método que adiciona um serviço utilizado, o usuário também seleciona uma reserva, e depois seleciona
um serviço, adicionando-o a lista de serviços da reserva, e incrementando seu respectivo preço no atributo valor total da reserva escolhida. Também
é possível estender a estadia de uma reserva selecionada, fazendo o cálculo do novo valor e adicionando-o no valor total dessa reserva. Do mesmo modo, temos
também uma função que adiciona um valor extra à reserva que é selecionada, podendo ser uma multa por exemplo, esse valor é pedido ao usuário e adicionado ao 
valor total da reserva. Como forma de análise, o controladorReservas também é capaz de gerar relatórios: tipo de quarto mais reservado, reservas por cada mês 
de um determinado ano e ranking de clientes que realizaram mais reservas, esses relatórios são importantes para análise e tomada de decisões da equipe do hotel.


## Hotel

Por fim, o sistema contém um controlador geral do hotel. A entidade hotel possui um saldo, inicializado em zero, e uma avaliação, esses atributos serão alterados
somente com as funções deste controlador.

Por exemplo, há a função "realizar checkout", que pede ao usuário para selecionar uma reserva, e caso esta não esteja Finalizada, ou seja, caso esteja
Pendente, o check-out é realizado, **incrementando o valor total da reserva no saldo do hotel**. Após isso, automaticamente a situação da reserva selecionada 
é alterada para Finalizada e o status do respectivo quarto é alterado para manutenção. O controlador também contém uma lista de avaliações; dentro da função 
de efetuar reserva, após os procedimentos citados anteriormente, é chamada a função "avaliar hotel"(do próprio controlador), essa função solicita ao usuário 
uma avaliação da reserva, e caso essa avaliação seja um número inteiro de 1 a 5, adiciona-se esse valor à lista de avaliações, fazendo o cálculo da média dessas 
avaliações, e atribuindo o resultado desse cálculo ao atributo "avaliação" da classe Hotel. Como dito anteriormente, ao efetuar o check-out, o quarto entra em manutenção,
por isso também foi implementada uma função que finaliza a manutenção de um determinado quarto solicitado ao usuário. Além disso, há o método de pagar funcionário,
utiliza-se o controlador deste e pede-se ao usuário selecionar um funcionário, após isso, o valor do salário deste funcionário é decrementado do saldo do hotel.
Também há como pagar uma despesa, pedindo um valor ao usuário e também subtraindo esse valor do saldo do hotel. Todas essas operações que envolvem o saldo do hotel
vão para uma lista de transações, atributo do ControladorHotel, em forma de string, é possível chamar o método mostra saldo, que imprime o saldo do hotel junto com
essa lista das transações que ocorreram. Por último, há o método que mostra a avaliação do hotel(média), mostrando também a lista com todas as avaliações.



## Pontos adicionais

- Todas as solicitações ao usuário possuem uma verificação, a maioria feita na *classe abstrata Tela*
      * Verificação de número inteiro
      * Verificação de string
      * Verificação de CPF
      * Verificação de data
      * Verificação de telefone
  
- Um cliente pode efetuar múltiplas reservas ao mesmo tempo, sendo um caso de *Agregação*.

- Ao tentar efetuar uma reserva, é feito uma validação se o cliente já atingiu a maioridade. Esse cálculo é feito por meio de sua data de nascimento.

- Uma reserva só é efetuada se o quarto selecionado estiver Disponível.
  
- Os métodos que alteram de qualquer modo a reserva, somente serão efetuadas caso a reserva esteja  em situação Pendente.

- Nos métodos que o usuário precisa selecionar alguma entidade, é verificado se essa entidade existe ou se ela está disponível.

- Em todos os controladores é usado o conceito da *composição*.
  

