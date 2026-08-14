# Arquitetura de UX e Jornadas Principais

## Objetivo

Este documento define a navegação e os fluxos principais do MVP do DMP antes
da implementação completa da interface. Ele é a referência para o shell da
aplicação, o design visual e as telas de cada módulo.

O MVP será usado por funcionários da papelaria em um único computador. A
interface deve privilegiar operações rápidas, confirmação explícita de ações
irreversíveis e mensagens que expliquem como corrigir um problema.

## Estrutura De Navegação

O shell da aplicação terá um cabeçalho com o nome **DMP**, a data do caixa
atual e a navegação principal. Cada item abre uma área independente, sem
perder dados persistidos ou o carrinho ativo.

| Item da navegação | Objetivo | Ação principal |
| --- | --- | --- |
| **Produtos** | Consultar e cadastrar produtos, preço e estoque atual. | **Cadastrar produto** |
| **Fornecedores** | Consultar e cadastrar fornecedores e relacioná-los aos produtos. | **Cadastrar fornecedor** |
| **Vendas** | Iniciar venda à vista ou a prazo e consultar vendas realizadas. | **Nova venda** |
| **Estoque** | Registrar entradas, ajustes e consultar o histórico de movimentações. | **Registrar entrada** ou **Histórico de movimentações** |
| **Clientes** | Consultar clientes, compras a prazo, parcelas, saldo e recebimentos. | **Cadastrar cliente** ou **Registrar recebimento** |
| **Caixa diário** | Consultar o movimento do dia e fechar o caixa. | **Fechar caixa** |

### Regras Do Shell

- **Vendas** é a entrada para escolher **Venda à vista** ou **Venda a prazo**.
- A busca de produtos aceita **Código ou descrição** e deve aparecer no fluxo
  de qualquer nova venda.
- A área **Clientes** permite cadastrar clientes a qualquer momento, mesmo sem
  uma venda a prazo em execução.
- Em **Clientes**, o funcionário pode iniciar **Cadastrar cliente** ou
  **Registrar recebimento**. O cadastro independente não depende de uma venda
  em andamento.
- Ao escolher **Venda a prazo**, o funcionário deve selecionar **Cliente
  cadastrado** ou **Criar cliente** antes de continuar. **Criar cliente** é um
  atalho contextual para o mesmo cadastro de clientes.
- A área **Caixa diário** mostra um único caixa por dia; abertura, sangria,
  suprimento e despesas não fazem parte do MVP.
- A navegação não deve ocultar validações ou confirmações pendentes de uma
  operação em andamento.
- Todas as telas devem usar textos em português e valores monetários no formato
  de reais, por exemplo `R$ 12,50`.

## Jornada 1: Cadastrar Fornecedor

### Objetivo

Cadastrar um fornecedor para que ele possa ser definido como fornecedor
principal ou alternativo de produtos e associado a entradas de estoque.

### Fluxo principal

1. O funcionário acessa **Fornecedores** e seleciona **Cadastrar fornecedor**.
2. Informa o **Nome do fornecedor**. Pode informar também **Telefone**,
   **E-mail** e **Observação**.
3. O sistema mostra um resumo dos dados preenchidos e pede confirmação em
   **Confirmar cadastro**.
4. O sistema salva o fornecedor como ativo.
5. A tela de sucesso mostra **Fornecedor cadastrado** e oferece as ações
   **Cadastrar outro fornecedor**, **Cadastrar produto** e **Ver fornecedor**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Catálogo sem fornecedores | Vazio | **Nenhum fornecedor cadastrado. Cadastre o primeiro fornecedor para começar.** |
| Nome ausente | Validação | **Informe o nome do fornecedor.** |
| Resumo do cadastro | Confirmação | **Confirme o cadastro do fornecedor [nome].** |
| Falha no registro | Erro | **Não foi possível cadastrar o fornecedor. Tente novamente.** Os dados preenchidos são preservados. |
| Registro concluído | Sucesso | **Fornecedor cadastrado com sucesso.** |

## Jornada 2: Consultar Produtos Do Fornecedor

### Objetivo

