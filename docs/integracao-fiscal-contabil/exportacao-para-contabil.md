# Exportacao dos Movimentos do Fiscal para o Contabil

Depois das parametrizacoes, os movimentos fiscais podem ser exportados para o Contabil. Essa etapa leva os lancamentos gerados a partir das notas fiscais para conferencia e fechamento contabil.

## Caminho no Alterdata

`Fiscal > Contabil > Exportar para o Contabil`

## Fluxo de exportacao

1. Selecionar a empresa.
2. Avancar.
3. Selecionar referencia ou competencia.
4. Selecionar tipo de movimento.
5. Conferir as opcoes da exportacao.
6. Gerar lote ou arquivo TXT.
7. Importar ou conferir no Contabil.
8. Validar debito, credito, historico, contas e valores.

## Exportacao direta

Na exportacao direta, o Fiscal envia os movimentos para o Contabil sem depender de arquivo intermediario. E o fluxo mais pratico quando os sistemas estao preparados para trabalhar integrados.

Conferir antes:

- Empresa correta.
- Competencia correta.
- Movimentos selecionados corretamente.
- Parametros de integracao revisados.
- Lotes anteriores controlados.

## Exportacao por arquivo TXT

Na exportacao por arquivo TXT, o Fiscal gera um arquivo para posterior importacao no Contabil. Esse fluxo e util quando ha necessidade de conferencia intermediaria, transferencia entre ambientes ou rotina especifica do escritorio.

Cuidados:

- Salvar o arquivo em pasta controlada.
- Evitar sobrescrever arquivos de competencia anterior.
- Conferir empresa e competencia no nome ou controle interno.
- Importar no Contabil correto.
- Guardar evidencia apenas quando nao houver dados sensiveis ou quando o arquivo estiver em local seguro interno.

## O que conferir antes de exportar

- Empresa e competencia.
- Notas fiscais escrituradas.
- Notas canceladas, inutilizadas ou denegadas, quando aplicavel.
- CFOP e codigo de operacao.
- CST/CSOSN e impostos.
- Clientes e fornecedores.
- Lancamentos automaticos.
- Historicos padroes.
- Parametros de integracao.
- Movimentos ja exportados.

## O que conferir depois de exportar

- Lote gerado no Contabil.
- Total de debitos e creditos.
- Contas contabeis usadas.
- Historicos gerados.
- Datas dos lancamentos.
- Valores por nota, CFOP e imposto.
- Razao das contas afetadas.
- Comparacao com relatorios fiscais.

## Quando reexportar

Reexporte somente quando a causa da divergencia estiver identificada e corrigida.

Casos comuns:

- Nota fiscal corrigida no Fiscal.
- CFOP ou codigo de operacao ajustado.
- Lancamento automatico corrigido.
- Vinculacao contabil corrigida.
- Historico padrao ajustado.
- Movimento exportado com competencia errada.
- Lote anterior excluido ou estornado de forma controlada.

Antes de reexportar, confirme se o lote anterior deve ser excluido, estornado ou mantido com ajuste manual. Evite gerar duplicidade no Contabil.
