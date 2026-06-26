# Padroes de Documentacao do Agente Alterdata

Este documento define o padrao de escrita do projeto. A base deve separar fonte oficial, procedimento interno e caso real resolvido, evitando misturar referencia oficial com interpretacao operacional.

## Tipos de documentos

### Procedimento operacional

Documento usado para orientar uma rotina executavel no escritorio.

Estrutura recomendada:

- Objetivo.
- Quando usar.
- Caminho no Alterdata.
- Pre-requisitos.
- Passo a passo.
- Conferencia.
- Erros comuns.
- Observacoes.

### Caso real

Documento usado para registrar um problema resolvido, sempre anonimizado.

Estrutura recomendada:

- Problema.
- Sintoma.
- Diagnostico.
- Causa.
- Correcao.
- Conferencia.
- Resultado.
- Prevencao.

### Fonte oficial

Documento usado para registrar referencia oficial sem copiar conteudo literal.

Estrutura recomendada:

- Link oficial.
- Resumo proprio.
- Observacao pratica.
- Relacao com documentos internos.

### Troubleshooting

Documento usado para diagnosticar erro ou divergencia recorrente.

Estrutura recomendada:

- Sintoma.
- Causa provavel.
- Onde verificar.
- Como corrigir.
- Como validar.
- Links internos.

### Checklist

Documento usado para conferir uma rotina antes ou depois de executar uma acao.

Estrutura recomendada:

- Contexto.
- Itens de conferencia.
- Resultado esperado.
- Responsavel ou rotina relacionada, quando aplicavel.

### Prompt de especialista

Documento usado para orientar uma IA especializada em um modulo ou rotina.

Estrutura recomendada:

- Papel da IA.
- Escopo.
- Forma de resposta.
- Regras de seguranca.
- Criterios de diagnostico.

## Regra de seguranca

- Nunca usar dados reais.
- Anonimizar cliente.
- Nao salvar XML real.
- Nao salvar CNPJ completo.
- Nao salvar certificado, senha, token ou backup.
- Nao salvar arquivo fiscal, banco de dados ou relatorio identificavel.

## Tom de escrita

- Direto.
- Operacional.
- Linguagem de escritorio contabil.
- Foco em diagnostico e correcao.
- Separar fato observado, causa provavel, caminho no Alterdata e conferencia.
- Evitar linguagem juridica quando o objetivo for procedimento interno.
- Quando depender de regra tributaria, deixar claro que a validacao depende do regime, municipio, operacao e parametrizacao.

## Como separar os tipos de conhecimento

- Conhecimento oficial Alterdata: registrar link, titulo, modulo, data de consulta e resumo proprio.
- Procedimento interno do escritorio: registrar passo a passo operacional e conferencia.
- Caso real resolvido: registrar sintoma, causa, correcao e prevencao, sempre sem dados sensiveis.