Consultar os produtos relacionados a um fornecedor para apoiar o planejamento
de reposição e distinguir os produtos em que ele é principal ou alternativo.

### Fluxo principal

1. O funcionário acessa **Fornecedores** e seleciona um fornecedor.
2. Seleciona **Ver fornecedor**.
3. O sistema mostra os dados do fornecedor e duas seções de produtos:
   **Produtos principais** e **Produtos alternativos**.
4. Cada produto mostra **Código**, **Descrição**, **Preço de venda** e
   **Estoque atual**.
5. O funcionário seleciona um produto para **Ver produto** ou usa **Voltar
   para fornecedores** para retornar à lista.
6. A tela oferece **Cadastrar produto** quando o funcionário precisar incluir um
   novo produto relacionado a esse fornecedor.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Fornecedor sem produtos | Vazio | **Este fornecedor ainda não está relacionado a nenhum produto.** A tela oferece **Cadastrar produto**. |
| Sem produtos principais | Vazio | **Este fornecedor não é o principal de nenhum produto.** |
| Sem produtos alternativos | Vazio | **Este fornecedor não está cadastrado como alternativa de nenhum produto.** |
| Produtos encontrados | Sucesso | Lista os produtos separados entre principais e alternativos, ordenados por descrição. |
| Fornecedor não encontrado | Erro | **Não foi possível localizar o fornecedor. Volte para a lista e tente novamente.** |
| Falha ao consultar produtos | Erro | **Não foi possível carregar os produtos deste fornecedor. Tente novamente.** |

## Jornada 3: Cadastrar Produto

### Objetivo

Cadastrar um produto no catálogo para que ele possa ser consultado, vendido e
relacionado aos fornecedores. O funcionário pode informar o estoque inicial do
produto; novas unidades recebidas depois do cadastro são registradas pela
jornada de **Entrada de estoque**.

### Fluxo principal

1. O funcionário acessa **Produtos** e seleciona **Cadastrar produto**.
2. Informa o **Código**, a **Descrição**, o **Preço de venda** e o **Estoque
   inicial**.
3. Seleciona um **Fornecedor principal** já cadastrado. Opcionalmente, seleciona
   um ou mais **Fornecedores alternativos** também já cadastrados.
4. O sistema mostra um resumo com código, descrição, preço, fornecedores e
   **Estoque inicial: [quantidade] unidade(s)**.
5. O funcionário seleciona **Confirmar cadastro**.
6. O sistema cria o produto com o estoque inicial informado, salva as relações
   com os fornecedores selecionados e registra a **Entrada inicial** no
   histórico de estoque, inclusive quando a quantidade for `0`.
7. A tela de sucesso mostra **Produto cadastrado** e oferece as ações
   **Cadastrar outro produto**, **Ver produto** e **Ver histórico de
   movimentações**. A ação **Registrar entrada** fica disponível para adicionar
   unidades depois do cadastro.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Catálogo sem produtos | Vazio | **Nenhum produto cadastrado. Cadastre o primeiro produto para começar.** |
| Código ausente | Validação | **Informe o código do produto.** |
| Código já cadastrado | Validação | **Já existe um produto com este código. Informe outro código.** |
| Descrição ausente | Validação | **Informe a descrição do produto.** |
| Preço ausente ou inválido | Validação | **Informe um preço de venda maior que zero.** |
| Estoque inicial ausente ou inválido | Validação | **Informe uma quantidade inteira de estoque maior ou igual a zero.** |
| Fornecedor principal não selecionado | Validação | **Selecione um fornecedor principal para cadastrar o produto.** |
| Fornecedor não encontrado | Validação | **Selecione um fornecedor cadastrado ou cadastre um novo fornecedor.** |
| Resumo do cadastro | Confirmação | **Confirme o cadastro do produto [descrição] com preço de [valor] e estoque inicial de [quantidade] unidade(s).** |
| Falha no registro | Erro | **Não foi possível cadastrar o produto. Tente novamente.** Os dados preenchidos são preservados. |
| Registro concluído | Sucesso | **Produto cadastrado com sucesso. Estoque inicial: [quantidade] unidade(s).** |

## Convenções De Interface

### Ações

