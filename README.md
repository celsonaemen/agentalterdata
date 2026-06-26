# Agente Especialista Alterdata

Base de conhecimento operacional para apoiar rotinas de escritorio contabil com foco no ecossistema Alterdata, especialmente Alterdata Pack/PHD, Fiscal, Contabil, WPHD, Integracao Fiscal x Contabil, Acessorias e Orion.

O objetivo deste repositorio e organizar procedimentos, diagnosticos, erros recorrentes, casos reais anonimizados e bases de consulta para que uma IA atue como apoio tecnico pratico nas demandas do dia a dia.

## Modulos cobertos

- Contabil
- Fiscal
- PIS/COFINS
- ISS
- Integracao Fiscal x Contabil
- Tributos na integracao Fiscal x Contabil
- WPHD
- DP
- Acessorias
- Orion
- Erros Comuns
- Casos Reais

## Uso esperado

Use este repositorio como base de conhecimento operacional para:

- Registrar procedimentos internos.
- Padronizar diagnosticos e correcoes.
- Documentar casos reais de forma anonimizada.
- Organizar links e referencias oficiais.
- Apoiar conferencias entre Fiscal e Contabil.
- Reduzir reincidencia de erros em rotinas do Alterdata.

## Controle de fontes oficiais

O projeto usa links oficiais da Alterdata como referencia, mas os documentos internos devem ser resumos proprios e procedimentos operacionais.

A pasta [bases-oficiais/bdcc/](bases-oficiais/bdcc/) controla os links oficiais, modulo, assunto, status da fonte, data de consulta e relacao com documentos internos. Essa camada ajuda a separar conhecimento oficial Alterdata, procedimento interno do escritorio e caso real resolvido.

Os primeiros links oficiais da Integracao Fiscal x Contabil ja foram mapeados em [bases-oficiais/bdcc/integracao-fiscal-contabil.md](bases-oficiais/bdcc/integracao-fiscal-contabil.md).

O projeto tambem possui fichas individuais para as fontes oficiais da Integracao Fiscal x Contabil em [bases-oficiais/bdcc/fontes/integracao-fiscal-contabil/](bases-oficiais/bdcc/fontes/integracao-fiscal-contabil/).

## Validacao de seguranca

O script abaixo ajuda a encontrar possiveis dados sensiveis em arquivos Markdown:

```bash
python scripts/check_sensitive_data.py
```

O script apenas imprime alertas. Ele nao bloqueia commit.

## Casos reais documentados

- [Caso 001 - CFOP de venda usado em operacao de transferencia](casos-reais/cfop/caso-001-cfop-venda-em-transferencia.md)
- [Caso 002 - Conferencia de PIS e COFINS para lancamento no Alterdata](casos-reais/pis-cofins/caso-002-conferencia-pis-cofins.md)

## Seguranca e sigilo

Nao salve neste repositorio dados sensiveis ou arquivos reais de clientes.

Evite incluir:

- XML real.
- CNPJ completo.
- CPF, RG ou dados pessoais.
- Certificados digitais.
- Tokens, senhas, chaves de API ou credenciais.
- Backups de sistemas.
- Bancos de dados.
- Relatorios com dados identificaveis.
- Documentos fiscais ou contabeis originais.

Ao registrar casos reais, anonimize empresas, valores, documentos, competencias sensiveis e qualquer informacao que permita identificar o cliente.
