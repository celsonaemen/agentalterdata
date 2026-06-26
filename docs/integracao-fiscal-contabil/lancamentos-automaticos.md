# Lancamentos Automaticos na Integracao Fiscal x Contabil

Os lancamentos automaticos sao cadastrados no Contabil e utilizados pelo Fiscal para gerar os lancamentos contabeis a partir dos movimentos fiscais. Eles definem a estrutura contabil que sera usada na integracao: contas, historico, chamadas e, quando aplicavel, centro de custos.

## Caminho no Contabil

`Contabil > Cadastros > Lancamentos Automaticos`

## Campos importantes

- Descricao: nome interno do lancamento automatico. Deve indicar claramente a operacao.
- Plano de contas: plano usado pela empresa integrada.
- Chamada devedora: conta que recebera o debito.
- Chamada credora: conta que recebera o credito.
- Historico padrao: texto ou modelo de historico levado para o lancamento contabil.
- Centro de custos: usar quando a empresa trabalha com centro de custo e a rotina exige essa separacao.

Um lancamento automatico errado pode gerar contabilizacao errada, lote com diferenca entre debito e credito ou ausencia de lancamento no Contabil.

## Exemplos genericos

### Compra de mercadoria

- Debito: estoque, compras ou despesa, conforme a rotina da empresa.
- Credito: fornecedores a pagar ou conta do fornecedor.
- Conferir: CFOP de entrada, fornecedor, imposto recuperavel e valor contabil.

### Venda de mercadoria

- Debito: clientes a receber ou conta do cliente.
- Credito: receita de venda.
- Conferir: CFOP de saida, cliente, receita, impostos incidentes e valor total da nota.

### ISS tomado

- Debito: despesa ou servico tomado.
- Credito: fornecedor ou impostos a recolher, conforme parametrizacao.
- Conferir: retencao, municipio, codigo de servico, base e aliquota.

### PIS/COFINS

- Debito ou credito: depende se a rotina trata credito, debito fiscal, receita ou imposto a recolher.
- Conferir: CST, base, aliquota, acumulador e reflexo no SPED.

### ICMS a recuperar

- Debito: ICMS a recuperar.
- Credito: fornecedor, estoque ou conta intermediaria, conforme a rotina.
- Conferir: CFOP, CST/CSOSN, base e valor destacado.

### ICMS a recolher

- Debito: despesa tributaria, imposto sobre vendas ou conta de apuracao.
- Credito: ICMS a recolher.
- Conferir: apuracao fiscal, valor do imposto e periodo de competencia.

## Como conferir

1. Identifique a nota ou movimento que gerou o lancamento.
2. Confira qual lancamento automatico foi usado.
3. Verifique chamada devedora, chamada credora e historico.
4. Compare valor fiscal com valor contabil gerado.
5. Confira se o lote fechou debito e credito.
6. Analise o razao das contas afetadas.
7. Se houver erro, corrija a parametrizacao e reexporte somente depois de controlar o que ja foi integrado.

## Erros comuns

- Chamada devedora vazia ou incorreta.
- Chamada credora vazia ou incorreta.
- Plano de contas diferente do usado pela empresa.
- Historico padrao inexistente ou inadequado.
- Lancamento automatico de venda usado em transferencia.
- Lancamento automatico de compra usado para servico.
- Conta de cliente ou fornecedor generica usada quando deveria ser individual.
- Centro de custo obrigatorio nao informado.

## Boas praticas

- Usar descricao objetiva para cada lancamento automatico.
- Separar lancamentos por tipo de operacao.
- Revisar lancamentos automaticos antes do fechamento mensal.
- Evitar reaproveitar lancamento automatico sem conferir debito, credito e historico.
- Documentar o motivo de cada conta usada.
- Conferir notas com mais de um CFOP antes da integracao.
- Testar a parametrizacao com uma competencia controlada antes de aplicar em volume.
