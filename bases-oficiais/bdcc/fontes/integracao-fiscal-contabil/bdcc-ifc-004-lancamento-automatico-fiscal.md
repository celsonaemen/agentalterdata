# Fonte Oficial - BDCC-IFC-004 - Cadastro de lancamento automatico

## Identificacao

**ID:** BDCC-IFC-004

**Titulo oficial:** Como criar um lancamento automatico - Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-como-cadastrar-um-lancamento-automatico-37261453.html

**Modulo:** Contabil

**Assunto:** Cadastro de lancamento automatico

**Documento interno relacionado:** [Lancamentos automaticos](../../../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte mostra o lancamento automatico como base para formar debito, credito e historico no lote contabil. O cadastro precisa estar coerente com o plano de contas e vinculado a rotina fiscal correta. E uma fonte central para explicar lote com diferenca ou ausencia de conta.

## Uso pratico no agente

Usar quando o usuario relatar diferenca entre debito e credito, ausencia de lancamento, historico errado ou conta vazia na integracao.

## Relacao com o Alterdata

- Contabil > Cadastros > Lancamentos Automaticos
- Vinculo com plano de contas
- Historico padrao
- Exportacao do Fiscal para o Contabil

## Relacao com documentos internos

- [Lancamentos automaticos](../../../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Chamada devedora ou credora ausente
- Historico padrao inadequado
- Lancamento de venda usado em transferencia
- Plano de contas incorreto

## Checklist derivado

- Descricao identifica a operacao?
- Debito preenchido?
- Credito preenchido?
- Historico padrao adequado?
- Plano de contas correto?

## Observacoes

Sempre conferir o lancamento automatico antes de excluir ou refazer lote, porque o erro tende a repetir na proxima exportacao.