| Intenção | Rótulo |
| --- | --- |
| Começar uma venda | **Nova venda** |
| Acrescentar produto | **Adicionar ao carrinho** |
| Alterar quantidade | **Quantidade** |
| Alterar preço praticado | **Preço praticado** |
| Avançar para pagamento | **Continuar para pagamento** |
| Consultar estoque | **Ver histórico de movimentações** |
| Confirmar operação | **Confirmar venda**, **Confirmar entrada**, **Confirmar ajuste** ou **Confirmar fechamento** |
| Abandonar uma operação | **Cancelar operação** |
| Corrigir dados | **Voltar e editar** |
| Cancelar uma venda já registrada | **Cancelar venda** |

### Mensagens

- Mensagens de erro devem dizer o que aconteceu e como corrigir, sem expor
  detalhes técnicos.
- Ações que alteram estoque, dívida ou caixa exigem uma confirmação antes do
  registro definitivo.
- Preços, valores de parcelas e pagamentos informados pelo funcionário devem
  ser maiores que zero. Valores negativos ou com sinal de menos são rejeitados
  antes da confirmação.
- Quantidades adicionadas a vendas e a movimentações de estoque devem ser
  maiores que zero. A única movimentação que aceita quantidade `0` é a
  **Entrada inicial** do produto; entradas posteriores, vendas, cancelamentos e
  ajustes exigem quantidade positiva. Estoque inicial e contagem física podem
  ser zero.
- Subtotais, saldos e diferenças são valores calculados; podem resultar em
  zero e uma diferença de ajuste pode ser negativa sem permitir entrada
  negativa pelo funcionário.
- Uma mensagem de sucesso deve identificar o resultado da operação, por
  exemplo o número da venda, o novo saldo ou a diferença do caixa.
- Campos obrigatórios devem ser marcados e validados no contexto da ação que
  depende deles.

## Estados Compartilhados

As telas críticas usam os seguintes estados visíveis:

| Estado | Comportamento esperado |
| --- | --- |
| Vazio | Explica que ainda não há registros e oferece a primeira ação possível. |
| Validação | Mantém os dados preenchidos, destaca os campos inválidos e explica a correção. |
| Erro | Informa que a operação não foi concluída e permite tentar novamente sem apagar os dados. |
| Confirmação | Resume o impacto da ação e oferece **Confirmar** e **Voltar e editar**. |
| Sucesso | Confirma o registro e oferece a próxima ação relevante. |

## Jornada 4: Consultar Histórico De Movimentações

### Objetivo

Permitir que o funcionário explique a formação do estoque consultando todos os
movimentos ou apenas os movimentos de um produto.

### Entradas da tela

- Em **Produtos**, o funcionário seleciona **Ver produto** e depois **Ver
  histórico de movimentações**. A tela abre filtrada para aquele produto.
- Em **Estoque**, o funcionário seleciona **Histórico de movimentações**. A
  tela abre com todos os produtos e permite filtrar por **Produto**, **Tipo de
  movimentação** e **Data**.

### Fluxo principal

1. O funcionário acessa o histórico por uma das entradas disponíveis.
2. O sistema lista os movimentos do mais recente para o mais antigo.
3. Cada linha mostra **Data e hora**, **Produto**, **Tipo**, **Quantidade**,
   **Estoque antes** e **Estoque depois**.
4. O funcionário seleciona um movimento para ver os detalhes, incluindo
   **Fornecedor**, quando houver, **Origem** e **Observação**.
5. O funcionário pode selecionar **Ver produto** ou **Voltar para estoque**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Histórico sem movimentações | Vazio | **Nenhuma movimentação de estoque registrada.** |
| Produto sem movimentações | Vazio | **Este produto ainda não possui movimentações de estoque.** |
| Filtros sem resultado | Vazio | **Nenhuma movimentação encontrada para os filtros informados.** |
| Histórico carregado | Sucesso | Lista os movimentos em ordem decrescente de data e hora. |
| Detalhe do movimento | Sucesso | Mostra todos os dados do movimento selecionado e permite voltar à lista. |
| Falha ao consultar histórico | Erro | **Não foi possível carregar o histórico de estoque. Tente novamente.** |

