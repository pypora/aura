---
name: aura
description: "Aplicar o design system AURA a interfaces web, componentes e telas existentes, com Manrope, cinzas neutros, light/dark mode e neon branco minimalista. Use quando o usuário escolher a identidade AURA."
license: MIT
---

# AURA

Implemente a identidade AURA na tela ou no componente solicitado. Preserve os fluxos e as funcionalidades do produto, adaptando o sistema à tecnologia do projeto. Esta skill contém a biblioteca AURA **0.5.1** e funciona sem depender do chat em que ela foi criada.

## Fontes de referência

Resolva os caminhos abaixo a partir da pasta desta skill.

- Leia o [guia visual](references/aura-guia.md) para as regras de composição, medidas e temas.
- Consulte [assets/design-system/aura-tokens.json](assets/design-system/aura-tokens.json) e as regras relevantes de [aura.css](assets/design-system/aura.css) para os valores e estados exatos.
- Use a [prévia de componentes](assets/design-system/aura-preview.html) como catálogo visual e fonte de marcação; copie apenas os componentes necessários à tarefa.
- Leia [integração por tecnologia](references/integracao.md) ao integrar ou migrar um projeto. Leia o [guia de interações](references/aura-interacoes.md) quando a tarefa envolver comportamento ou seleção de tema.

## Aplicação no projeto

1. Identifique o framework, os componentes, os estilos e o mecanismo de temas existentes. Se o projeto já tiver AURA, use sua implementação como ponto de partida e compare com esta versão antes de atualizar arquivos. Preserve adaptações do produto e siga as escolhas explícitas do usuário.
2. Integre os tokens, a fonte e os componentes no escopo solicitado. Em uma aplicação HTML, reutilize o CSS e o JavaScript necessários. Em React, Vue ou outra biblioteca com estado próprio, use os mesmos tokens e a marcação como referência para componentes e comportamentos do framework.
3. Carregue a Manrope localmente e inclua sua licença. O CSS resolve `fontes-aura/manrope-variable.ttf` em relação à sua própria localização; ajuste esse caminho se o bundler mover os assets. DM Sans e Inter pertencem somente ao comparativo histórico.
4. Aplique a hierarquia do produto com os tokens compartilhados. Os componentes base e suas variantes neon devem manter a mesma geometria. Ao precisar de um componente novo, derive suas medidas e estados dos componentes próximos do catálogo.
5. Confira a tela em ambos os temas e em larguras relevantes. Verifique fonte carregada, alinhamento, conteúdo longo, foco de teclado e estados usados na tarefa. Use renderização real quando disponível; diferencie inspeção visual de verificações de DOM, código ou contraste numérico. Execute os comandos de validação pertinentes do projeto.

O CSS fornecido inclui regras globais para `html`, `body` e controles. Em uma migração parcial, adapte seu escopo ao projeto para que a aplicação do AURA permaneça restrita às áreas solicitadas. A skill não autoriza uma reformulação de todo o produto ou uma publicação.

## Decisões visuais do AURA

- **Identidade:** luz branca sobre cinza neutro, minimalismo, espaço livre e hierarquia clara. A assinatura vem da luz; nenhuma forma geométrica especial é obrigatória.
- **Base acromática:** use cinzas com **R=G=B** nos dois temas. Fundos, textos, bordas, foco, overlays, sombras, tabelas, carrosséis e avatares seguem essa regra. Preserve as cores de sucesso, erro e aviso exclusivamente nos estados semânticos. Ao ampliar a paleta base, altere a luminosidade mantendo os três canais iguais.
- **Fonte oficial:** Manrope em títulos, textos e componentes. Use os pesos **400 / 500 / 600 / 700**, seguindo seus papéis no guia.
- **Tipografia:** corpo **16 px**, controles **14 px**, ajuda **12 px** com base de 16 px. Preserve os tamanhos em `rem` e a escala de títulos definida nos tokens.
- **Controles:** altura mínima padrão **48 px** e compacta **44 px**. Textareas, seleções múltiplas e escolhas com várias linhas crescem com o conteúdo. Ícones comuns usam **20 px**.
- **Raios por função:** **8 px** em elementos internos, **12 px** em controles, **16 px** em superfícies e **24 px** em painéis. Cápsulas e círculos seguem as exceções do catálogo. Use os tokens de raio também nas variantes e no mobile.
- **Espaços:** ritmo em múltiplos de 4 px, por meio dos tokens compartilhados. Diferencie espaçamento de composição das dimensões fixas dos controles.
- **Temas:** light é o padrão; dark troca cores e efeitos mantendo a mesma tipografia e geometria. Reutilize `themes.light` e `themes.dark` do JSON ou os seletores de tema do CSS, conforme a integração do projeto.
- **Cores semânticas:** use `--aura-action` com `--aura-on-action`. Sobre preenchimento neon branco, use `--aura-on-neon`. Preserve os pares de texto, fundo, borda e foco nos estados de sucesso, aviso e erro.
- **Neon:** use um ponto focal por área, com as variantes já fornecidas. O halo é decorativo, sem animação contínua; as opacidades são menores no dark. Preserve legibilidade e identificação de foco/seleção sem depender do brilho.

## Ao entregar

Informe quais partes receberam AURA, como os arquivos e temas foram integrados e o que foi verificado. Diferencie limitações reais de validações concluídas. Preserve os tokens e as decisões como fonte comum para futuras telas do projeto.
