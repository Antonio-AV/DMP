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
| **Estoque** | Registrar entradas, ajustes e consultar o histórico de movimentações. | **Registrar entrada** |
| **Clientes** | Consultar clientes, compras a prazo, parcelas, saldo e recebimentos. | **Registrar recebimento** |
| **Caixa diário** | Consultar o movimento do dia e fechar o caixa. | **Fechar caixa** |

### Regras Do Shell

- **Vendas** é a entrada para escolher **Venda à vista** ou **Venda a prazo**.
- A busca de produtos aceita **Código ou descrição** e deve aparecer no fluxo
  de qualquer nova venda.
- A área **Clientes** permite cadastrar clientes a qualquer momento, mesmo sem
  uma venda a prazo em execução.
- Ao escolher **Venda a prazo**, o funcionário deve selecionar **Cliente
  cadastrado** ou **Criar cliente** antes de continuar.
- A área **Caixa diário** mostra um único caixa por dia; abertura, sangria,
  suprimento e despesas não fazem parte do MVP.
- A navegação não deve ocultar validações ou confirmações pendentes de uma
  operação em andamento.
- Todas as telas devem usar textos em português e valores monetários no formato
  de reais, por exemplo `R$ 12,50`.

## Convenções De Interface

### Ações

| Intenção | Rótulo |
| --- | --- |
| Começar uma venda | **Nova venda** |
| Acrescentar produto | **Adicionar ao carrinho** |
| Alterar quantidade | **Quantidade** |
| Alterar preço praticado | **Preço praticado** |
| Avançar para pagamento | **Continuar para pagamento** |
| Confirmar operação | **Confirmar venda**, **Confirmar entrada**, **Confirmar ajuste** ou **Confirmar fechamento** |
| Abandonar uma operação | **Cancelar operação** |
| Corrigir dados | **Voltar e editar** |
| Cancelar uma venda já registrada | **Cancelar venda** |

### Mensagens

- Mensagens de erro devem dizer o que aconteceu e como corrigir, sem expor
  detalhes técnicos.
- Ações que alteram estoque, dívida ou caixa exigem uma confirmação antes do
  registro definitivo.
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

## Jornada 1: Venda À Vista

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
9. O sistema mostra um resumo e pede confirmação: **Confirmar venda**.
10. Após a confirmação, o sistema registra a venda, reduz o estoque, cria o
    recebimento imediato e inclui o valor no caixa do dia dentro da mesma
    operação.
11. A tela de sucesso mostra **Venda concluída** e o identificador da venda,
    com as ações **Nova venda** e **Ir para o caixa diário**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Carrinho inicial | Vazio | **Seu carrinho está vazio. Busque um produto para começar.** |
| Busca sem resultado | Vazio | **Nenhum produto encontrado. Confira o código ou tente outra descrição.** |
| Quantidade inválida | Validação | **Informe uma quantidade maior que zero.** |
| Estoque insuficiente | Validação | **Estoque insuficiente. Disponível: [quantidade].** O item não é adicionado acima do saldo disponível. |
| Produto sem preço | Validação | **Este produto não tem preço cadastrado. Atualize o cadastro antes de vender.** |
| Carrinho sem itens ao avançar | Validação | **Adicione pelo menos um produto para continuar.** |
| Forma não escolhida | Validação | **Escolha uma forma de pagamento.** |
| Resumo antes do registro | Confirmação | **Confirme a venda de [total] em [forma de pagamento].** |
| Falha no registro | Erro | **Não foi possível concluir a venda. Tente novamente.** O carrinho permanece disponível. |
| Registro concluído | Sucesso | **Venda concluída. Estoque e caixa foram atualizados.** |

## Jornada 2: Venda A Prazo

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
6. Para uma dívida única, informa **Vencimento**.
7. Para uma compra parcelada, informa **Número de parcelas** e os vencimentos.
   O sistema calcula os valores automaticamente e mostra **Valor da parcela**;
   o funcionário pode editar os valores antes de continuar.
8. O sistema mostra **Cliente**, itens, **Total da venda**, vencimento ou
   parcelas e **Total em aberto**.
9. O funcionário seleciona **Confirmar venda a prazo**.
10. Após a confirmação, o sistema registra a venda, reduz o estoque e cria a
    dívida e suas parcelas. Não é criado recebimento imediato.
11. A tela de sucesso mostra **Venda a prazo concluída**, o cliente, o total
    em aberto e a ação **Ver dívida do cliente**.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Opção de cliente não selecionada | Validação | **Escolha Cliente cadastrado ou Criar cliente para continuar.** |
