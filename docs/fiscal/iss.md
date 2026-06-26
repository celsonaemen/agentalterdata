# Conferencia Operacional de ISS no Alterdata

ISS depende da nota de servico, municipio, codigo de servico, retencao e parametrizacao da empresa. O tratamento fiscal e contabil pode variar conforme municipio, tipo de servico, tomador, prestador e regra interna do escritorio.

Use este procedimento para conferir ISS antes da integracao ou antes de concluir que existe diferenca no Contabil.

## ISS proprio x ISS retido

ISS proprio e o imposto devido pelo prestador, quando aplicavel conforme a operacao e a parametrizacao da empresa.

ISS retido e o imposto retido pelo tomador ou destacado conforme regra da operacao. Ele pode ter tratamento contabil diferente do ISS proprio.

Sempre separe ISS proprio de ISS retido antes de somar valores por competencia.

## Onde conferir

- Movimento de servicos.
- Nota de servico.
- Codigo de servico.
- Municipio.
- Tomador ou prestador.
- Retencao.
- Apuracao de ISS.
- Parametrizacao fiscal da empresa.
- Integracao Fiscal x Contabil.

## Erros comuns

- Codigo de servico incorreto.
- Municipio incorreto.
- ISS retido nao marcado.
- ISS proprio tratado como retido.
- ISS retido tratado como proprio.
- Retencao sem conta contabil.
- Servico sem lancamento automatico.
- Nota de servico fora da competencia.
- Lote contabil gerado antes da correcao fiscal.

## Impacto no Contabil

ISS pode impactar contas de imposto a recolher, retencoes, despesa, receita ou contas transitorias, conforme a rotina da empresa.

Na conferencia contabil, verifique:

- Conta de ISS a recolher.
- Conta de ISS retido.
- Conta de receita ou despesa vinculada ao servico.
- Historico do lancamento.
- Valor por competencia.
- Lote gerado na integracao.

Se o ISS retido nao estiver parametrizado, o lote pode sair sem lancamento esperado ou cair em conta incorreta.

## Como validar

1. Confira empresa e competencia.
2. Gere relatorio de servicos ou apuracao de ISS.
3. Separe ISS proprio e ISS retido.
4. Confira municipio e codigo de servico.
5. Verifique se a retencao esta marcada quando aplicavel.
6. Compare o valor fiscal com o lote contabil.
7. Confira o razao da conta de ISS.
8. Investigue diferenca por nota de servico antes de ajustar o Contabil.

## Checklist de ISS antes de integrar

- A nota e de servico?
- O municipio esta correto?
- O codigo de servico esta correto?
- O tomador/prestador esta correto?
- Existe ISS proprio?
- Existe ISS retido?
- A retencao esta marcada corretamente?
- A conta contabil esta parametrizada?
- O lancamento automatico esta vinculado?
- A competencia esta correta?
- O valor bate com a apuracao?
