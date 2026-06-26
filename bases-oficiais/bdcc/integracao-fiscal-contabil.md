# Fontes oficiais - Integracao Fiscal x Contabil

Este arquivo centraliza as fontes oficiais ja mapeadas sobre Integracao Fiscal x Contabil. Ele registra links, resumos proprios e uso pratico dentro do agente, sem copiar o conteudo literal dos artigos oficiais.

## BDCC-IFC-001

**Titulo oficial:** Integracao Fiscal x Contabil: Tudo que voce precisa saber sobre Integracao Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-tudo-que-voce-precisa-saber-sobre-integracao-fiscalxcontabil-84260204.html

**Modulo:** Fiscal / Contabil

**Assunto:** Visao geral da Integracao Fiscal x Contabil

**Documento interno relacionado:** [README integracao](../../docs/integracao-fiscal-contabil/README.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte apresenta a integracao como conexao operacional entre Fiscal e Contabil, com foco em reduzir retrabalho e inconsistencias. Tambem diferencia formas de integracao, como online, lote e arquivo de texto. O artigo serve como base inicial para entender quais cadastros e parametrizacoes precisam estar prontos antes da exportacao.

**Uso pratico dentro do agente:**

Usar como referencia de visao geral quando o usuario perguntar o que e integracao, qual fluxo seguir ou por que Fiscal e Contabil precisam estar parametrizados juntos.

## BDCC-IFC-002

**Titulo oficial:** Integracao Fiscal x Contabil: Principais configuracoes no Fiscal para a Integracao Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-principais-configuracoes-no-fiscal-para-a-integracao-fiscal-x-contabil-184784013.html

**Modulo:** Fiscal

**Assunto:** Configuracoes no cadastro da empresa

**Documento interno relacionado:** [Configuracoes no Fiscal](../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte organiza os pontos de configuracao no Fiscal que permitem a integracao com o Contabil. O foco operacional esta em cadastro da empresa, habilitacao da integracao, CFOP, produto, codigo de operacao, guias e exportacao. E uma referencia importante para diagnosticar quando o movimento fiscal nao chega ao Contabil.

**Uso pratico dentro do agente:**

Usar para orientar conferencia de empresa, CFOP, codigo de operacao e lancamentos automaticos antes de reexportar movimentos.

## BDCC-IFC-003

**Titulo oficial:** Vinculacao Contabil - Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-vinculacao-contabil-220178968.html

**Modulo:** Fiscal / Contabil

**Assunto:** Vinculacao contabil de clientes e fornecedores

**Documento interno relacionado:** [Vinculacao contabil](../../docs/integracao-fiscal-contabil/vinculacao-contabil.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte trata da vinculacao entre clientes, fornecedores e contas contabeis dentro do Fiscal. O ponto central e definir se a conta sera usada para entrada, saida ou ambos. Essa parametrizacao ajuda a evitar que lancamentos integrados caiam em conta errada.

**Uso pratico dentro do agente:**

Usar em diagnosticos de cliente ou fornecedor caindo em conta incorreta, conciliacao com conta individual ou uso indevido de conta generica.

## BDCC-IFC-004

**Titulo oficial:** Como criar um lancamento automatico - Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-como-cadastrar-um-lancamento-automatico-37261453.html

**Modulo:** Contabil

**Assunto:** Cadastro de lancamento automatico

**Documento interno relacionado:** [Lancamentos automaticos](../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte mostra que o lancamento automatico precisa existir no Contabil e depois ser vinculado ao plano de contas. O cadastro envolve descricao, plano, chamadas devedora e credora e historico padrao. Esse ponto e essencial porque a integracao depende do lancamento automatico para formar o lote contabil.

**Uso pratico dentro do agente:**

Usar quando o problema indicar lote sem debito/credito, ausencia de lancamento ou movimento fiscal sem conta contabil definida.

## BDCC-IFC-005

**Titulo oficial:** Como criar um lancamento automatico - Contabil

**Link oficial:** https://ajuda.alterdata.com.br/bdcc/como-criar-um-lancamento-automatico-117662446.html

**Modulo:** Contabil

**Assunto:** Cadastro de lancamento automatico no Contabil

**Documento interno relacionado:** [Lancamentos automaticos](../../docs/integracao-fiscal-contabil/lancamentos-automaticos.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte reforca o cadastro do lancamento automatico pelo lado do Contabil. O procedimento destaca a criacao do cadastro e a configuracao das contas e do historico. E util para validar se o erro esta no cadastro contabil antes de revisar a nota fiscal.

**Uso pratico dentro do agente:**

Usar para orientar criacao ou revisao de lancamento automatico quando a parametrizacao fiscal aponta para codigo inexistente ou incompleto.

## BDCC-IFC-006

**Titulo oficial:** Integracao Online Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-integracao-online-fiscal-x-contabil-37261456.html

**Modulo:** Fiscal / Contabil

**Assunto:** Integracao online

**Documento interno relacionado:** [Exportacao para Contabil](../../docs/integracao-fiscal-contabil/exportacao-para-contabil.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte explica a configuracao para gerar integracao automatica entre Fiscal e Contabil. Ela relaciona habilitacao no cadastro da empresa, periodo inicial, tipo de movimento e conferencia do lote no Contabil. Tambem aponta que inconsistencias podem aparecer no gerenciamento da integracao.

**Uso pratico dentro do agente:**

Usar para diferenciar exportacao manual, lote, arquivo e integracao online, principalmente quando o usuario perguntar por movimentos integrados automaticamente.

## BDCC-IFC-007

**Titulo oficial:** Integracao Fiscal x Contabil: Como configurar o Fiscal para levar informacoes adicionais no historico

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-como-configurar-o-fiscal-para-levar-informacoes-adicionais-no-historico-73680242.html

**Modulo:** Fiscal

**Assunto:** Informacoes adicionais no historico da integracao

**Documento interno relacionado:** [Configuracoes no Fiscal](../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte trata da composicao do historico levado do Fiscal para o Contabil. O ponto pratico e configurar o historico padrao no Contabil e selecionar no Fiscal quais informacoes complementares devem acompanhar o lancamento. Isso ajuda a melhorar rastreabilidade sem transformar o historico em texto confuso.

**Uso pratico dentro do agente:**

Usar em problemas de historico incompleto, historico excessivo, identificacao de nota no razao e necessidade de rastrear fornecedor ou documento.

## BDCC-IFC-008

**Titulo oficial:** Integracao Fiscal x Contabil: Selecoes em Configuracoes Opcoes no Fiscal

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-selecoes-em-configuracoes-opcoes-no-fiscal-208372180.html

**Modulo:** Fiscal

**Assunto:** Configuracoes e opcoes de exportacao

**Documento interno relacionado:** [Configuracoes no Fiscal](../../docs/integracao-fiscal-contabil/configuracoes-no-fiscal.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte detalha opcoes de exportacao do Fiscal para o Contabil, incluindo configuracoes gerais, historicos, ISS tomador e impostos. Ela e relevante para entender por que certos valores sao abatidos, aglutinados ou levados com determinado lancamento automatico. Tambem ajuda a revisar parametros que afetam tributos e retencoes.

**Uso pratico dentro do agente:**

Usar quando houver divergencia de valor liquido, historico, ISS tomador, PIS/COFINS ou exportacao de impostos para o Contabil.

## BDCC-IFC-009

**Titulo oficial:** Configuracao de Notas de Servicos para Integracao Fiscal x Contabil

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/configuracao-de-notas-de-servicos-para-integracao-fiscal-x-contabil-37261396.html

**Modulo:** Fiscal / ISS

**Assunto:** Notas de servico e ISS tomador na integracao

**Documento interno relacionado:** [PIS COFINS ISS](../../docs/integracao-fiscal-contabil/pis-cofins-iss.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte concentra parametrizacoes de servicos para que notas prestadas ou tomadas sejam integradas corretamente. O foco operacional esta em codigo de operacao, lancamentos automaticos por imposto e configuracao de ISS tomador. E especialmente util para separar servico, retencao e impostos antes de gerar lote contabil.

**Uso pratico dentro do agente:**

Usar em diagnosticos de ISS proprio, ISS retido, notas de servico sem lancamento automatico ou divergencia entre servico fiscal e contabil.

## BDCC-IFC-010

**Titulo oficial:** Integracao Fiscal x Contabil: Nao foi possivel efetuar a integracao, o periodo escolhido nao possui movimento ou entao ja foi feita a integracao

**Link oficial:** https://ajuda.alterdata.com.br/fiscalbase/integracao-fiscal-x-contabil-nao-foi-possivel-efetuar-a-integracao-o-periodo-escolhido-nao-possui-movimento-ou-entao-ja-foi-feita-a-integracao-37261407.html

**Modulo:** Fiscal / Contabil

**Assunto:** Erro de integracao sem movimento ou ja integrada

**Documento interno relacionado:** [Troubleshooting](../../docs/integracao-fiscal-contabil/troubleshooting.md)

**Status:** Mapeado

**Data de consulta:** 2026-06-26

**Resumo proprio:**

A fonte aborda a mensagem de falha quando o periodo nao tem movimento apto ou quando a integracao ja ocorreu. A causa operacional pode estar em falta de lancamentos automaticos vinculados, periodo errado ou movimento ja marcado como exportado. O artigo orienta a conferir campos do movimento e atualizar vinculos antes de tentar novamente.

**Uso pratico dentro do agente:**

Usar no troubleshooting de lote nao gerado, movimento ausente na exportacao, competencia errada ou tentativa de reexportacao sem controle.
