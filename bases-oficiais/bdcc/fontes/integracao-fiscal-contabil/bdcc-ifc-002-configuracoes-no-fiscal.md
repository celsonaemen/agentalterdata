# Fonte Oficial - BDCC-IFC-002 - Configuracoes no cadastro da empresa

## Identificacao

**ID:** BDCC-IFC-002

**Titulo oficial:** Integracao Fiscal x Contabil: Principais configuracoes no Fiscal para a Integracao Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-principais-configuracoes-no-fiscal-para-a-integracao-fiscal-x-contabil-184784013.html

**Modulo:** Fiscal

**Assunto:** Configuracoes no cadastro da empresa

**Documento interno relacionado:** [Configuracoes no Fiscal](../../../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte concentra pontos do Fiscal que precisam estar parametrizados para a integracao funcionar. A conferencia passa por cadastro da empresa, CFOP, codigo de operacao, produto, guias e exportacao. E uma referencia para quando o movimento fiscal nao gera lote ou gera lancamento incompleto.

## Uso pratico no agente

Usar quando o usuario relatar que a nota nao integrou, que o lote nao aparece, ou que a empresa parece estar sem configuracao para exportar ao Contabil.

## Relacao com o Alterdata

- Fiscal > Cadastro > Empresas
- Configuracoes de integracao
- CFOP e codigo de operacao
- Exportacao para o Contabil

## Relacao com documentos internos

- [Configuracoes no Fiscal](../../../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Empresa errada ou sem integracao marcada
- Codigo de operacao sem parametro contabil
- CFOP incoerente com a operacao
- Movimento corrigido depois de exportado

## Checklist derivado

- Empresa correta aberta?
- Integracao habilitada?
- CFOP revisado?
- Codigo de operacao revisado?
- Guias e impostos conferidos?

## Observacoes

Nao assumir que o erro esta no lote contabil antes de revisar a configuracao fiscal da empresa e do movimento.
