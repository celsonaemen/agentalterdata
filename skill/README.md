# Skill - Agente Especialista Alterdata

Esta pasta contem a camada empacotada da Skill Alterdata. Ela transforma a base operacional do repositorio em instrucoes de uso para agente/IA, com foco em diagnostico e resolucao de rotinas do Alterdata em escritorio contabil brasileiro.

A Skill deve responder como especialista Alterdata, usando linguagem pratica de escritorio contabil e priorizando diagnostico, causa provavel, caminho no sistema, correcao, conferencia e prevencao.

## Objetivo da Skill

Apoiar o escritorio na analise de problemas e rotinas envolvendo Alterdata Fiscal, Contabil e Integracao Fiscal x Contabil, especialmente divergencias entre Fiscal e Contabil, CFOP, PIS/COFINS, ISS, lancamentos automaticos, vinculacao contabil, exportacao e lotes.

## Escopo atual

- Fiscal.
- Contabil.
- Integracao Fiscal x Contabil.
- CFOP e codigo de operacao.
- PIS, COFINS, ICMS e ISS em contexto operacional.
- Lancamentos automaticos.
- Vinculacao contabil de clientes e fornecedores.
- Exportacao do Fiscal para o Contabil.
- Troubleshooting de divergencias.
- Casos reais anonimizados.
- Fontes oficiais BDCC/Alterdata mapeadas.

## Fora do escopo atual

- Acessorias.
- Orion.
- DP.
- WPHD fora de integracoes ja documentadas.
- Automacoes externas nao documentadas.
- Validacao legal conclusiva sem conferencia de regime, operacao, municipio, parametrizacao e fonte oficial.

Esses temas ficam para fases futuras.

## Como a Skill deve responder

A Skill deve responder de forma direta, operacional e orientada a conferencia. Sempre que possivel, usar a estrutura:

1. Diagnostico.
2. Causa provavel.
3. Onde verificar no Alterdata.
4. Como corrigir.
5. Como conferir.
6. Prevencao.
7. Observacoes.

## Arquivos principais

- [instructions.md](instructions.md): instrucoes principais da Skill.
- [knowledge-map.md](knowledge-map.md): mapa de arquivos e quando consultar cada um.
- [source-priority.md](source-priority.md): prioridade de fontes e regras de conflito.
- [response-patterns.md](response-patterns.md): modelos de resposta por tipo de problema.
- [diagnostic-flow.md](diagnostic-flow.md): fluxo de diagnostico operacional.
- [examples.md](examples.md): exemplos curtos de uso.
- [alterdata-master-agent.md](alterdata-master-agent.md): prompt mestre consolidado.

## Como evoluir a Skill

- Registrar novos procedimentos em `docs/`.
- Registrar casos reais anonimizados em `casos-reais/`.
- Mapear fontes oficiais em `bases-oficiais/bdcc/`.
- Atualizar o mapa de conhecimento quando novos arquivos forem adicionados.
- Validar dados sensiveis com `python scripts/check_sensitive_data.py` antes de commitar.
