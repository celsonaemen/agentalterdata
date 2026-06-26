# Fonte Oficial - BDCC-IFC-003 - Vinculacao contabil de clientes e fornecedores

## Identificacao

**ID:** BDCC-IFC-003

**Titulo oficial:** Vinculacao Contabil - Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-vinculacao-contabil-220178968.html

**Modulo:** Fiscal / Contabil

**Assunto:** Vinculacao contabil de clientes e fornecedores

**Documento interno relacionado:** [Vinculacao contabil](../../../../docs/integracao-fiscal-contabil/vinculacao-contabil.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

## Resumo proprio

Esta fonte trata da relacao entre clientes, fornecedores e contas contabeis usadas na integracao. A vinculacao pode afetar entrada, saida ou ambos, conforme a rotina da empresa. E importante para evitar que valores integrados caiam em conta generica ou em cadastro incorreto.

## Uso pratico no agente

Usar quando cliente ou fornecedor cair em conta errada, quando houver duvida entre conta individual e generica, ou quando a conciliacao nao fechar por conta vinculada incorreta.

## Relacao com o Alterdata

- Fiscal > aba Contabil > Vinculacao Contabil
- Cadastro de clientes e fornecedores
- Razao de contas a receber e a pagar
- Lote gerado pela integracao

## Relacao com documentos internos

- [Vinculacao contabil](../../../../docs/integracao-fiscal-contabil/vinculacao-contabil.md)
- [Arquivo central de fontes oficiais](../../integracao-fiscal-contabil.md)
- [Indice de links oficiais](../../indice-links.md)

## Riscos de erro na pratica

- Vincular apenas entrada quando a rotina exige saida
- Usar conta generica indevidamente
- Cadastrar conta fora do plano correto
- Ignorar duplicidade de cliente ou fornecedor

## Checklist derivado

- Cadastro correto?
- Vinculacao para entrada, saida ou ambos?
- Conta pertence ao plano da empresa?
- Razao confirma o saldo esperado?

## Observacoes

Ajuste manual no Contabil nao resolve recorrencia quando a vinculacao fiscal continua errada.
