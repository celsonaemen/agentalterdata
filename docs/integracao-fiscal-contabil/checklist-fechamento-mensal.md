# Checklist de Fechamento Mensal - Fiscal x Contabil

## Objetivo

Validar a integracao entre Fiscal e Contabil antes do fechamento mensal, reduzindo divergencias de valores, CFOP incorreto, impostos nao integrados, cliente ou fornecedor em conta errada e lotes com diferenca entre debito e credito.

Este checklist deve ser usado como procedimento interno do escritorio. Nao substitui a conferencia fiscal, contabil ou tributaria especifica de cada empresa.

## Quando usar

- Antes de exportar movimentos do Fiscal para o Contabil.
- Apos correcoes de notas fiscais.
- Apos ajuste de CFOP ou codigo de operacao.
- Antes da entrega de obrigacoes.
- Antes de fechar balancete.

## Etapa 1 - Conferencia da empresa

- [ ] Empresa correta selecionada.
- [ ] Competencia correta.
- [ ] Regime tributario conferido.
- [ ] Cadastro da empresa revisado.
- [ ] Opcao de integracao com Contabil habilitada, quando aplicavel.
- [ ] Plano de contas correto.
- [ ] Empresa vinculada corretamente entre Fiscal e Contabil.

## Etapa 2 - Conferencia das notas fiscais

- [ ] Notas de entrada importadas.
- [ ] Notas de saida importadas.
- [ ] Notas de servico conferidas.
- [ ] Canceladas/inutilizadas verificadas.
- [ ] Notas fora da competencia identificadas.
- [ ] Duplicidades verificadas.
- [ ] Totais de notas conferidos com relatorio fiscal.

## Etapa 3 - Conferencia de CFOP e codigo de operacao

- [ ] CFOP de venda conferido.
- [ ] CFOP de compra conferido.
- [ ] CFOP de transferencia conferido.
- [ ] CFOP de devolucao conferido.
- [ ] Codigo de operacao compativel com a natureza da operacao.
- [ ] Operacoes sem CFOP ou com CFOP generico revisadas.
- [ ] Casos de venda x transferencia revisados.

Observacao: CFOP errado pode gerar conta contabil errada, historico incorreto, valor divergente e lancamento incompativel com a operacao real.

## Etapa 4 - Conferencia de impostos

- [ ] ICMS conferido.
- [ ] IPI conferido, quando houver.
- [ ] PIS conferido.
- [ ] COFINS conferido.
- [ ] ISS conferido.
- [ ] Retencoes conferidas.
- [ ] Imposto proprio separado de imposto retido.
- [ ] Base de calculo e aliquota conferidas.
- [ ] Relatorios fiscais comparados com apuracao.

## Etapa 5 - Conferencia de clientes e fornecedores

- [ ] Clientes cadastrados corretamente.
- [ ] Fornecedores cadastrados corretamente.
- [ ] Vinculacao contabil revisada.
- [ ] Conta individual ou generica definida conforme padrao do escritorio.
- [ ] CNPJ/CPF nao deve ser salvo no repositorio, apenas conferido no sistema.
- [ ] Cliente/fornecedor sem conta contabil identificado.

## Etapa 6 - Conferencia dos lancamentos automaticos

- [ ] Lancamentos automaticos de entrada conferidos.
- [ ] Lancamentos automaticos de saida conferidos.
- [ ] Lancamentos de ISS tomador conferidos.
- [ ] Lancamentos de PIS/COFINS conferidos.
- [ ] Contas de debito e credito revisadas.
- [ ] Historico padrao revisado.
- [ ] Centro de custos revisado, quando usado.
- [ ] Lancamentos sem conta contabil corrigidos.

## Etapa 7 - Exportacao para o Contabil

- [ ] Competencia correta selecionada.
- [ ] Tipo de movimento correto.
- [ ] Opcoes de exportacao conferidas.
- [ ] Movimentos ja exportados verificados.
- [ ] Exportacao direta ou TXT definida.
- [ ] Lote gerado identificado.
- [ ] Mensagens de erro registradas.

## Etapa 8 - Conferencia no Contabil

