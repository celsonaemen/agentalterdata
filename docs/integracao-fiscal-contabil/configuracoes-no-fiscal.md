# Configuracoes no Fiscal para Integracao Contabil

A configuracao principal da Integracao Fiscal x Contabil fica no cadastro da empresa no Fiscal. Essa tela define se os movimentos fiscais da empresa podem gerar lancamentos para o Contabil.

## Caminho no Alterdata

`Fiscal > Cadastro > Empresas > abrir empresa > Geral > Integracao`

Quando a empresa deve integrar com o Contabil, marque a opcao `Integra com a Contabilidade`, quando aplicavel a rotina da empresa.

Essa configuracao permite vincular lancamentos automaticos as notas fiscais e preparar os movimentos para exportacao contabil.

## Checklist de configuracao

- Empresa correta.
- Plano de contas correto.
- Integracao habilitada.
- Lancamentos automaticos vinculados.
- Clientes e fornecedores conferidos.
- Codigo de operacao revisado.
- CFOP revisado.

## Quando revisar essa tela

- Ao cadastrar uma empresa nova.
- Ao iniciar a integracao de uma empresa que antes era lancada manualmente.
- Quando o Fiscal nao gera lote no Contabil.
- Quando notas aparecem no Fiscal, mas nao aparecem na exportacao.
- Quando houve troca de plano de contas ou alteracao de parametrizacao contabil.
- Quando uma empresa foi copiada de outra e pode ter herdado configuracoes incorretas.
- Antes do primeiro fechamento fiscal e contabil da empresa.

## Erros comuns

- Integracao desmarcada no cadastro da empresa.
- Empresa aberta no Fiscal diferente da empresa do Contabil.
- Plano de contas incorreto para a empresa.
- Lancamento automatico nao vinculado ao movimento fiscal.
- Codigo de operacao sem parametrizacao contabil.
- CFOP usado de forma incorreta para a operacao.
- Cliente ou fornecedor sem vinculacao contabil quando a rotina exige conta especifica.

## Impacto no Contabil

Se essa configuracao estiver incorreta, o Contabil pode receber lancamentos incompletos, em conta errada ou nao receber nenhum lote. Tambem pode ocorrer diferenca entre debito e credito, ausencia de historico, duplicidade de lancamentos ou divergencia entre relatorios fiscais e contabeis.

Antes de corrigir diretamente no Contabil, confirme se a origem do erro esta no Fiscal. Corrigir apenas o lote contabil pode esconder a causa e permitir que o erro volte na proxima exportacao.