## Jornada 5: Cadastrar Cliente

### Objetivo

Cadastrar um cliente a qualquer momento, inclusive antes de iniciar uma venda a
prazo, para que ele possa ser localizado e associado a compras futuras.

### Fluxo principal

1. O funcionário acessa **Clientes** e seleciona **Cadastrar cliente**.
2. Informa o **Nome do cliente**. Pode informar também **Telefone** e
   **Observação**.
3. O sistema mostra um resumo dos dados preenchidos e pede confirmação em
   **Confirmar cadastro**.
4. O sistema salva o cliente, sem criar venda, dívida ou recebimento.
5. A tela de sucesso mostra **Cliente cadastrado** e oferece as ações
   **Cadastrar outro cliente**, **Ver cliente** e **Nova venda a prazo**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Lista sem clientes | Vazio | **Nenhum cliente cadastrado. Cadastre o primeiro cliente para começar.** |
| Nome ausente | Validação | **Informe o nome do cliente.** |
| Resumo do cadastro | Confirmação | **Confirme o cadastro do cliente [nome].** |
| Falha no registro | Erro | **Não foi possível cadastrar o cliente. Tente novamente.** Os dados preenchidos são preservados. |
| Registro concluído | Sucesso | **Cliente cadastrado com sucesso.** Nenhuma venda ou dívida foi criada. |

## Jornada 6: Venda À Vista

### Objetivo

Registrar uma venda recebida no momento da compra, reduzindo o estoque e
registrando um recebimento no caixa diário.

### Fluxo principal

1. O funcionário acessa **Vendas** e seleciona **Nova venda** > **Venda à
   vista**.
2. O sistema exibe o campo **Código ou descrição**.
3. O funcionário pesquisa um produto e seleciona um resultado. O resultado
   mostra **Descrição**, **Código**, **Preço cadastrado** e **Estoque
   disponível**.
4. O funcionário informa **Quantidade** e seleciona **Adicionar ao carrinho**.
5. Se o produto já estiver no carrinho, o sistema soma a quantidade em uma
   única linha.
6. O carrinho mostra **Produto**, **Quantidade**, **Preço praticado** e
   **Subtotal**. O funcionário pode alterar a quantidade, o preço praticado
   ou remover o item.
7. O funcionário seleciona **Continuar para pagamento**.
8. A tela de pagamento mostra **Total da venda** e exige uma única forma:
   **Dinheiro**, **Pix**, **Débito** ou **Crédito**.
9. Antes da confirmação, o sistema revalida o estoque disponível de todos os
   itens, considerando as quantidades e preços atuais do carrinho.
10. Se todos os itens estiverem disponíveis, o sistema mostra um resumo e pede
    confirmação: **Confirmar venda**.
11. Após a confirmação, o sistema registra a venda, reduz o estoque, cria o
    recebimento imediato e inclui o valor no caixa do dia dentro da mesma
    operação.
12. No momento da confirmação, o sistema registra a **Data e hora de
    finalização** da venda.
13. A tela de sucesso mostra **Venda concluída**, o identificador da venda e a
    data e hora de finalização, com as ações **Nova venda** e **Ir para o caixa
    diário**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Carrinho inicial | Vazio | **Seu carrinho está vazio. Busque um produto para começar.** |
| Busca sem resultado | Vazio | **Nenhum produto encontrado. Confira o código ou tente outra descrição.** |
| Quantidade inválida | Validação | **Informe uma quantidade maior que zero.** |
| Estoque insuficiente ao adicionar ou editar | Validação | **Estoque insuficiente. Disponível: [quantidade].** O item não é adicionado ou editado acima do saldo disponível. |
| Estoque insuficiente ao finalizar | Validação | **O estoque de [produto] mudou. Disponível: [quantidade]. Revise o carrinho.** A venda não é confirmada e o carrinho permanece disponível. |
| Produto sem preço | Validação | **Este produto não tem preço cadastrado. Atualize o cadastro antes de vender.** |
| Carrinho sem itens ao avançar | Validação | **Adicione pelo menos um produto para continuar.** |
| Forma não escolhida | Validação | **Escolha uma forma de pagamento.** |
| Preço praticado inválido | Validação | **Informe um preço praticado maior que zero.** Valores negativos não são permitidos. |
| Resumo antes do registro | Confirmação | **Confirme a venda de [total] em [forma de pagamento].** |
| Falha no registro | Erro | **Não foi possível concluir a venda. Tente novamente.** O carrinho permanece disponível. |
| Registro concluído | Sucesso | **Venda concluída em [data e hora]. Estoque e caixa foram atualizados.** |

