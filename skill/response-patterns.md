# Padroes de Resposta da Skill Alterdata

Use estes modelos para manter respostas consistentes e operacionais.

## Problema de divergencia Fiscal x Contabil

### Diagnostico

Informar o sintoma e a primeira hipotese operacional.

### Causas provaveis

Listar causas como competencia errada, nota nao integrada, CFOP incorreto, reexportacao, lote duplicado, imposto sem parametro ou conta errada.

### Onde verificar no Alterdata

Indicar Fiscal, movimento de notas, exportacao, lote contabil, razao e balancete.

### Correcao

Orientar corrigir a origem antes de mexer no lote, tratar lote anterior e reintegrar quando necessario.

### Conferencia

Comparar relatorio fiscal, lote, razao e balancete.

### Prevencao

Usar checklist mensal e documentar recorrencias.

## Problema com CFOP

### Natureza da operacao

Confirmar se e venda, compra, transferencia, devolucao, remessa ou outra rotina.

### CFOP informado

Analisar o CFOP usado, sem afirmar regra legal sem validacao.

### CFOP esperado, quando for possivel orientar genericamente

Indicar que o CFOP esperado depende da operacao real, UF, entrada/saida e orientacao fiscal.

### Codigo de operacao

Conferir se o codigo de operacao acompanha a natureza correta.

### Impacto no Fiscal

Apontar reflexo em relatorios, impostos e classificacao da nota.

### Impacto no Contabil

Apontar reflexo em conta, historico, receita, estoque, imposto ou lote.

### Como corrigir

Corrigir a classificacao fiscal conforme procedimento interno e controlar o lote ja gerado.

### Como validar

Conferir nota, relatorio fiscal, lote contabil e razao.

## Problema com PIS/COFINS

### Separar PIS/COFINS proprio e retido

Nunca misturar imposto proprio com retencao sem validar o relatorio.

### Conferir competencia

Verificar se as notas pertencem ao periodo analisado.

### Conferir CST, base, aliquota e valor

Checar itens da nota e apuracao.

### Conferir apuracao

Comparar relatorio fiscal com a apuracao.

### Conferir integracao contabil

Verificar lancamento automatico, conta contabil e lote.

### Conferir razao

Comparar contas de PIS/COFINS no Contabil.

## Problema com ISS

### Separar ISS proprio e retido

Identificar se o imposto e devido pelo prestador ou retido pelo tomador.

### Conferir nota de servico

Validar competencia e natureza do servico.

### Conferir codigo de servico

Confirmar codigo usado no Fiscal.

### Conferir municipio

Validar municipio relacionado a operacao.

### Conferir tomador/prestador

Confirmar papel de cada parte na nota.

### Conferir integracao

Verificar parametros e lancamentos automaticos.

### Conferir contas contabeis

Validar contas de ISS proprio, ISS retido, receita ou despesa.

## Analise de print

### O que aparece na tela

Descrever apenas o que estiver visivel ou informado pelo usuario.

### O que essa tela controla

Explicar a funcao operacional da tela.

### O que esta correto

Apontar configuracoes coerentes.

### O que merece atencao

Apontar campos que precisam de conferencia.

### Proximo passo recomendado

Indicar a proxima verificacao no Alterdata.

## Analise de relatorio

### Identificar colunas

Separar competencia, documento, base, imposto, valor e conta.

### Separar por competencia

Evitar concluir por total anual sem soma mensal.

### Separar impostos

Distinguir PIS, COFINS, ISS, ICMS, proprio e retido.

### Somar valores

Totalizar por mes e por tipo de imposto.

### Comparar Fiscal x Contabil

Comparar com lote, razao e balancete.

### Apontar divergencias

Localizar diferenca por nota, CFOP, imposto ou conta.

### Indicar ajuste

Orientar corrigir origem e reintegrar quando necessario.
