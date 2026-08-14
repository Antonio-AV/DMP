# Especificação do MVP de Gestão da Papelaria

## Problema

A papelaria dos pais utiliza um sistema antigo, offline e limitado. Os quatro
funcionários trabalham no mesmo computador, sem usuários individuais.

O sistema atual permite cadastrar produtos por código, realizar vendas à vista
ou a prazo e associar débitos a clientes, mas não oferece uma experiência
moderna nem uma visão integrada de estoque, recebimentos, caixa diário e
fornecedores.

## Solução

Criar uma aplicação web local para Windows, executada com Streamlit e acessada
pelo navegador em `localhost`.

A primeira versão será um MVP demonstrativo, com dados simulados, capaz de
realizar:

- Cadastro e consulta de produtos.
- Cadastro de fornecedores.
- Associação de fornecedores principais e alternativos aos produtos.
- Vendas à vista e a prazo.
- Controle automático de estoque.
- Clientes com compras a prazo, parcelas e saldo.
- Registro de recebimentos.
- Caixa diário.
- Cancelamento de vendas ainda não pagas.
- Histórico de movimentações de estoque.

A aplicação não dependerá de internet nem de servidor externo.

## Histórias de Usuário

1. Como funcionário, quero cadastrar e editar um produto com código, descrição, preço e estoque inicial, para que seus dados permaneçam atualizados sem alterar o histórico de estoque.

2. Como funcionário, quero acessar o sistema com uma senha geral, para que apenas pessoas autorizadas usem a aplicação.

3. Como funcionário, quero localizar produtos pelo código, para que consiga adicioná-los rapidamente à venda.

4. Como funcionário, quero localizar produtos pela descrição, para que consiga encontrar itens sem lembrar seus códigos.

5. Como funcionário, quero informar a quantidade de um produto, para que registre múltiplas unidades corretamente.

6. Como funcionário, quero que produtos repetidos sejam agrupados, para que o carrinho permaneça organizado.

7. Como funcionário, quero visualizar o preço cadastrado do produto, para que possa conferi-lo antes de finalizar.

8. Como funcionário, quero alterar o preço de um item durante a venda, para que possa aplicar negociações específicas.

9. Como funcionário, quero que o preço praticado seja preservado na venda, para que alterações futuras não modifiquem o histórico.

10. Como funcionário, quero visualizar todos os itens e o total da venda, para que possa corrigir erros antes da confirmação.

11. Como funcionário, quero finalizar uma venda à vista, para que o estoque e o caixa sejam atualizados.

12. Como funcionário, quero registrar a data e hora de finalização de cada venda, para que o histórico registre quando a operação foi concluída.

13. Como funcionário, quero pesquisar vendas pelo número ou por uma data e hora de finalização, para que consiga localizar todas as vendas daquela hora.

14. Como funcionário, quero registrar dinheiro, Pix, débito ou crédito, para que o recebimento seja classificado.

15. Como funcionário, quero que uma venda use uma única forma de pagamento no MVP, para que o fluxo inicial permaneça simples.

16. Como funcionário, quero finalizar uma venda a prazo, para que o valor seja associado ao débito de um cliente.

17. Como funcionário, quero cadastrar um cliente a qualquer momento, inclusive antes de uma venda a prazo, para que possa manter o cadastro de clientes atualizado.

18. Como funcionário, quero visualizar cada compra a prazo separadamente, para que saiba a origem de cada débito.

19. Como funcionário, quero registrar uma compra a prazo sem parcelas, para que ela tenha apenas um vencimento.

20. Como funcionário, quero dividir uma compra a prazo em parcelas, para que possa representar acordos parcelados.

21. Como funcionário, quero definir vencimentos para a dívida ou para as parcelas, para que possa acompanhar quando os valores devem ser pagos.

22. Como funcionário, quero calcular parcelas automaticamente, para que o preenchimento seja rápido.

