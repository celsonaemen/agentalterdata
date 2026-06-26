# Caso 001 - Divergencia Fiscal x Contabil por CFOP

## Data do registro

2026-06-26

## Modulo

Fiscal / Contabil / Integracao Fiscal x Contabil

## Empresa

Cliente A

## Competencia

2025

## Sintoma

Os valores dos relatorios fiscais nao batiam com os lancamentos contabeis gerados pela integracao. A diferenca apareceu apos a exportacao do Fiscal para o Contabil.

## Causa

Uma nota com natureza de transferencia foi tratada com CFOP/codigo de operacao de venda. Com isso, o Fiscal aplicou parametrizacao contabil de venda para uma operacao que deveria receber tratamento de transferencia.

## Impacto

- Lancamento contabil errado.
- Conta contabil errada.
- Historico contabil errado.
- Valor divergente entre Fiscal e Contabil.
- Possivel classificacao indevida como receita.
- Possivel reflexo indevido em impostos ou relatorios gerenciais.

## Diagnostico rapido

1. Comparar o total do relatorio fiscal com o total integrado no Contabil.
2. Isolar a diferenca por competencia.
3. Separar as notas por CFOP.
4. Identificar notas de transferencia tratadas como venda.
5. Conferir codigo de operacao e lancamento automatico.
6. Localizar o lote contabil gerado.
7. Confirmar se a conta e o historico indicam venda indevida.

## Correcao

1. Corrigir a classificacao fiscal da nota conforme procedimento interno.
2. Revisar CFOP dos itens e codigo de operacao.
3. Conferir impostos e totais da nota.
4. Ajustar a parametrizacao contabil, se a causa estiver no vinculo da operacao.
5. Tratar o lote contabil incorreto conforme politica do escritorio.
6. Reintegrar ou reexportar o movimento corrigido.

## Como validar no relatorio fiscal

- Conferir relatorio fiscal da competencia.
- Validar se a nota aparece com a natureza correta.
- Separar total por CFOP.
- Verificar se a transferencia nao esta compondo total de venda.
- Revisar impostos vinculados ao movimento.

## Como validar no lote contabil

- Abrir o lote gerado pela integracao.
- Conferir debito e credito.
- Conferir conta contabil usada.
- Conferir historico.
- Conferir valor da nota.
- Comparar com o relatorio fiscal corrigido.
- Conferir o razao das contas afetadas.

## Como evitar recorrencia

- Conferir CFOP antes de exportar a competencia.
- Criar checklist para notas de transferencia.
- Revisar codigos de operacao usados na importacao.
- Separar lancamentos automaticos de venda e transferencia.
- Evitar ajustar apenas o Contabil quando a origem do erro esta no Fiscal.
- Registrar casos semelhantes para comparacao futura.

## Links relacionados

- [Caso detalhado por CFOP](../cfop/caso-001-cfop-venda-em-transferencia.md)
- [Procedimento: CFOP de venda x CFOP de transferencia](../../docs/fiscal/cfop-venda-transferencia.md)
- [Troubleshooting da Integracao Fiscal x Contabil](../../docs/integracao-fiscal-contabil/troubleshooting.md)