| Cliente cadastrado sem resultados | Vazio | **Cliente não encontrado. Escolha Criar cliente ou tente outra busca.** |
| Cliente não selecionado | Validação | **Selecione um cliente para registrar uma venda a prazo.** |
| Nome ausente no cadastro | Validação | **Informe o nome do cliente.** |
| Número de parcelas inválido | Validação | **Informe pelo menos uma parcela.** |
| Vencimento ausente | Validação | **Informe o vencimento da dívida.** |
| Soma das parcelas diferente do total | Validação | **A soma das parcelas deve ser igual ao total da venda.** |
| Venda sem estoque suficiente | Validação | Usa a mesma mensagem de estoque da venda à vista e não conclui a operação. |
| Resumo de cliente e condições | Confirmação | **Confirme a venda a prazo de [total] para [cliente].** |
| Falha no registro | Erro | **Não foi possível registrar a venda a prazo. Tente novamente.** Os dados preenchidos são preservados. |
| Registro concluído | Sucesso | **Venda a prazo concluída. Dívida criada para [cliente].** |

## Jornada 3: Consultar Dívida E Registrar Pagamento

### Objetivo

Localizar as compras a prazo de um cliente, identificar a dívida correta e
registrar um pagamento total ou parcial.

### Fluxo principal

1. O funcionário acessa **Clientes** e pesquisa por **Nome ou telefone**.
2. Seleciona o cliente e visualiza **Compras a prazo**, **Parcelas**,
   **Pagamentos realizados** e **Total em aberto**.
3. Seleciona a compra que está sendo paga. Cada compra aparece separadamente
   com data, total, vencimento, valor pago e saldo.
4. Seleciona **Registrar recebimento** e informa **Valor recebido**.
5. O sistema mostra o saldo anterior, o valor informado e o saldo após o
   recebimento.
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
| Resumo do recebimento | Confirmação | **Confirme o recebimento de [valor] para a compra de [data].** |
| Falha no registro | Erro | **Não foi possível registrar o recebimento. Tente novamente.** |
| Pagamento registrado | Sucesso | **Recebimento registrado. Novo saldo em aberto: [valor].** |

## Jornada 4: Entrada De Estoque

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

## Jornada 5: Ajuste De Inventário

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

## Jornada 6: Cancelar Venda Não Paga

### Objetivo

Corrigir uma venda não paga sem apagar o histórico, restaurando as unidades
ao estoque e retirando a venda dos totais líquidos.

### Fluxo principal

1. O funcionário acessa **Vendas** e pesquisa pelo **Número da venda** ou
   período.
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

## Jornada 7: Fechar Caixa Diário

### Objetivo

Conferir o movimento do dia com os valores físicos contados e fechar o caixa
com uma senha específica.

### Fluxo principal

1. O funcionário acessa **Caixa diário** e escolhe a data atual.
2. O sistema mostra separadamente **Vendas à vista**, **Vendas a prazo** e
   **Recebimentos de clientes**.
3. Em **Vendas à vista**, mostra o total por forma de pagamento: **Dinheiro**,
   **Pix**, **Débito** e **Crédito**.
4. O sistema mostra **Total esperado** e permite informar os valores físicos
   contados: **Dinheiro contado**, **Pix conferido**, **Débito conferido** e
   **Crédito conferido**, quando aplicável.
5. O sistema calcula e mostra a **Diferença** entre o esperado e o contado.
6. O funcionário seleciona **Fechar caixa**.
7. O sistema mostra o resumo da conferência e pede a **Senha de fechamento**.
8. Com a senha correta, o funcionário confirma em **Confirmar fechamento**.
9. A tela de sucesso mostra **Caixa fechado**, data, totais e diferença
   registrada.

### Estados específicos

| Momento | Estado | Texto ou comportamento |
| --- | --- | --- |
| Dia sem movimento | Vazio | **Não há movimentações registradas neste dia.** O fechamento continua disponível. |
| Contagem ausente | Validação | **Informe os valores contados antes de fechar o caixa.** |
| Valor contado inválido | Validação | **Informe um valor igual ou maior que zero.** |
| Senha ausente | Validação | **Informe a senha de fechamento.** |
| Senha incorreta | Erro | **Senha de fechamento incorreta. O caixa não foi fechado.** |
| Caixa já fechado | Validação | **O caixa deste dia já está fechado.** |
| Resumo antes do fechamento | Confirmação | **Confirme o fechamento do caixa de [data]. Diferença: [valor].** |
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