23. Como funcionário, quero editar os valores das parcelas, para que possa representar acordos personalizados.

24. Como funcionário, quero registrar pagamentos parciais, para que o saldo restante seja atualizado.

25. Como funcionário, quero selecionar a compra que está sendo paga, para que o recebimento seja associado ao débito correto.

26. Como funcionário, quero visualizar o total devido por cliente, para que saiba quanto ainda está em aberto.

27. Como funcionário, quero visualizar os recebimentos de clientes, para que possa conferir os valores recebidos no dia.

28. Como funcionário, quero que o estoque seja reduzido ao finalizar uma venda, para que o saldo represente a quantidade disponível.

29. Como funcionário, quero que o sistema bloqueie vendas acima do estoque, para que não sejam criados saldos negativos.

30. Como funcionário, quero registrar entradas manuais de estoque, para que possa adicionar produtos recebidos.

31. Como funcionário, quero registrar ajustes de inventário, para que possa corrigir divergências.

32. Como funcionário, quero visualizar o histórico de movimentações, para que as alterações no estoque sejam explicáveis.

33. Como funcionário, quero cancelar uma venda não paga, para que erros possam ser corrigidos.

34. Como funcionário, quero que o cancelamento restaure o estoque, para que o saldo permaneça correto.

35. Como funcionário, quero que vendas canceladas permaneçam no histórico, para que operações não sejam apagadas.

36. Como funcionário, quero que vendas canceladas não entrem nos totais líquidos, para que os valores sejam confiáveis.

37. Como funcionário, quero cadastrar um fornecedor, para que seus produtos possam ser relacionados a ele.

38. Como funcionário, quero definir o fornecedor principal de um produto, para que saiba de quem normalmente compro o item.

39. Como funcionário, quero adicionar fornecedores alternativos, para que possa consultar outras opções de compra.

40. Como funcionário, quero consultar os produtos de um fornecedor, para que possa planejar reposições.

41. Como funcionário, quero associar uma entrada de estoque a um fornecedor, para que o histórico de reposição seja rastreável.

42. Como funcionário, quero acessar o caixa diário, para que as operações do dia sejam agrupadas automaticamente.

43. Como funcionário, quero visualizar vendas à vista, vendas a prazo e recebimentos separadamente, para que entenda o movimento do dia.

44. Como funcionário, quero visualizar o total por forma de pagamento, para que possa conferir dinheiro, Pix e cartões.

45. Como funcionário, quero informar os valores físicos contados no fechamento, para que possa comparar o esperado com o recebido.

46. Como funcionário, quero fechar o caixa com uma senha específica, para que o fechamento não aconteça acidentalmente.

47. Como funcionário, quero que todos os funcionários tenham acesso às mesmas operações, para que o MVP não dependa de gerenciamento individual de usuários.

## Decisões de Implementação

- A aplicação será desenvolvida em Python.
- A interface será construída com Streamlit.
- O Streamlit será executado localmente e acessado pelo navegador via `localhost`.
- A aplicação não dependerá de internet ou serviços externos.
- O banco de dados será SQLite, acessado pela biblioteca padrão `sqlite3`.
- O sistema será empacotado para Windows utilizando PyInstaller.
- O pacote de instalação deverá incluir o runtime necessário, as dependências e os arquivos estáticos.
- Um atalho deverá iniciar o servidor local e abrir o navegador automaticamente.
- O domínio será separado da interface Streamlit.
- Os casos de uso serão o principal ponto de entrada da aplicação.
- O domínio não dependerá diretamente de componentes Streamlit.
- O MVP será um monólito modular, sem API remota ou backend separado.
- O estado da sessão do Streamlit será usado apenas para estado transitório, como o carrinho ativo.
- O estado persistido do negócio pertencerá ao SQLite.
- Valores monetários serão armazenados em centavos inteiros.
- Preços, valores de parcelas e pagamentos informados devem ser maiores que zero;
  valores negativos não são permitidos.
