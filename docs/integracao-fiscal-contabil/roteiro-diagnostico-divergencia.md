# Roteiro de Diagnostico - Divergencia Fiscal x Contabil

## Objetivo

Criar um roteiro pratico para quando o valor do Fiscal nao bate com o Contabil. A investigacao deve localizar a origem da diferenca antes de ajustar manualmente o lote contabil.

## Diagnostico rapido

- A competencia esta correta?
- O relatorio fiscal usado e o mesmo periodo do lote contabil?
- Houve reexportacao?
- O lote anterior foi excluido/estornado?
- Existe nota com CFOP errado?
- Existe codigo de operacao errado?
- Existem notas de servico com ISS retido?
- PIS/COFINS foi separado entre proprio e retido?
- Cliente/fornecedor caiu na conta correta?
- O lancamento automatico esta correto?

## Ordem recomendada de investigacao

1. Conferir relatorio fiscal.
2. Conferir movimento de notas.
3. Conferir CFOP/codigo de operacao.
4. Conferir impostos.
5. Conferir vinculacao contabil.
6. Conferir lancamento automatico.
7. Conferir exportacao.
8. Conferir lote contabil.
9. Conferir razao/balancete.
10. Documentar causa e correcao.

## Causas comuns

### CFOP incorreto

O CFOP pode direcionar a nota para uma natureza errada, como venda tratada como transferencia ou transferencia tratada como venda.

### Codigo de operacao incompativel

Mesmo com CFOP correto, codigo de operacao errado pode puxar lancamento automatico, historico ou conta contabil incompat?vel com a operacao real.

### Lancamento automatico errado

Conta de debito, conta de credito ou historico podem estar ausentes ou apontando para uma operacao diferente.

### Conta contabil errada

A conta pode estar incorreta no lancamento automatico, na vinculacao contabil ou no cadastro de cliente/fornecedor.

### Nota fora da competencia

A nota pode estar escriturada em periodo diferente do relatorio fiscal ou do lote contabil analisado.

### Nota duplicada

Duplicidade de nota ou reexportacao sem controle pode inflar valores no Fiscal ou no Contabil.

### Movimento ja exportado

Movimento marcado como exportado pode nao aparecer novamente ou pode gerar duplicidade se o lote anterior nao for tratado.

### Tributo retido confundido com tributo proprio

PIS, COFINS ou ISS retidos podem ter tratamento contabil diferente do imposto proprio. Misturar esses valores gera divergencia.

### Historico padrao incorreto

Historico padrao ruim dificulta localizar a nota e pode indicar que o lancamento automatico usado nao e o correto.

### Cliente/fornecedor sem vinculacao contabil

Cadastro sem conta vinculada pode jogar valor em conta generica, conta errada ou impedir a integracao esperada.

## Como corrigir

- Corrigir origem no Fiscal sempre que possivel.
- Revisar parametrizacao da empresa, CFOP, codigo de operacao, impostos e lancamentos automaticos.
- Reprocessar integracao quando a causa estiver corrigida.
- Excluir ou estornar lote incorreto conforme politica do escritorio.
- Reintegrar somente os movimentos necessarios.
- Validar no Contabil antes de encerrar a pendencia.

## Como validar

- Comparar relatorio fiscal x lote contabil.
- Conferir razao.
- Conferir balancete.
- Conferir contas de impostos.
- Conferir contas de clientes/fornecedores.
- Conferir historico e documento.
- Confirmar que debito e credito fecham.
- Registrar a causa encontrada e a correcao aplicada.

## Quando virar caso real

Divergencias recorrentes, erros novos ou problemas relevantes devem ser documentados em `casos-reais/`, sempre sem dados sensiveis.

Use caso real quando:

- O problema se repetiu em mais de uma empresa ou competencia.
- A causa nao era obvia.
- A correcao exigiu varias etapas.
- O erro pode treinar a equipe para evitar reincidencia.
- A situacao envolve CFOP, PIS/COFINS, ISS, integracao, lote ou vinculacao contabil.

## Links internos relacionados

- [Checklist de fechamento mensal](checklist-fechamento-mensal.md)
- [Troubleshooting](troubleshooting.md)
- [Exportacao para o Contabil](exportacao-para-contabil.md)
- [Vinculacao contabil](vinculacao-contabil.md)
- [Lancamentos automaticos](lancamentos-automaticos.md)
- [PIS, COFINS e ISS na integracao](pis-cofins-iss.md)