## Jornada 7: Venda A Prazo

### Objetivo

Registrar uma venda sem recebimento imediato, associando-a a um cliente e
criando uma dívida com uma ou mais parcelas.

### Fluxo principal

1. O funcionário acessa **Vendas** e seleciona **Nova venda** > **Venda a
   prazo**.
2. O funcionário monta o carrinho usando a mesma busca da venda à vista.
3. Na etapa **Cliente**, o funcionário escolhe **Cliente cadastrado** ou
   **Criar cliente**.
4. Ao escolher **Cliente cadastrado**, pesquisa por **Nome ou telefone** e
   seleciona um cliente existente. Ao escolher **Criar cliente**, informa
   **Nome** e, opcionalmente, **Telefone** e **Observação**; o novo cliente é
   salvo e associado à venda.
5. Na etapa **Condições da venda**, o funcionário escolhe entre **Uma dívida**
   e **Parcelar compra**.
6. Para uma dívida única, informa o **Vencimento da dívida**.
7. Para uma compra parcelada, informa o **Número de parcelas**. O sistema
   calcula automaticamente o valor e o vencimento de cada parcela:
   - O valor total é dividido em centavos entre as parcelas. Se sobrarem
     centavos, eles são distribuídos um a um entre as primeiras parcelas para
     que a soma permaneça exatamente igual ao total.
   - A **Parcela 1** vence um mês depois da data da venda, a **Parcela 2** dois
     meses depois, e assim por diante, mantendo o mesmo dia quando existir no
     mês. Quando o mês não tiver esse dia, usa o último dia do mês.
   - Cada parcela aparece identificada com **Valor da parcela** e
     **Vencimento**. O funcionário pode editar tanto os valores quanto as
     datas antes de continuar.
8. O sistema mostra **Cliente**, itens, **Total da venda**, vencimento ou
   parcelas editadas e **Total em aberto**.
9. O funcionário seleciona **Confirmar venda a prazo**.
10. Após a confirmação, o sistema registra a venda, reduz o estoque e cria a
    dívida e suas parcelas. Não é criado recebimento imediato.
11. No momento da confirmação, o sistema registra a **Data e hora de
    finalização** da venda.
12. A tela de sucesso mostra **Venda a prazo concluída**, o cliente, o total em
    aberto e a data e hora de finalização, com a ação **Ver dívida do cliente**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Opção de cliente não selecionada | Validação | **Escolha Cliente cadastrado ou Criar cliente para continuar.** |
| Cliente cadastrado sem resultados | Vazio | **Cliente não encontrado. Escolha Criar cliente ou tente outra busca.** |
| Cliente não selecionado | Validação | **Selecione um cliente para registrar uma venda a prazo.** |
| Nome ausente no cadastro | Validação | **Informe o nome do cliente.** |
| Número de parcelas inválido | Validação | **Informe pelo menos uma parcela.** |
| Número de parcelas maior que o total | Validação | **O número de parcelas não pode ser maior que o total disponível em centavos.** |
| Vencimento da dívida ausente | Validação | **Informe o vencimento da dívida.** |
| Vencimento de parcela ausente | Validação | **Informe o vencimento da parcela [n].** A venda não pode ser confirmada enquanto qualquer parcela estiver sem vencimento. |
| Soma das parcelas diferente do total | Validação | **A soma das parcelas deve ser igual ao total da venda.** |
| Valor de parcela inválido | Validação | **Cada parcela deve ter um valor maior que zero.** |
| Venda sem estoque suficiente | Validação | Usa a mesma mensagem de estoque da venda à vista e não conclui a operação. |
| Resumo de cliente e condições | Confirmação | **Confirme a venda a prazo de [total] para [cliente].** |
| Falha no registro | Erro | **Não foi possível registrar a venda a prazo. Tente novamente.** Os dados preenchidos são preservados. |
| Registro concluído | Sucesso | **Venda a prazo concluída em [data e hora]. Dívida criada para [cliente].** |

