# Vinculacao Contabil de Clientes e Fornecedores

A vinculacao contabil relaciona clientes e fornecedores as contas contabeis corretas. Ela e usada para que os movimentos fiscais gerem lancamentos no Contabil com a conta adequada para cada pessoa, empresa ou grupo.

## Caminho no Alterdata

`Fiscal > aba Contabil > Vinculacao Contabil`

Pode existir vinculacao para entrada, saida ou ambos, conforme a rotina da empresa e o tipo de movimento.

## Uso pratico

- Fornecedores vinculados a fornecedores a pagar.
- Clientes vinculados a clientes a receber.
- Contas especificas por cliente ou fornecedor, quando a empresa precisa controlar individualmente.
- Contas genericas por grupo, quando o controle individual nao e necessario.

## Quando usar conta individual

Use conta individual quando a empresa precisa controlar saldo por cliente ou fornecedor no razao ou na conciliacao.

Exemplos:

- Fornecedor com volume relevante.
- Cliente recorrente com saldo a receber acompanhado pela contabilidade.
- Necessidade de conciliar duplicatas, pagamentos ou recebimentos por pessoa.
- Exigencia interna de demonstrar saldo individualizado.

## Quando usar conta generica

Use conta generica quando o controle individual nao for necessario ou quando a empresa trabalha com lancamento consolidado.

Exemplos:

- Fornecedores eventuais de baixo valor.
- Clientes sem controle individual no Contabil.
- Rotinas em que o controle detalhado fica em outro sistema.
- Empresas que conciliam apenas contas resumidas.

## Impacto na conciliacao

A vinculacao incorreta pode jogar valores em conta errada e prejudicar a conciliacao. Isso aparece no razao, balancete, relatorios de contas a pagar, contas a receber e no fechamento do periodo.

Quando cliente ou fornecedor cai em conta errada, confira primeiro a vinculacao contabil antes de ajustar manualmente o lancamento. Se o erro estiver na origem, ele tende a repetir nas proximas integracoes.

## Erros comuns

- Cliente sem conta contabil vinculada.
- Fornecedor sem conta contabil vinculada.
- Vinculacao feita apenas para entrada, mas o erro ocorre na saida.
- Vinculacao feita apenas para saida, mas o erro ocorre na entrada.
- Conta generica usada quando deveria haver conta individual.
- Conta individual duplicada ou vinculada ao cadastro errado.
- Alteracao no cadastro fiscal sem revisao da vinculacao contabil.

## Checklist de conferencia

- O cadastro do cliente ou fornecedor esta correto?
- A vinculacao e de entrada, saida ou ambos?
- A conta contabil pertence ao plano de contas da empresa?
- A conta esta ativa?
- A natureza da conta esta correta?
- A rotina pede conta individual ou generica?
- O lancamento automatico esta buscando a vinculacao correta?
- O razao da conta bate com os movimentos fiscais?
