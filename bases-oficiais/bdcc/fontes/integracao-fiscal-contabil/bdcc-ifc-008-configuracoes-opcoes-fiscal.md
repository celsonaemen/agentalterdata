# Fonte Oficial - BDCC-IFC-008 - Configuracoes e opcoes de exportacao

## Identificacao

**ID:** BDCC-IFC-008

**Titulo oficial:** Integracao Fiscal x Contabil: Selecoes em Configuracoes Opcoes no Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-selecoes-em-configuracoes-opcoes-no-fiscal-208372180.html

**Modulo:** Fiscal

**Assunto:** Configuracoes e opcoes de exportacao

**Documento interno relacionado:** [Configuracoes no Fiscal](../../../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte cobre opcoes do Fiscal que afetam a forma de exportacao para o Contabil. Ela ajuda a analisar historicos, impostos, ISS tomador e criterios que podem alterar o valor ou a forma do lancamento integrado. E relevante quando o problema esta em parametrizacao, nao na nota isolada.

## Uso pratico no agente

Usar em divergencias de valor liquido, impostos nao integrados, ISS tomador, historico diferente do esperado ou exportacao com comportamento inconsistente.

## Relacao com o Alterdata

- Configuracoes do Fiscal
- Opcoes de exportacao
- Integracao de impostos
- Lote contabil

## Relacao com documentos internos

- [Configuracoes no Fiscal](../../../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Parametro fiscal diferente do padrao interno
- Imposto abatido de forma inesperada
- Aglutinacao indevida
- Reexportacao sem revisar opcoes

## Checklist derivado

- Opcoes de exportacao conferidas?
- Impostos estao parametrizados?
- ISS tomador revisado?
- Historico e aglutinacao conferidos?

## Observacoes

Antes de mexer no lote, revisar se uma opcao do Fiscal esta mudando a forma do lancamento.
