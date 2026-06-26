# Troubleshooting da Integracao Fiscal x Contabil

Este guia ajuda a diagnosticar problemas comuns na integracao entre Fiscal e Contabil. Use como roteiro antes de corrigir manualmente o lote no Contabil.

## Fiscal nao gera lote no Contabil

### Sintoma

A exportacao e executada, mas nenhum lote aparece no Contabil.

### Causa provavel

Integracao desabilitada, empresa incorreta, competencia sem movimento, parametrizacao incompleta ou movimento ja exportado.

### Onde verificar no Alterdata

- `Fiscal > Cadastro > Empresas > Geral > Integracao`
- `Fiscal > Contabil > Exportar para o Contabil`
- `Contabil > Lotes`

### Como corrigir

Confirme empresa, competencia e opcao `Integra com a Contabilidade`. Depois revise os movimentos selecionados, os lancamentos automaticos e se a competencia possui notas fiscais validas para exportacao.

### Como validar

Execute nova exportacao controlada e confira se o lote aparece no Contabil com data, valor e historico esperados.

## Lote gerado com diferenca entre debito e credito

### Sintoma

O lote e criado, mas nao fecha debito e credito.

### Causa provavel

Lancamento automatico incompleto, conta de debito ou credito ausente, imposto sem contrapartida, centro de custo obrigatorio ou parametrizacao diferente por tipo de movimento.

### Onde verificar no Alterdata

- `Contabil > Cadastros > Lancamentos Automaticos`
- `Fiscal > Cadastro > Empresas > Geral > Integracao`
- `Fiscal > Contabil > Exportar para o Contabil`
- `Contabil > Lotes`

### Como corrigir

Abra o lancamento automatico usado no movimento e confira chamada devedora, chamada credora, historico e centro de custo. Corrija a parametrizacao antes de reexportar.

### Como validar

Gere o lote novamente em ambiente controlado e confira se total de debitos e creditos ficou igual.

## Nota fiscal nao aparece na exportacao

### Sintoma

A nota esta escriturada no Fiscal, mas nao aparece para exportar ao Contabil.

### Causa provavel

Nota fora da competencia, tipo de movimento nao selecionado, nota cancelada, codigo de operacao sem integracao ou movimento ja exportado.

### Onde verificar no Alterdata

- Escrituracao da nota no Fiscal.
- Parametros da exportacao.
- Cadastro da empresa.
- Codigo de operacao.
- Controle de movimentos ja exportados.

### Como corrigir

Confirme a data da nota, competencia, situacao do documento, tipo de movimento e codigo de operacao. Se a nota ja foi exportada, avalie se o lote anterior precisa ser tratado antes de nova exportacao.

### Como validar

Refaca a selecao da exportacao e confirme se a nota aparece na listagem ou no lote gerado.

## Valor do Fiscal nao bate com o Contabil

### Sintoma

O total do relatorio fiscal e diferente do valor integrado no Contabil.

### Causa provavel

Nota nao exportada, nota duplicada, CFOP incorreto, item com tratamento diferente, imposto nao integrado, reexportacao sem exclusao do lote anterior ou ajuste manual no Contabil.

### Onde verificar no Alterdata

- Relatorios fiscais por competencia.
- Exportacao para o Contabil.
- Lotes do Contabil.
- Razao das contas afetadas.

### Como corrigir

Separe por competencia, tipo de movimento, CFOP e imposto. Compare nota a nota ate localizar a diferenca. Corrija a origem no Fiscal ou a parametrizacao antes de ajustar o Contabil.

### Como validar

Compare novamente relatorio fiscal, lote contabil e razao da conta. O valor deve bater por competencia e por natureza da operacao.

## CFOP errado gerando conta errada

### Sintoma

O lancamento vai para conta contabil incompativel com a operacao.

### Causa provavel

CFOP incorreto na nota, codigo de operacao errado ou lancamento automatico vinculado a operacao errada.

### Onde verificar no Alterdata

- Nota fiscal no Fiscal.
- Itens da nota.
- CFOP.
- Codigo de operacao.
- Lancamento automatico vinculado.

### Como corrigir

Revise a operacao real da nota. Ajuste CFOP, codigo de operacao e lancamento automatico conforme orientacao fiscal e rotina interna. Reexporte somente depois de controlar o lote anterior.

### Como validar

Confira se o novo lancamento caiu na conta correta e se o valor bate com o movimento fiscal.

## Cliente ou fornecedor caindo em conta errada

### Sintoma

O valor foi integrado, mas caiu em conta de cliente ou fornecedor incorreta.

### Causa provavel

Vinculacao contabil incorreta, cadastro duplicado, conta generica indevida ou lancamento automatico ignorando a vinculacao.

### Onde verificar no Alterdata

- `Fiscal > aba Contabil > Vinculacao Contabil`
- Cadastro do cliente ou fornecedor.
- Lancamento automatico usado.
- Razao da conta contabil.

### Como corrigir