- O banco terá migrações versionadas para permitir evolução do esquema.
- As entidades principais serão `Produto`, `Fornecedor`, `ProdutoFornecedor`, `Venda`, `ItemVenda`, `Cliente`, `Parcela`, `Recebimento`, `CaixaDiario` e `MovimentoEstoque`.
- Uma venda terá os estados `aberta`, `finalizada` ou `cancelada`.
- Uma venda finalizada armazenará a data e hora local em que foi confirmada.
- A data e hora de finalização permanecerá no histórico mesmo se a venda for cancelada depois.
- A pesquisa de vendas poderá usar o número da venda ou uma data e hora
  selecionadas; a hora selecionada buscará os minutos `00` a `59`, com todos os
  segundos, no mesmo dia.
- Cada item guardará o preço praticado no momento da venda.
- Produtos repetidos serão agrupados pela soma da quantidade.
- Antes de finalizar uma venda, o sistema revalidará o estoque de todos os itens
  do carrinho, inclusive após alterações de quantidade.
- Uma venda finalizada reduzirá o estoque dentro da mesma transação.
- O sistema bloqueará vendas que resultem em estoque negativo.
- A edição dos dados cadastrais de um produto não alterará seu estoque; mudanças
  de estoque serão feitas por entradas ou ajustes.
- O cadastro de produto permitirá informar um estoque inicial inteiro maior ou igual a zero.
- O estoque inicial será registrado como uma entrada no histórico de movimentações,
  inclusive quando for zero.
- As demais movimentações de estoque exigirão quantidade positiva; ajuste sem
  diferença não criará movimentação.
- Cada venda à vista criará um recebimento imediato.
- Cada venda a prazo criará uma dívida associada a um cliente.
- Uma venda a prazo iniciará com uma dívida única, um vencimento padrão e o
  seletor de parcelas definido como `1`.
- O funcionário poderá informar um número de parcelas maior ou igual a um;
  uma parcela mantém a dívida única e duas ou mais criam o parcelamento.
- Quando o número for `1`, nenhuma entidade `Parcela` separada será persistida;
  a dívida armazenará o valor total e seu vencimento.
- Toda dívida terá vencimento. Vendas parceladas terão vencimento por parcela.
- Toda parcela deverá ter um vencimento informado; a venda parcelada não poderá
  ser confirmada enquanto houver uma parcela sem vencimento.
- Ao informar o número de parcelas, o sistema calculará automaticamente os
  valores em centavos e os vencimentos mensais a partir da data da venda.
- Os centavos restantes da divisão serão distribuídos entre as primeiras
  parcelas para que a soma seja exatamente igual ao total.
- O funcionário poderá editar o valor e o vencimento de cada parcela antes da
  confirmação.
- O número de parcelas não poderá ser maior que o total da venda em centavos.
- Pagamentos parciais serão permitidos.
- O pagamento será associado à compra a prazo selecionada pelo funcionário.
- Em uma compra com dívida única, o pagamento reduzirá diretamente o saldo
  da dívida.
- Em uma compra parcelada, o pagamento será aplicado primeiro à parcela mais
  antiga em aberto e seguirá para as próximas se houver valor excedente.
- Uma venda à vista usará apenas uma forma de pagamento no MVP.
- As formas de pagamento previstas são dinheiro, Pix, débito e crédito.
- Todo movimento de estoque será persistido.
- Os movimentos previstos são entrada, venda, cancelamento e ajuste.
- O cancelamento manterá a venda no histórico e criará o movimento de estorno do estoque.
- O MVP permitirá cancelar somente vendas ainda não pagas.
- Um fornecedor poderá fornecer vários produtos.
- O cadastro de produto exigirá um fornecedor principal; fornecedores alternativos serão opcionais.
- O fornecedor principal não poderá ser repetido entre os fornecedores alternativos do mesmo produto.
- A relação entre produto e fornecedor será persistida separadamente para suportar essa cardinalidade.
- Fornecedores referenciados por históricos não serão apagados fisicamente; serão arquivados.
- Uma entrada manual de estoque poderá identificar o fornecedor.
- O cadastro de fornecedores e suas relações com produtos fará parte do MVP.
- Pedidos de compra, cotações e relatórios avançados de fornecedores ficarão fora do MVP.
- Haverá um caixa por dia.
- O registro do caixa diário será criado automaticamente no primeiro acesso do
  dia, com totais zerados e sem etapa de abertura.
