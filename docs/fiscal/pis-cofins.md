# Conferencia Operacional de PIS e COFINS no Alterdata

PIS e COFINS devem ser conferidos por competencia, regime tributario, CST, base de calculo, aliquota, valor do imposto e retencoes. A forma de apuracao e o reflexo contabil dependem do regime da empresa, tipo de receita, operacao e parametrizacao fiscal.

Use este procedimento como roteiro interno de conferencia antes de integrar ou lancar valores no Contabil.

## PIS/COFINS proprio x PIS/COFINS retido

PIS/COFINS proprio e o valor apurado sobre receitas ou operacoes tributadas, conforme regime e parametrizacao da empresa.

PIS/COFINS retido e o valor retido por terceiros ou destacado como retencao, podendo ter tratamento contabil diferente do imposto proprio. Nao some retencao com imposto proprio sem confirmar a finalidade do relatorio.

## Onde conferir

- Movimento de notas.
- Itens da nota.
- CST.
- Base de calculo.
- Aliquota.
- Valor de PIS.
- Valor de COFINS.
- Retencoes.
- Relatorio de apuracao.
- SPED Contribuicoes, quando aplicavel.

## Erros comuns

- CST incorreto.
- Aliquota incorreta.
- Receita sem tributacao.
- Produto ou servico sem parametrizacao.
- Retencao lancada como imposto proprio.
- Imposto proprio tratado como retencao.
- Nota fora da competencia.
- Duplicidade de exportacao para o Contabil.
- Codigo de operacao errado.
- Lote contabil gerado antes da correcao fiscal.

## Como validar

1. Selecione a empresa e a competencia correta.
2. Gere relatorio fiscal de PIS/COFINS.
3. Separe PIS e COFINS.
4. Separe imposto proprio e retencao.
5. Confira CST, base de calculo, aliquota e valor.
6. Compare o total mensal com a apuracao.
7. Compare o total integrado com o lote contabil.
8. Confira o razao das contas de PIS e COFINS.
9. Investigue diferencas por nota antes de ajustar manualmente.

## Relacao com a Integracao Fiscal x Contabil

Na integracao, PIS e COFINS podem gerar lancamentos de imposto a recolher, imposto a recuperar, retencao, despesa, receita ou contas de apuracao, conforme a parametrizacao.

Se PIS/COFINS nao bater com o Contabil, confira:

- CST dos itens.
- Codigo de operacao.
- CFOP.
- Base e aliquota.
- Retencao.
- Lancamento automatico.
- Conta contabil vinculada.
- Lote ja exportado.

Quando houver alteracao no Fiscal depois da exportacao, controle o lote anterior antes de reintegrar.

## Checklist rapido

- PIS proprio foi separado de PIS retido?
- COFINS proprio foi separado de COFINS retido?
- A competencia esta correta?
- A nota pertence ao periodo analisado?
- CST e aliquota estao coerentes com a rotina da empresa?
- O valor bate com a apuracao?
- O valor integrado bate com o Contabil?
- Existe lote duplicado ou movimento ja exportado?
