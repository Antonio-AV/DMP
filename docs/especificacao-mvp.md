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

1. Como funcionário, quero acessar o sistema com uma senha geral, para que apenas pessoas autorizadas usem a aplicação.

2. Como funcionário, quero localizar produtos pelo código, para que consiga adicioná-los rapidamente à venda.

3. Como funcionário, quero localizar produtos pela descrição, para que consiga encontrar itens sem lembrar seus códigos.

4. Como funcionário, quero informar a quantidade de um produto, para que registre múltiplas unidades corretamente.

5. Como funcionário, quero que produtos repetidos sejam agrupados, para que o carrinho permaneça organizado.

6. Como funcionário, quero visualizar o preço cadastrado do produto, para que possa conferi-lo antes de finalizar.

7. Como funcionário, quero alterar o preço de um item durante a venda, para que possa aplicar negociações específicas.

8. Como funcionário, quero que o preço praticado seja preservado na venda, para que alterações futuras não modifiquem o histórico.

9. Como funcionário, quero visualizar todos os itens e o total da venda, para que possa corrigir erros antes da confirmação.

10. Como funcionário, quero finalizar uma venda à vista, para que o estoque e o caixa sejam atualizados.

11. Como funcionário, quero registrar dinheiro, Pix, débito ou crédito, para que o recebimento seja classificado.

12. Como funcionário, quero que uma venda use uma única forma de pagamento no MVP, para que o fluxo inicial permaneça simples.

13. Como funcionário, quero finalizar uma venda a prazo, para que o valor seja associado ao débito de um cliente.

14. Como funcionário, quero cadastrar um cliente a qualquer momento, inclusive antes de uma venda a prazo, para que possa manter o cadastro de clientes atualizado.

15. Como funcionário, quero visualizar cada compra a prazo separadamente, para que saiba a origem de cada débito.

16. Como funcionário, quero registrar uma compra a prazo sem parcelas, para que ela tenha apenas um vencimento.

17. Como funcionário, quero dividir uma compra a prazo em parcelas, para que possa representar acordos parcelados.

18. Como funcionário, quero definir vencimentos para a dívida ou para as parcelas, para que possa acompanhar quando os valores devem ser pagos.

19. Como funcionário, quero calcular parcelas automaticamente, para que o preenchimento seja rápido.

20. Como funcionário, quero editar os valores das parcelas, para que possa representar acordos personalizados.

21. Como funcionário, quero registrar pagamentos parciais, para que o saldo restante seja atualizado.

22. Como funcionário, quero selecionar a compra que está sendo paga, para que o recebimento seja associado ao débito correto.

23. Como funcionário, quero visualizar o total devido por cliente, para que saiba quanto ainda está em aberto.

24. Como funcionário, quero visualizar os recebimentos de clientes, para que possa conferir os valores recebidos no dia.

25. Como funcionário, quero que o estoque seja reduzido ao finalizar uma venda, para que o saldo represente a quantidade disponível.

26. Como funcionário, quero que o sistema bloqueie vendas acima do estoque, para que não sejam criados saldos negativos.

27. Como funcionário, quero registrar entradas manuais de estoque, para que possa adicionar produtos recebidos.

28. Como funcionário, quero registrar ajustes de inventário, para que possa corrigir divergências.

29. Como funcionário, quero visualizar o histórico de movimentações, para que as alterações no estoque sejam explicáveis.

30. Como funcionário, quero cancelar uma venda não paga, para que erros possam ser corrigidos.

31. Como funcionário, quero que o cancelamento restaure o estoque, para que o saldo permaneça correto.

32. Como funcionário, quero que vendas canceladas permaneçam no histórico, para que operações não sejam apagadas.

33. Como funcionário, quero que vendas canceladas não entrem nos totais líquidos, para que os valores sejam confiáveis.

34. Como funcionário, quero cadastrar um fornecedor, para que seus produtos possam ser relacionados a ele.

35. Como funcionário, quero definir o fornecedor principal de um produto, para que saiba de quem normalmente compro o item.

36. Como funcionário, quero adicionar fornecedores alternativos, para que possa consultar outras opções de compra.

37. Como funcionário, quero consultar os produtos de um fornecedor, para que possa planejar reposições.

38. Como funcionário, quero associar uma entrada de estoque a um fornecedor, para que o histórico de reposição seja rastreável.

39. Como funcionário, quero abrir o caixa diário, para que as operações do dia sejam agrupadas.

40. Como funcionário, quero visualizar vendas à vista, vendas a prazo e recebimentos separadamente, para que entenda o movimento do dia.

41. Como funcionário, quero visualizar o total por forma de pagamento, para que possa conferir dinheiro, Pix e cartões.

42. Como funcionário, quero informar os valores físicos contados no fechamento, para que possa comparar o esperado com o recebido.

43. Como funcionário, quero fechar o caixa com uma senha específica, para que o fechamento não aconteça acidentalmente.

44. Como funcionário, quero que todos os funcionários tenham acesso às mesmas operações, para que o MVP não dependa de gerenciamento individual de usuários.

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
- O banco terá migrações versionadas para permitir evolução do esquema.
- As entidades principais serão `Produto`, `Fornecedor`, `ProdutoFornecedor`, `Venda`, `ItemVenda`, `Cliente`, `Parcela`, `Recebimento`, `CaixaDiario` e `MovimentoEstoque`.
- Uma venda terá os estados `aberta`, `finalizada` ou `cancelada`.
- Cada item guardará o preço praticado no momento da venda.
- Produtos repetidos serão agrupados pela soma da quantidade.
- Uma venda finalizada reduzirá o estoque dentro da mesma transação.
- O sistema bloqueará vendas que resultem em estoque negativo.
- Cada venda à vista criará um recebimento imediato.
- Cada venda a prazo criará uma dívida associada a um cliente.
- Uma venda a prazo poderá ter uma dívida única ou várias parcelas.
- Toda dívida terá vencimento. Vendas parceladas terão vencimento por parcela.
- Parcelas poderão ser calculadas automaticamente ou editadas manualmente.
- Pagamentos parciais serão permitidos.
- O pagamento será associado à compra a prazo selecionada pelo funcionário.
- Uma venda à vista usará apenas uma forma de pagamento no MVP.
- As formas de pagamento previstas são dinheiro, Pix, débito e crédito.
- Todo movimento de estoque será persistido.
- Os movimentos previstos são entrada, venda, cancelamento e ajuste.
- O cancelamento manterá a venda no histórico e criará o movimento de estorno do estoque.
- O MVP permitirá cancelar somente vendas ainda não pagas.
- Um fornecedor poderá fornecer vários produtos.
- Cada produto terá um fornecedor principal e poderá ter fornecedores alternativos.
- A relação entre produto e fornecedor será persistida separadamente para suportar essa cardinalidade.
- Fornecedores referenciados por históricos não serão apagados fisicamente; serão arquivados.
- Uma entrada manual de estoque poderá identificar o fornecedor.
- O cadastro de fornecedores e suas relações com produtos fará parte do MVP.
- Pedidos de compra, cotações e relatórios avançados de fornecedores ficarão fora do MVP.
- Haverá um caixa por dia.
- O caixa consolidará vendas e recebimentos.
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
- O histórico deverá registrar entradas, ajustes, vendas e cancelamentos.
- O cadastro de fornecedor deverá verificar fornecedor principal e fornecedores alternativos.
- O cancelamento deverá marcar a venda, restaurar o estoque e excluir a venda dos totais líquidos.
- O caixa deverá separar vendas à vista, vendas a prazo, recebimentos e formas de pagamento.
- O fechamento deverá exigir a senha correta.
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