Corrija a vinculacao contabil para entrada, saida ou ambos. Confira se a conta pertence ao plano correto e se a rotina deve usar conta individual ou generica.

### Como validar

Reexporte de forma controlada ou teste com um movimento especifico. Confira o razao da conta correta.

## Historico muito grande ou incorreto

### Sintoma

O lancamento aparece com historico inadequado, truncado, confuso ou maior que o permitido pela rotina.

### Causa provavel

Historico padrao mal configurado, complemento puxando informacao excessiva ou informacao adicional da nota sem tratamento.

### Onde verificar no Alterdata

- Cadastro de historicos padroes no Contabil.
- Lancamento automatico.
- Parametros da integracao.
- Dados adicionais da nota fiscal.

### Como corrigir

Simplifique o historico padrao e use complementos realmente necessarios para identificacao. Evite levar informacao excessiva do documento fiscal para o lancamento.

### Como validar

Gere novo lote de teste e confira se o historico ficou claro, util e aceito pelo Contabil.

## PIS/COFINS nao integrado

### Sintoma

O valor de PIS/COFINS aparece no Fiscal, mas nao gera reflexo contabil esperado.

### Causa provavel

CST, acumulador, codigo de operacao ou lancamento automatico sem parametrizacao contabil para PIS/COFINS.

### Onde verificar no Alterdata

- Itens da nota.
- CST de PIS/COFINS.
- Acumulador ou codigo de operacao.
- Lancamento automatico.
- Relatorio fiscal de apuracao.

### Como corrigir

Confira se o imposto deve integrar contabilmente. Depois ajuste parametrizacao fiscal e contabil conforme a rotina da empresa.

### Como validar

Compare apuracao fiscal, lote contabil e razao das contas de PIS/COFINS.

## ISS retido nao integrado

### Sintoma

O ISS retido aparece na nota ou na apuracao, mas nao gera lancamento no Contabil.

### Causa provavel

Servico sem parametrizacao, retencao nao marcada, municipio/codigo de servico incorreto ou lancamento automatico sem conta para ISS retido.

### Onde verificar no Alterdata

- Nota de servico no Fiscal.
- Retencao de ISS.
- Codigo de servico.
- Municipio.
- Lancamento automatico.

### Como corrigir

Revise os dados do servico e a retencao. Ajuste o lancamento automatico para refletir a conta correta de ISS retido, quando a rotina contabil exigir.

### Como validar

Confira o lote contabil, a conta de ISS retido e o relatorio fiscal da competencia.

## Movimento ja exportado anteriormente

### Sintoma

O sistema indica que o movimento ja foi exportado ou o Contabil apresenta duplicidade.

### Causa provavel

Reexportacao sem controle do lote anterior, movimento alterado apos exportacao ou tentativa de exportar novamente a mesma competencia.

### Onde verificar no Alterdata

- Controle de exportacao no Fiscal.
- Lotes gerados no Contabil.
- Data e usuario da exportacao, quando disponivel.
- Razao das contas afetadas.

### Como corrigir

Identifique o lote anterior. Decida se deve excluir, estornar, manter ou ajustar manualmente conforme a rotina interna. Depois reexporte apenas os movimentos necessarios.

### Como validar

Confira se nao existe duplicidade no Contabil e se o saldo final bate com o Fiscal.

## Caso real: CFOP de venda usado em transferencia

### Sintoma

Fiscal e Contabil nao batem apos a integracao.

### Causa

Uma nota foi escriturada com CFOP de venda, mas a operacao correta era transferencia. Com isso, o Fiscal levou a nota para regra contabil de venda, gerando receita, cliente ou imposto de forma indevida.

### Correcao

1. Revisar o XML e confirmar a natureza real da operacao.
2. Conferir CFOP por item.
3. Revisar o codigo de operacao usado no Fiscal.
4. Conferir o lancamento automatico vinculado.
5. Ajustar a escrituracao conforme orientacao fiscal.
6. Controlar o lote contabil ja gerado.
7. Reexportar ou ajustar conforme a rotina interna.

### Prevencao

Criar checklist de CFOP antes da integracao, principalmente para notas de venda, transferencia, remessa, devolucao e bonificacao. Em notas com mais de um CFOP, conferir cada item antes de exportar.

## Checklist mestre de diagnostico

- Empresa correta?
- Competencia correta?
- Integracao habilitada no cadastro da empresa?
- Movimento ja foi exportado antes?
- Nota fiscal esta escriturada e ativa?
- Tipo de movimento foi selecionado na exportacao?
- CFOP representa a operacao real?
- Nota possui mais de um CFOP?
- Codigo de operacao esta correto?
- Lancamento automatico esta vinculado?
- Debito e credito estao preenchidos?
- Historico padrao esta correto?
- Cliente ou fornecedor tem vinculacao contabil?
- Impostos possuem parametrizacao contabil?
- Lote gerado fecha debito e credito?
- Valor integrado bate com relatorio fiscal?
- Razao contabil confirma a conta esperada?