- [ ] Lote importado localizado.
- [ ] Debito e credito fechando.
- [ ] Valores conferidos com relatorio fiscal.
- [ ] Historicos conferidos.
- [ ] Documento/numero da nota conferido.
- [ ] Contas contabeis conferidas.
- [ ] Razao conferido.
- [ ] Balancete revisado.

## Etapa 9 - Tratamento de divergencias

| Sintoma | Causa provavel | Onde verificar | Como corrigir |
| --- | --- | --- | --- |
| Fiscal nao bate com Contabil. | Nota nao integrada, nota duplicada, CFOP incorreto ou ajuste manual no Contabil. | Relatorio fiscal, lote contabil, razao e movimento de notas. | Separar por competencia, localizar a diferenca e corrigir a origem antes de reintegrar. |
| Lote com diferenca entre debito e credito. | Lancamento automatico incompleto, conta ausente ou imposto sem contrapartida. | Lancamentos automaticos, contas de debito/credito e lote. | Corrigir parametrizacao e gerar novo lote conforme politica do escritorio. |
| Nota nao apareceu na integracao. | Competencia errada, tipo de movimento nao selecionado, nota cancelada ou movimento ja exportado. | Movimento de notas, exportacao, controle de integracao. | Corrigir selecao/parametro e reexportar apenas se necessario. |
| Cliente/fornecedor em conta errada. | Vinculacao contabil incorreta ou cadastro duplicado. | Vinculacao contabil, cadastro da pessoa, razao. | Ajustar vinculacao e revisar lote gerado. |
| CFOP gerou lancamento errado. | CFOP ou codigo de operacao incompativel com a natureza real. | Itens da nota, CFOP, codigo de operacao, lancamento automatico. | Corrigir classificacao fiscal e reintegrar conforme controle do lote anterior. |
| PIS/COFINS nao integrou. | CST, base, retencao ou parametrizacao contabil incorreta. | Apuracao, itens da nota, lancamento automatico e razao. | Separar proprio/retido, corrigir parametros e validar no Contabil. |
| ISS retido nao integrou. | Retencao nao marcada, servico sem codigo ou conta contabil ausente. | Movimento de servicos, apuracao de ISS, lancamento automatico. | Corrigir dados de servico e parametrizacao antes de reexportar. |
| Movimento ja exportado anteriormente. | Reexportacao sem tratamento do lote anterior. | Controle de exportacao no Fiscal e lotes no Contabil. | Identificar lote anterior e decidir excluir, estornar, manter ou ajustar conforme politica interna. |

## Etapa 10 - Fechamento e evidencia

- [ ] Relatorios fiscais salvos internamente conforme politica do escritorio.
- [ ] Balancete conferido.
- [ ] Razao das contas principais conferido.
- [ ] Pendencias registradas.
- [ ] Correcoes documentadas.
- [ ] Casos relevantes transformados em caso real no repositorio, sempre anonimizados.

## Checklist rapido final

- [ ] Empresa e competencia corretas.
- [ ] Notas fiscais conferidas.
- [ ] CFOP e codigo de operacao revisados.
- [ ] PIS, COFINS e ISS separados entre proprio e retido.
- [ ] Clientes e fornecedores vinculados corretamente.
- [ ] Lancamentos automaticos completos.
- [ ] Exportacao feita apenas apos correcoes.
- [ ] Lote localizado no Contabil.
- [ ] Debito e credito fechando.
- [ ] Razao e balancete conferidos.
- [ ] Pendencias documentadas.

## Links internos relacionados

- [README da integracao](README.md)
- [Troubleshooting](troubleshooting.md)
- [Configuracoes no Fiscal](configuracoes-no-fiscal.md)
- [Lancamentos automaticos](lancamentos-automaticos.md)
- [Vinculacao contabil](vinculacao-contabil.md)
- [Exportacao para o Contabil](exportacao-para-contabil.md)
- [PIS, COFINS e ISS na integracao](pis-cofins-iss.md)
- [CFOP de venda x CFOP de transferencia](../fiscal/cfop-venda-transferencia.md)
- [Conferencia operacional de PIS e COFINS](../fiscal/pis-cofins.md)
- [Conferencia operacional de ISS](../fiscal/iss.md)
