# Fonte Oficial - BDCC-IFC-009 - Notas de servico e ISS tomador na integracao

## Identificacao

**ID:** BDCC-IFC-009

**Titulo oficial:** Configuracao de Notas de Servicos para Integracao Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/configuracao-de-notas-de-servicos-para-integracao-fiscal-x-contabil-37261396.html

**Modulo:** Fiscal / ISS

**Assunto:** Notas de servico e ISS tomador na integracao

**Documento interno relacionado:** [PIS COFINS ISS](../../../../docs/integracao-fiscal-contabil/pis-cofins-iss.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte trata da configuracao de notas de servico para integracao, com atencao a codigos de operacao, lancamentos automaticos e ISS tomador. O uso operacional e separar servico prestado, servico tomado, imposto proprio e retencao antes de gerar o lote contabil.

## Uso pratico no agente

Usar quando houver duvida sobre ISS proprio, ISS retido, nota de servico sem lancamento, servico tomado ou divergencia entre apuracao de ISS e Contabil.

## Relacao com o Alterdata

- Movimento de servicos
- Codigo de operacao
- ISS tomador
- Lancamentos automaticos de impostos

## Relacao com documentos internos

- [PIS COFINS ISS](../../../../docs/integracao-fiscal-contabil/pis-cofins-iss.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- ISS retido nao parametrizado
- Servico sem codigo correto
- Lancamento automatico ausente
- Confundir imposto proprio com retencao

## Checklist derivado

- Nota e de servico?
- Codigo de servico conferido?
- ISS proprio ou retido separado?
- Lancamento automatico vinculado?
- Lote bate com apuracao?

## Observacoes

Nao misturar ISS com PIS/COFINS sem separar a natureza do imposto e a competencia.
