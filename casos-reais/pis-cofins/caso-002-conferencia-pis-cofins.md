# Caso 002 - Conferencia de PIS e COFINS para lancamento no Alterdata

## Data do registro

2026-06-26

## Modulo

Fiscal / Contabil / Integracao Fiscal x Contabil

## Empresa

Cliente A

## Competencia

Ano completo

## Problema

Necessidade de identificar mes a mes os valores de PIS e COFINS em relatorio fiscal para lancamento ou conferencia no Alterdata.

## Sintoma

Usuario precisa saber o saldo de PIS e COFINS do ano todo e verificar se existe ISS no relatorio.

## Diagnostico

Separar PIS, COFINS e ISS antes de concluir o saldo. Dentro de cada tributo, separar imposto proprio de retencao, conferir a competencia, somar os valores por mes e validar se os valores pertencem ao mesmo tipo de imposto.

O total anual deve ser resultado da soma mensal conferida. Nao use apenas um total consolidado sem validar as competencias.

## Onde verificar no Alterdata

- Relatorios fiscais.
- Apuracao de PIS/COFINS.
- Movimento de notas.
- Apuracao de ISS.
- Integracao Fiscal x Contabil.
- Lotes no Contabil.
- Razao das contas de tributos.

## Correcao/Procedimento

1. Extrair relatorio por competencia.
2. Identificar colunas de PIS, COFINS e ISS.
3. Separar valores proprios e retidos.
4. Totalizar por mes.
5. Conferir se as notas pertencem a competencia analisada.
6. Comparar os totais com a apuracao.
7. Conferir se existe lote contabil ja gerado.
8. Lancar ou ajustar no Contabil, se necessario e conforme politica do escritorio.
9. Documentar qualquer ajuste manual feito fora da integracao.

## Conferencia

- Total anual de PIS.
- Total anual de COFINS.
- Total mensal de PIS.
- Total mensal de COFINS.
- Verificacao de ISS no relatorio.
- Separacao entre proprio e retido.
- Comparacao com razao contabil.
- Comparacao com guia ou apuracao.
- Conferencia de lote contabil, quando houver integracao.

## Resultado esperado

Saldos mensais de PIS e COFINS conferidos e prontos para lancamento ou validacao no Alterdata. Se houver ISS no relatorio, o valor deve ficar separado para conferencia propria, sem misturar com PIS/COFINS.

## Prevencao

- Criar checklist mensal de fechamento PIS/COFINS/ISS.
- Salvar memoria de calculo interna sem dados sensiveis.
- Separar impostos proprios de retencoes.
- Conferir competencias antes de somar o ano completo.
- Comparar Fiscal e Contabil antes do fechamento.
- Evitar lancamento manual sem identificar a origem no Fiscal.

## Checklist final

- A empresa foi anonimizada como Cliente A?
- O periodo analisado cobre o ano completo?
- PIS proprio foi separado de PIS retido?
- COFINS proprio foi separado de COFINS retido?
- ISS foi identificado separadamente?
- Valores foram totalizados por mes?
- Total anual foi calculado pela soma mensal?
- A apuracao foi conferida?
- O razao contabil foi comparado?
- O lote da integracao foi verificado?
- Ajustes manuais foram documentados?

## Links relacionados

- [PIS, COFINS e ISS na Integracao Fiscal x Contabil](../../docs/integracao-fiscal-contabil/pis-cofins-iss.md)
- [Conferencia Operacional de PIS e COFINS](../../docs/fiscal/pis-cofins.md)
- [Conferencia Operacional de ISS](../../docs/fiscal/iss.md)
