# Fonte Oficial - BDCC-IFC-005 - Cadastro de lancamento automatico no Contabil

## Identificacao

**ID:** BDCC-IFC-005

**Titulo oficial:** Como criar um lancamento automatico - Contabil

**Link oficial:** https://ajuda.alterdata.com.br/bdcc/como-criar-um-lancamento-automatico-117662446.html

**Modulo:** Contabil

**Assunto:** Cadastro de lancamento automatico no Contabil

**Documento interno relacionado:** [Lancamentos automaticos](../../../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte reforca o lado contabil do cadastro de lancamento automatico. A ficha deve ser usada para validar se as chamadas, contas e historicos existem no Contabil antes de culpar a nota fiscal. Tambem ajuda a padronizar lancamentos por natureza de operacao.

## Uso pratico no agente

Usar quando a duvida for criacao ou revisao do cadastro contabil que sera chamado pela integracao fiscal.

## Relacao com o Alterdata

- Contabil > Cadastros > Lancamentos Automaticos
- Plano de contas
- Historicos padroes
- Lotes contabeis

## Relacao com documentos internos

- [Lancamentos automaticos](../../../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Cadastro incompleto no Contabil
- Conta inativa ou fora do plano
- Historico sem informacao util
- Reaproveitar lancamento automatico de outra operacao

## Checklist derivado

- Lancamento existe no Contabil?
- Contas estao ativas?
- Historico esta claro?
- Codigo usado no Fiscal aponta para este cadastro?

## Observacoes

Quando houver lancamento automatico duplicado, registrar qual e o padrao interno antes de alterar parametrizacoes.
