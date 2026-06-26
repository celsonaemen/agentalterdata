# PIS, COFINS e ISS na Integracao Fiscal x Contabil

PIS, COFINS e ISS podem impactar a integracao contabil quando existe apuracao, retencao, lancamento automatico ou parametrizacao vinculada a nota fiscal. A conferencia precisa separar o que e imposto proprio, o que e retencao e o que deve ou nao gerar reflexo contabil.

O tratamento depende do regime tributario, municipio, tipo de operacao, cadastro da empresa e parametrizacao do Alterdata. Nao trate todo valor destacado como saldo a recolher sem conferir a origem.

## Separacao obrigatoria

Antes de integrar ou lancar no Contabil, separe:

- PIS proprio.
- COFINS proprio.
- PIS retido.
- COFINS retido.
- ISS proprio.
- ISS retido.

Essa separacao evita misturar imposto apurado pela empresa com imposto retido por terceiros ou compensavel em outra rotina.

## Onde conferir no Alterdata

- `Fiscal > Relatorios > Impostos`
- `Fiscal > Apuracao`
- `Fiscal > Movimento de Notas`
- `Fiscal > Integracao Contabil`
- `Contabil > Lotes`
- `Contabil > Razao`

## Impacto na Contabilidade

Dependendo da rotina da empresa, PIS, COFINS e ISS podem gerar ou afetar:

- PIS a recolher.
- COFINS a recolher.
- ISS a recolher.
- Tributos retidos a recuperar ou compensar.
- Despesa ou receita conforme natureza da operacao.
- Contas de impostos incidentes sobre venda ou servico.
- Contas de retencoes sofridas ou efetuadas.

Exemplos operacionais:

- PIS proprio apurado pode ser conferido contra conta de PIS a recolher.
- COFINS proprio apurado pode ser conferido contra conta de COFINS a recolher.
- ISS proprio pode ser conferido contra conta de ISS a recolher.
- PIS/COFINS/ISS retidos podem precisar de conta diferente de imposto proprio.
- Servico tomado ou prestado pode afetar despesa, receita, imposto ou retencao conforme parametrizacao.

## Principais causas de divergencia

- Nota sem CST correto.
- Codigo de operacao errado.
- CFOP incompativel.
- Servico sem codigo de servico ou tributacao municipal correta.
- ISS retido nao parametrizado.
- PIS/COFINS retido confundido com imposto proprio.
- Lancamento automatico sem conta contabil.
- Lote ja exportado antes da correcao.
- Nota fora da competencia.
- Valor ajustado no Fiscal depois da integracao, sem tratamento no Contabil.
- Retencao informada na nota, mas sem reflexo na integracao.

## Checklist de conferencia antes da integracao

- Empresa e competencia corretas.
- Regime tributario conferido para a rotina analisada.
- Notas de entrada, saida e servico revisadas.
- CST de PIS/COFINS conferido.
- Base de calculo e aliquota conferidas.
- PIS proprio separado de PIS retido.
- COFINS proprio separado de COFINS retido.
- ISS proprio separado de ISS retido.
- Codigo de servico e municipio conferidos para ISS.
- Codigo de operacao e CFOP revisados.
- Lancamentos automaticos com contas contabeis preenchidas.
- Relatorio fiscal ou apuracao fechado antes de exportar.

## Checklist de conferencia depois da integracao

- Lote gerado no Contabil localizado.
- Total de debito e credito conferido.
- Contas de PIS, COFINS e ISS revisadas no razao.
- Historicos dos lancamentos conferidos.
- Valores integrados comparados com relatorios fiscais.
- Retencoes conferidas em contas separadas, quando aplicavel.
- Ajustes manuais identificados antes de concluir a diferenca.
- Duplicidade de exportacao descartada.

## Quando reexportar

Reexporte somente depois de identificar a causa da divergencia e decidir o tratamento do lote anterior.

Reexportacao pode ser necessaria quando:

- CST foi corrigido.
- Codigo de operacao foi ajustado.
- Parametrizacao de PIS/COFINS foi corrigida.
- Retencao foi marcada ou desmarcada corretamente.
- Codigo de servico ou municipio foi corrigido.
- Lancamento automatico recebeu conta contabil correta.
- Lote anterior foi excluido ou estornado conforme politica do escritorio.

## Boas praticas

- Conferir PIS, COFINS e ISS mensalmente antes da integracao.
- Separar imposto proprio de imposto retido em todos os relatorios.
- Evitar ajustar somente o Contabil quando a origem do erro esta no Fiscal.
- Documentar parametrizacoes especiais por empresa.
- Manter lancamentos automaticos separados para imposto proprio e retencao, quando a rotina exigir.
- Conferir servicos com ISS retido antes do fechamento.
- Validar valores anuais por soma mensal, nao apenas pelo total consolidado.

## Links relacionados

- [Conferencia Operacional de PIS e COFINS](../fiscal/pis-cofins.md)
- [Conferencia Operacional de ISS](../fiscal/iss.md)
- [Caso 002 - Conferencia de PIS e COFINS para lancamento no Alterdata](../../casos-reais/pis-cofins/caso-002-conferencia-pis-cofins.md)