## Jornada 8: Consultar Vendas

### Objetivo

Localizar vendas já finalizadas ou canceladas pelo número da venda ou pelo
dia e hora em que foram finalizadas.

### Fluxo principal

1. O funcionário acessa **Vendas** e seleciona **Consultar vendas**.
2. Escolhe um modo de busca: **Número da venda** ou **Data e hora**.
3. Se escolher **Número da venda**, informa o número da venda.
4. Se escolher **Data e hora**, seleciona a **Data da venda** e uma **Hora da
   venda**. A hora representa o intervalo completo daquela hora: por exemplo,
   `15:00` busca vendas finalizadas de `15:00:00` até antes de `16:00:00`.
5. Seleciona **Pesquisar**.
6. O sistema lista as vendas encontradas com **Número**, **Data e hora de
   finalização**, **Tipo**, **Total**, **Cliente** quando houver e **Status**.
7. O funcionário seleciona uma venda para visualizar seus itens, pagamento ou
   dívida e os detalhes do histórico.
8. A busca pode ser refeita alterando os filtros ou selecionando **Limpar
   filtros**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Modo de busca não selecionado | Validação | **Escolha buscar por número da venda ou por data e hora.** |
| Número ausente | Validação | **Informe o número da venda.** |
| Data ausente | Validação | **Selecione a data da venda.** |
| Hora ausente | Validação | **Selecione a hora da venda.** |
| Hora selecionada | Sucesso | Busca todas as vendas finalizadas dentro da hora escolhida, das `HH:00:00` até antes da próxima hora. |
| Nenhuma venda encontrada | Vazio | **Nenhuma venda encontrada para os filtros informados.** |
| Resultados encontrados | Sucesso | Lista as vendas ordenadas da mais recente para a mais antiga. |
| Falha na consulta | Erro | **Não foi possível consultar as vendas. Tente novamente.** |

## Jornada 9: Consultar Dívida E Registrar Pagamento

### Objetivo

Localizar as compras a prazo de um cliente, identificar a dívida correta e
registrar um pagamento total ou parcial.

### Fluxo principal

1. O funcionário acessa **Clientes** e pesquisa por **Nome ou telefone**.
2. Seleciona o cliente e visualiza **Compras a prazo**, **Parcelas**,
   **Pagamentos realizados** e **Total em aberto**.
3. Seleciona a compra que está sendo paga. Cada compra aparece separadamente
   com data, total, vencimento, valor pago e saldo.
4. Seleciona **Registrar recebimento**, informa **Valor recebido** e escolhe
   uma **Forma de pagamento**: **Dinheiro**, **Pix**, **Débito** ou **Crédito**.
5. O sistema mostra o saldo anterior, o valor informado, a forma de pagamento
   e o saldo após o recebimento.
6. O funcionário confirma em **Confirmar recebimento**.
7. O sistema registra o recebimento associado à compra selecionada e atualiza
   a parcela, a dívida do cliente e o caixa diário.
8. A tela de sucesso mostra **Recebimento registrado** e o **Novo saldo em
   aberto**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Busca sem clientes | Vazio | **Nenhum cliente encontrado.** |
| Cliente sem compras em aberto | Vazio | **Este cliente não possui compras a prazo em aberto.** |
| Nenhuma compra selecionada | Validação | **Selecione a compra que está sendo paga.** |
| Valor ausente ou zero | Validação | **Informe um valor recebido maior que zero.** |
| Valor acima do saldo | Validação | **O valor recebido não pode ser maior que o saldo em aberto.** |
| Forma de pagamento não escolhida | Validação | **Escolha uma forma de pagamento.** |
| Resumo do recebimento | Confirmação | **Confirme o recebimento de [valor] em [forma] para a compra de [data].** |
| Falha no registro | Erro | **Não foi possível registrar o recebimento. Tente novamente.** |
| Pagamento registrado | Sucesso | **Recebimento registrado. Novo saldo em aberto: [valor].** |

