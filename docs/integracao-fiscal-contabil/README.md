# Integracao Fiscal x Contabil

A Integracao Fiscal x Contabil no Alterdata conecta o Pack Fiscal ao Pack Contabil para transformar movimentos fiscais em lancamentos contabeis. O objetivo e reduzir retrabalho, evitar divergencias entre modulos e manter a escrituracao mais consistente.

Na pratica, a integracao depende de parametrizacoes feitas no Fiscal e no Contabil. O Fiscal precisa saber quando uma empresa integra com a Contabilidade, quais movimentos serao enviados, quais clientes e fornecedores possuem vinculacao contabil e quais lancamentos automaticos serao usados para gerar debito, credito e historico.

## Principais pontos da integracao

- Configuracao no cadastro da empresa no Fiscal.
- Lancamentos automaticos cadastrados no Contabil.
- Historicos padroes para gerar o texto dos lancamentos.
- Vinculacao contabil de clientes e fornecedores.
- Configuracoes de exportacao dos movimentos.
- Exportacao dos movimentos fiscais para o Contabil.
- Conferencia dos lotes gerados no Contabil.
- Correcao de erros comuns antes de reexportar.

## Fluxo ideal da integracao

1. Conferir o cadastro da empresa no Fiscal.
2. Marcar a empresa para integrar com a Contabilidade, quando aplicavel.
3. Revisar plano de contas, contas de clientes, fornecedores, receitas, despesas e impostos.
4. Cadastrar ou revisar os lancamentos automaticos no Contabil.
5. Conferir historicos padroes e complementos usados nos lancamentos.
6. Fazer a vinculacao contabil de clientes e fornecedores.
7. Escriturar ou importar as notas fiscais no Fiscal.
8. Conferir CFOP, CST, bases, impostos e codigo de operacao.
9. Exportar os movimentos para o Contabil.
10. Conferir lote, debito, credito, historico, data, valor e conta contabil.
11. Corrigir a causa da divergencia antes de reexportar.

## Arquivos desta pasta

- [configuracoes-no-fiscal.md](configuracoes-no-fiscal.md): configuracao da empresa no Fiscal para permitir a integracao.
- [lancamentos-automaticos.md](lancamentos-automaticos.md): cadastro e conferencia dos lancamentos automaticos usados na integracao.
- [vinculacao-contabil.md](vinculacao-contabil.md): relacao entre clientes, fornecedores e contas contabeis.
- [exportacao-para-contabil.md](exportacao-para-contabil.md): fluxo de exportacao dos movimentos fiscais para o Contabil.
- [pis-cofins-iss.md](pis-cofins-iss.md): conferencia de PIS, COFINS e ISS na integracao entre Fiscal e Contabil.
- [checklist-fechamento-mensal.md](checklist-fechamento-mensal.md): checklist mensal para conferencia antes, durante e depois da integracao.
- [roteiro-diagnostico-divergencia.md](roteiro-diagnostico-divergencia.md): roteiro para diagnosticar diferencas entre Fiscal e Contabil.
- [troubleshooting.md](troubleshooting.md): diagnostico de erros e divergencias comuns.

## Principais riscos

- Empresa errada ou competencia errada na exportacao.
- Integracao desmarcada no cadastro da empresa.
- Lancamento automatico sem conta de debito ou credito.
- Historico padrao ausente, muito grande ou inadequado.
- Cliente ou fornecedor sem vinculacao contabil.
- CFOP ou codigo de operacao incorreto.
- Nota com mais de um CFOP tratada como se fosse uma unica operacao.
- Impostos sem parametrizacao contabil.
- Movimento exportado mais de uma vez.
- Alteracao no Fiscal depois da exportacao sem ajuste no Contabil.

## Checklist rapido

- A empresa esta correta no Fiscal e no Contabil?
- A competencia esta correta?
- A opcao de integracao com a Contabilidade esta habilitada?
- O plano de contas usado e o correto?
- Os lancamentos automaticos estao completos?
- As contas de debito e credito estao corretas?
- O historico padrao esta adequado?
- Clientes e fornecedores estao vinculados corretamente?
- CFOP, CST e codigo de operacao foram revisados?
- Os impostos foram conferidos antes da exportacao?
- O lote foi gerado sem diferenca entre debito e credito?
- O valor integrado bate com os relatorios fiscais?
