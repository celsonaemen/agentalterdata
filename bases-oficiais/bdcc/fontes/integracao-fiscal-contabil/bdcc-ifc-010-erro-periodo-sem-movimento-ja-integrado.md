# Fonte Oficial - BDCC-IFC-010 - Erro de integracao sem movimento ou ja integrada

## Identificacao

**ID:** BDCC-IFC-010

**Titulo oficial:** Integracao Fiscal x Contabil: Nao foi possivel efetuar a integracao, o periodo escolhido nao possui movimento ou entao ja foi feita a integracao

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-nao-foi-possivel-efetuar-a-integracao-o-periodo-escolhido-nao-possui-movimento-ou-entao-ja-foi-feita-a-integracao-37261407.html

**Modulo:** Fiscal / Contabil

**Assunto:** Erro de integracao sem movimento ou ja integrada

**Documento interno relacionado:** [Troubleshooting](../../../../docs/integracao-fiscal-contabil/troubleshooting.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte aborda falha de integracao quando o periodo nao possui movimento apto ou quando a integracao ja foi feita. A causa pratica pode estar em competencia errada, movimento ja exportado ou falta de vinculo com lancamento automatico. E uma base para diagnosticar lote nao gerado.

## Uso pratico no agente

Usar quando o usuario relatar mensagem de periodo sem movimento, movimento ja integrado, nota ausente na exportacao ou tentativa de reexportar sem controlar lote anterior.

## Relacao com o Alterdata

- Fiscal > Integracao Contabil
- Movimento de notas
- Controle de exportacao
- Contabil > Lotes

## Relacao com documentos internos

- [Troubleshooting](../../../../docs/integracao-fiscal-contabil/troubleshooting.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Selecionar competencia errada
- Tentar integrar movimento ja exportado
- Nao tratar lote anterior
- Faltar lancamento automatico no movimento

## Checklist derivado

- Competencia correta?
- Existe movimento no periodo?
- Movimento ja foi integrado?
- Lancamento automatico esta vinculado?
- Lote anterior foi controlado?

## Observacoes

A reexportacao so deve ocorrer depois de identificar o que foi integrado antes.