- O caixa separará vendas à vista, vendas a prazo e recebimentos de débitos.
- O total recebido será a soma das vendas à vista e dos recebimentos de débitos;
  vendas a prazo não pagas não entrarão nesse total.
- A diferença do caixa será calculada como total contado menos total esperado;
  valor negativo representa falta e valor positivo representa sobra.
- O caixa não modelará inicialmente abertura, sangria, suprimentos ou despesas.
- O fechamento exigirá uma senha específica.
- Não haverá usuários individuais ou permissões diferenciadas.
- Os dados do MVP serão simulados ou cadastrados manualmente.
- Não haverá importação automática do sistema antigo.
- O empacotamento com PyInstaller deverá ser validado em um computador Windows limpo.
- Não serão assumidas integrações com impressora, leitor de código de barras ou gaveta de dinheiro.

## Decisões de Teste

- O seam principal será a camada de casos de uso, usando SQLite temporário.
- Os testes validarão comportamento observável, não detalhes internos.
- A finalização de uma venda à vista deverá verificar venda, recebimento, estoque e caixa.
- A finalização de uma venda a prazo deverá verificar cliente, dívida, parcelas e estoque.
- O pagamento parcial deverá atualizar recebimentos e saldo restante.
- O estoque deverá bloquear vendas acima da quantidade disponível.
- A finalização deverá revalidar o estoque depois de alterações no carrinho.
- O histórico deverá registrar entradas, ajustes, vendas e cancelamentos.
- O cadastro de fornecedor deverá verificar fornecedor principal e fornecedores alternativos.
- O cancelamento deverá marcar a venda, restaurar o estoque e excluir a venda dos totais líquidos.
- O caixa deverá separar vendas à vista, vendas a prazo, recebimentos de débitos,
  formas de pagamento e o total efetivamente recebido.
- O fechamento deverá exigir a senha correta.
- O fechamento deverá registrar corretamente falta, sobra ou ausência de diferença
  usando a fórmula total contado menos total esperado.
- O aplicativo empacotado deverá ser validado em ambiente Windows.
- O repositório ainda não possui testes anteriores; a suíte de casos de uso será a primeira convenção do projeto.
- Testes da interface Streamlit cobrirão apenas jornadas mínimas e sua integração com os casos de uso.

## Fora do Escopo

- IA para respostas ou análises.
- Migração automática do sistema antigo.
- Uso imediato em produção.
- Sincronização online.
- Múltiplos computadores ou caixas simultâneos.
- Usuários individuais e permissões por funcionário.
- Pagamentos divididos em múltiplas formas.
- Cancelamento de venda parcialmente paga.
- Pedidos de compra.
- Cotações de fornecedores.
- Relatórios avançados.
- Emissão fiscal ou impressão de comprovantes.
- Integração com leitor, impressora ou gaveta de dinheiro.
- Abertura de caixa, sangria, suprimentos e despesas.
- Rotina definitiva de backup.
- Regras fiscais e contábeis.

## Observações

- Este MVP é uma demonstração funcional com dados simulados, não uma substituição imediata do sistema atual.
- A operação real deverá ser validada com os responsáveis da papelaria antes da migração.
- As regras de cancelamento de vendas parcialmente pagas ainda precisam ser definidas antes de entrarem no produto.
