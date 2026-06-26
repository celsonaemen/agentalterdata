# CFOP de venda x CFOP de transferencia

Este procedimento orienta a conferencia operacional quando uma nota pode ter sido classificada como venda ou transferencia de forma incorreta no Fiscal.

Nao use este material como tabela legal de CFOP. A finalidade aqui e orientar a conferencia interna no Alterdata antes da integracao com o Contabil.

## Diferenca operacional entre venda e transferencia

Venda normalmente representa uma operacao com cliente, receita e reflexos comerciais, fiscais e contabeis ligados a faturamento.

Transferencia normalmente representa movimentacao entre estabelecimentos, unidades ou estoques, conforme a operacao real da empresa. O tratamento contabil tende a ser diferente de venda, porque nao deve ser confundido automaticamente com receita de venda.

Antes de corrigir, confirme a natureza real da operacao no documento e no procedimento fiscal do escritorio.

## Por que o CFOP influencia a integracao contabil

O CFOP ajuda o Fiscal a entender a natureza da operacao. No Alterdata, essa informacao se relaciona com codigo de operacao, parametrizacao contabil e lancamento automatico.

Quando o CFOP/codigo de operacao esta errado, a integracao pode levar o movimento para:

- Conta contabil errada.
- Historico errado.
- Tratamento de receita indevido.
- Imposto ou acumulador incorreto.
- Lote contabil divergente.

## Riscos de classificar transferencia como venda

- Gerar receita indevida no Contabil.
- Jogar valor em cliente a receber quando nao deveria.
- Levar imposto ou apuracao para rotina inadequada.
- Distorcer relatorios fiscais e contabeis.
- Causar divergencia na integracao Fiscal x Contabil.

## Riscos de classificar venda como transferencia

- Deixar de reconhecer receita quando a operacao era venda.
- Gerar conta contabil de transferencia indevida.
- Omitir reflexos de faturamento nos relatorios.
- Prejudicar conciliacao e fechamento.
- Causar diferenca entre fiscal, contabil e controles internos.

## Pontos de conferencia no Alterdata

- Nota fiscal escriturada.
- CFOP de cada item.
- Codigo de operacao.
- Cliente, fornecedor ou estabelecimento relacionado.
- Natureza da operacao.
- Impostos vinculados.
- Parametrizacao contabil.
- Lancamento automatico.
- Lote gerado no Contabil.

## Relacao com codigo de operacao

O codigo de operacao ajuda a direcionar a rotina fiscal e contabil. Mesmo que o CFOP pareca correto, um codigo de operacao errado pode puxar parametrizacao de venda para uma transferencia, ou parametrizacao de transferencia para uma venda.

Ao corrigir uma divergencia, confira CFOP e codigo de operacao juntos.

## Relacao com lancamento automatico

O lancamento automatico define debito, credito e historico que serao gerados no Contabil. Se uma transferencia usa lancamento automatico de venda, o Contabil pode receber receita, cliente ou historico de venda indevidamente.

Mantenha lancamentos automaticos separados por natureza de operacao sempre que isso reduzir risco de erro.

## Relacao com relatorios fiscais

Relatorios fiscais podem agrupar valores por CFOP, tipo de operacao, imposto ou acumulador. Se uma transferencia entra como venda, os totais de venda podem ficar maiores que o correto e a conferencia com o Contabil fica distorcida.

Antes de exportar, confira totais por CFOP na competencia.

## Relacao com Contabil

No Contabil, o erro aparece em lote, razao, balancete ou relatorio de conferencia. O sintoma comum e o valor fiscal nao bater com o valor contabil, ou o lancamento cair em conta incompativel com a natureza real da nota.

Corrija a origem no Fiscal antes de ajustar manualmente o Contabil. Ajuste manual sem corrigir a origem tende a repetir o erro na proxima exportacao.

## Checklist operacional

- A nota e venda ou transferencia?
- O CFOP dos itens representa a operacao real?
- Ha mais de um CFOP na nota?
- O codigo de operacao acompanha a natureza correta?
- O lancamento automatico e de venda ou transferencia?
- Os impostos foram revisados?
- O relatorio fiscal da competencia foi conferido?
- O lote contabil gerado bate com o Fiscal?
- A conta contabil representa a operacao correta?
