# Caso 001 - CFOP de venda usado em operacao de transferencia

## Data do registro

2026-06-26

## Modulo

Fiscal / Contabil / Integracao Fiscal x Contabil

## Empresa

Cliente A

## Competencia

2025

## Problema

Foi identificada uma nota fiscal cuja operacao real era transferencia, mas que no Fiscal estava sendo tratada com CFOP/codigo de operacao de venda. Exemplo operacional: uso de CFOP de venda, como `6102`, quando a operacao deveria seguir tratamento de transferencia, como `6152`, conforme a natureza real da nota.

Essa classificacao incorreta pode fazer o Fiscal gerar valores, contas contabeis, historicos e impostos incompativeis com a operacao real, causando divergencia entre os totais fiscais e os lancamentos contabeis apos a integracao.

## Sintoma identificado

- Valor do Fiscal nao bate com o Contabil apos a integracao.
- Nota aparece em relatorio fiscal como venda, mas a operacao era transferencia.
- Lote contabil gerado com conta de receita, cliente ou imposto que nao corresponde a transferencia.
- Historico contabil indica venda ou receita quando deveria representar transferencia.
- Diferenca aparece ao comparar relatorios fiscais com lote, razao ou balancete.

## Diagnostico

O diagnostico deve comecar pela nota fiscal e nao pelo lote contabil. O lote e consequencia da classificacao fiscal e da parametrizacao vinculada.

Verifique:

- Natureza real da operacao.
- CFOP informado nos itens da nota.
- Codigo de operacao usado no Fiscal.
- Lancamento automatico vinculado ao CFOP/codigo de operacao.
- Parametrizacao contabil da operacao.
- Lote gerado no Contabil.

Se a nota e de transferencia, mas entrou no Fiscal como venda, a integracao pode gerar contabilizacao de venda indevida.

## Causa provavel

CFOP ou codigo de operacao parametrizado com natureza de venda para uma nota cuja operacao real era transferencia.

Isso pode ocorrer por:

- Importacao do XML com classificacao nao revisada.
- Codigo de operacao selecionado incorretamente.
- CFOP de item mantido como venda.
- Parametrizacao contabil vinculada ao CFOP de venda.
- Lancamento automatico de venda aplicado a movimento de transferencia.

## Onde verificar no Alterdata

- `Fiscal > Movimento de Notas`
- Conferencia da NF.
- CFOP dos itens.
- Codigo de operacao.
- Parametrizacao contabil vinculada ao CFOP/operacao.
- Integracao Fiscal x Contabil.
- Lote gerado no Contabil.

## Correcao no Fiscal

1. Conferir o XML/NF original sem anexar ou salvar o arquivo no repositorio.
2. Identificar a natureza correta da operacao.
3. Conferir CFOP de cada item da nota.
4. Corrigir CFOP/codigo de operacao, quando permitido e conforme procedimento do escritorio.
5. Revisar o total da nota apos a correcao.
6. Revisar impostos vinculados a operacao.
7. Conferir se o lancamento automatico vinculado corresponde a transferencia.
8. Reprocessar ou reexportar a integracao, quando necessario.

## Correcao no Contabil

1. Localizar o lote gerado pela integracao.
2. Conferir os lancamentos criados.
3. Identificar contas, historicos, debitos, creditos e valores gerados indevidamente.
4. Excluir ou estornar o lote incorreto, conforme politica do escritorio.
5. Reimportar ou reintegrar apos a correcao no Fiscal.
6. Conferir debito, credito, historico e valor.
7. Validar se o novo lancamento representa transferencia, e nao venda.

## Conferencia apos correcao

- Relatorio fiscal da competencia.
- Nota fiscal corrigida no Fiscal.
- CFOP dos itens.
- Codigo de operacao.
- Parametrizacao contabil usada na integracao.
- Lote novo ou ajustado no Contabil.
- Razao das contas afetadas.
- Balancete, quando aplicavel.

## Resultado esperado

- Fiscal e Contabil passam a bater para a competencia analisada.
- Nota deixa de gerar tratamento contabil de venda indevida.
- Lote contabil passa a refletir a natureza real de transferencia.
- Contas, historicos e valores ficam consistentes com a operacao.

## Prevencao

- Conferir CFOP antes da integracao mensal.
- Revisar notas de transferencia, venda, remessa, devolucao e bonificacao.
- Em notas com mais de um CFOP, conferir item por item.
- Validar codigo de operacao antes de exportar para o Contabil.
- Manter lancamentos automaticos separados por natureza de operacao.
- Registrar casos recorrentes para treinamento interno.

## Checklist final

- A empresa esta correta?
- A competencia e 2025?
- A nota pertence ao Cliente A?
- A natureza real da operacao foi confirmada?
- O CFOP dos itens foi revisado?
- O codigo de operacao foi conferido?
- A parametrizacao contabil esta vinculada a transferencia?
- O lote incorreto foi tratado conforme politica do escritorio?
- A integracao foi reprocessada ou reexportada quando necessario?
- O novo lote fecha debito e credito?
- O valor do Fiscal bate com o Contabil?

## Links relacionados

- [Procedimento: CFOP de venda x CFOP de transferencia](../../docs/fiscal/cfop-venda-transferencia.md)
- [Troubleshooting da Integracao Fiscal x Contabil](../../docs/integracao-fiscal-contabil/troubleshooting.md)