## Jornada 10: Entrada De Estoque

### Objetivo

Adicionar unidades recebidas ao estoque e registrar a movimentação, com
fornecedor opcional.

### Fluxo principal

1. O funcionário acessa **Estoque** e seleciona **Registrar entrada**.
2. Pesquisa o produto por **Código ou descrição** e informa **Quantidade
   recebida**.
3. Opcionalmente seleciona um **Fornecedor**.
4. Confere o **Estoque atual** e o **Novo estoque**.
5. Informa uma **Observação**, se necessário, e seleciona **Confirmar
   entrada**.
6. O sistema registra o movimento de entrada e atualiza o estoque.
7. A tela de sucesso mostra **Entrada registrada** e o novo saldo.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Histórico sem movimentações | Vazio | **Nenhuma movimentação de estoque registrada.** |
| Produto não encontrado | Validação | **Selecione um produto cadastrado.** |
| Quantidade inválida | Validação | **Informe uma quantidade recebida maior que zero.** |
| Resumo do impacto | Confirmação | **O estoque passará de [atual] para [novo]. Confirmar entrada?** |
| Falha no registro | Erro | **Não foi possível registrar a entrada. Tente novamente.** |
| Registro concluído | Sucesso | **Entrada registrada. Novo estoque: [quantidade].** |

## Jornada 11: Ajuste De Inventário

### Objetivo

Corrigir uma divergência entre o estoque registrado e a contagem física,
mantendo o histórico da alteração.

### Fluxo principal

1. O funcionário acessa **Estoque** e seleciona **Ajustar inventário**.
2. Pesquisa e seleciona um produto.
3. O sistema mostra **Estoque registrado**.
4. O funcionário informa **Quantidade contada** e o **Motivo do ajuste**.
5. O sistema calcula a diferença e mostra o novo saldo.
6. O funcionário seleciona **Confirmar ajuste**.
7. O sistema grava um movimento de ajuste e atualiza o estoque.
8. A tela de sucesso mostra **Ajuste registrado** e a diferença aplicada.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Produto não selecionado | Validação | **Selecione um produto para ajustar.** |
| Quantidade inválida | Validação | **Informe uma quantidade contada igual ou maior que zero.** |
| Motivo ausente | Validação | **Informe o motivo do ajuste.** |
| Sem diferença | Validação | **A quantidade contada é igual ao estoque registrado. Nenhum ajuste é necessário.** |
| Resumo da diferença | Confirmação | **O estoque será ajustado em [diferença] unidade(s). Confirmar ajuste?** |
| Falha no registro | Erro | **Não foi possível registrar o ajuste. Tente novamente.** |
| Registro concluído | Sucesso | **Ajuste registrado. Novo estoque: [quantidade].** |

## Jornada 12: Cancelar Venda Não Paga

### Objetivo

Corrigir uma venda não paga sem apagar o histórico, restaurando as unidades
ao estoque e retirando a venda dos totais líquidos.

### Fluxo principal

1. O funcionário acessa **Vendas** e pesquisa pelo **Número da venda** ou pelos
   filtros de data e hora de finalização.
2. Seleciona uma venda com status **Concluída** e sem recebimento associado.
3. Confere os itens, o total e o impacto: **O estoque será restaurado e a
   venda não entrará nos totais líquidos.**
4. Seleciona **Cancelar venda**.
5. O sistema pede confirmação com o motivo opcional: **Esta ação não pode ser
   desfeita. Confirmar cancelamento?**
6. Após confirmar, a venda passa para **Cancelada**, o estoque é restaurado e
   um movimento de cancelamento é criado. O registro original permanece no
   histórico.
7. A tela de sucesso mostra **Venda cancelada** e o estoque restaurado.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Nenhuma venda encontrada | Vazio | **Nenhuma venda encontrada para os filtros informados.** |
| Venda já cancelada | Validação | **Esta venda já está cancelada.** |
| Venda paga | Validação | **Vendas com recebimento não podem ser canceladas no MVP.** |
| Venda aberta | Validação | **Finalize ou descarte a venda antes de consultar o cancelamento.** |
| Antes do cancelamento | Confirmação | **Esta ação restaurará [quantidade] unidade(s) e removerá [valor] dos totais líquidos.** |
| Falha no cancelamento | Erro | **Não foi possível cancelar a venda. Nenhuma alteração foi aplicada.** |
| Cancelamento concluído | Sucesso | **Venda cancelada. O estoque foi restaurado e o histórico foi mantido.** |

## Jornada 13: Fechar Caixa Diário

### Objetivo

Conferir o movimento do dia com os valores físicos contados e fechar o caixa
com uma senha específica.

### Fluxo principal

1. O funcionário acessa **Caixa diário** e escolhe a data atual.
2. O sistema mostra quatro blocos separados:
   - **Vendas à vista**: total das vendas recebidas no momento da compra,
     detalhado por **Dinheiro**, **Pix**, **Débito** e **Crédito**.
   - **Vendas a prazo**: total contratado no dia, sem somar esse valor ao
     recebido enquanto não houver pagamento.
   - **Recebimentos de débitos**: pagamentos de compras a prazo anteriores,
     detalhados por forma de pagamento.
   - **Total recebido no dia**: soma de vendas à vista e recebimentos de
     débitos.
3. O sistema mostra **Total esperado para conferência**, igual ao **Total
   recebido no dia**. Vendas a prazo não pagas ficam fora desse total.
4. O funcionário informa os valores físicos conferidos por forma de pagamento:
   **Dinheiro contado**, **Pix conferido**, **Débito conferido** e **Crédito
   conferido**, quando aplicável.
5. O sistema calcula e mostra a **Diferença** entre o total esperado e o total
   contado.
6. O funcionário seleciona **Fechar caixa**.
7. O sistema mostra o resumo da conferência e pede a **Senha de fechamento**.
8. Com a senha correta, o funcionário confirma em **Confirmar fechamento**.
9. A tela de sucesso mostra **Caixa fechado**, data, cada categoria e o total
   recebido com a diferença registrada.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Dia sem movimento | Vazio | **Não há movimentações registradas neste dia.** O fechamento continua disponível. |
| Contagem ausente | Validação | **Informe os valores contados antes de fechar o caixa.** |
| Valor contado inválido | Validação | **Informe um valor igual ou maior que zero.** |
| Senha ausente | Validação | **Informe a senha de fechamento.** |
| Senha incorreta | Erro | **Senha de fechamento incorreta. O caixa não foi fechado.** |
| Caixa já fechado | Validação | **O caixa deste dia já está fechado.** |
| Resumo antes do fechamento | Confirmação | **Confirme o fechamento do caixa de [data]. Total recebido: [valor]. Diferença: [valor].** |
| Falha no fechamento | Erro | **Não foi possível fechar o caixa. Tente novamente.** |
| Fechamento concluído | Sucesso | **Caixa fechado com sucesso. Diferença registrada: [valor].** |

## Regras De Escopo Representadas Na UX

- Uma venda à vista usa somente uma forma de pagamento no MVP.
- Venda a prazo exige cliente e vencimento, mesmo quando não há parcelas
  múltiplas.
- Pagamentos podem ser parciais, mas não podem exceder o saldo em aberto.
- Venda paga não pode ser cancelada no MVP.
- Cancelamento mantém o histórico e restaura o estoque.
- Toda alteração de estoque deve mostrar o saldo antes e depois.
- O caixa consolida vendas e recebimentos, sem modelar despesas ou operações de
  abertura.
- Não há usuários individuais nem permissões diferentes entre funcionários.

## Critérios De Pronto Para A Próxima Implementação

- A navegação contém exatamente os seis módulos definidos neste documento.
- Cada jornada possui uma entrada clara, etapas, confirmação e sucesso.
- Os estados vazio, validação, erro, sucesso e confirmação estão definidos nos
  pontos críticos de cada jornada.
- Os textos apresentados ao usuário podem ser implementados diretamente em
  português.
- O design visual pode usar este documento sem precisar decidir novamente as
  regras de negócio do MVP.
