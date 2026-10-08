# Integração do AURA em aplicações web

O pacote de referência está em `../assets/design-system/`, relativo a este arquivo. Os estilos e assets usados no produto devem fazer parte do próprio projeto; a aplicação não deve depender do caminho pessoal onde a skill está instalada.

## HTML com JavaScript

Copie o CSS, a Manrope e a licença preservando esta relação de caminhos:

```text
assets/aura/
  aura.css
  fontes-aura/
    manrope-variable.ttf
    manrope-OFL.txt
```

Acrescente `aura.js` quando usar suas interações. O script funciona no navegador e inicializa a marcação documentada em [aura-interacoes.md](aura-interacoes.md). Pode ser carregado com `defer`; `Aura.init(root)` também inicializa conteúdo inserido depois.

```html
<link rel="stylesheet" href="./assets/aura/aura.css">
<script src="./assets/aura/aura.js" defer></script>
```

Os dados e as simulações da prévia são exemplos. Ligue formulários, progresso, upload e ações aos comportamentos reais do produto. A prévia completa e o comparativo tipográfico servem como catálogo; não são páginas obrigatórias do app.

O campo de senha do catálogo demonstra o controle com um valor de exemplo. Ao usá-lo em login, remova esse valor e use `autocomplete="current-password"`; em cadastro, use `new-password`. Adapte os campos ao fluxo real de autenticação.

## React, Vue e componentes com estado próprio

Reutilize o CSS, os tokens, os nomes de classes e os elementos semânticos quando forem compatíveis com a arquitetura existente. Adapte os exemplos para a API dos componentes do projeto.

O `aura.js` modifica o DOM diretamente, incluindo `value`, `checked`, `hidden` e estados de acessibilidade. Em componentes controlados, implemente esses comportamentos com o estado e os eventos do framework para evitar dois responsáveis pelo mesmo estado. O script continua útil como referência de comportamento.

Em renderização no servidor, mantenha acesso a `window`, `document` e `localStorage` no cliente. Integre fonte e assets pelo mecanismo existente do projeto. Se já houver uma biblioteca de componentes acessível, aplique os tokens e variantes AURA nela quando isso preservar melhor os fluxos do produto.

## Temas e persistência

O CSS usa `data-aura-theme="light"` ou `data-aura-theme="dark"` no elemento `html`, com `color-scheme` correspondente. Na integração JavaScript fornecida:

- `Aura.setTheme('light')` e `Aura.setTheme('dark')` aplicam e salvam a preferência.
- A chave de armazenamento é `aura-theme`. Uma preferência válida salva prevalece sobre o atributo inicial.
- O botão `data-aura-theme-toggle` alterna os modos; seu filho `data-aura-theme-label` exibe a próxima opção.
- `aria-label="Modo escuro"` permanece estável e `aria-pressed` indica se o modo está ativo. O texto visível que muda pode usar `aria-hidden="true"`.
- `document` emite `aura:themechange`, com o valor em `event.detail.theme`.

Em um projeto com gerenciador de tema próprio, mantenha esse gerenciador como responsável pela preferência e mapeie seus modos para os tokens AURA. Evite instalar uma segunda lógica de persistência. Preserve o tema inicial e a hidratação adotados pelo projeto; quando necessário, aplique a preferência antes da primeira pintura.

## Migração parcial e atualização

`aura.css` aplica fonte e cores no `html`, medidas no `body`, `box-sizing` global e herança de fonte nos controles. Avalie essas regras antes de importá-lo em um produto existente. Para alterar uma tela isolada, adapte os tokens e regras ao contêiner da tela, ou use a infraestrutura de estilos do projeto. O seletor de dark deve acompanhar o mesmo escopo.

Os mapas `themes.light` e `themes.dark` em `aura-tokens.json` contêm nomes de variáveis CSS e valores, inclusive URLs de SVG e sombras. Preserve os valores completos; o campo `color` no topo registra a paleta clara original, enquanto os mapas de tema contêm as cores e efeitos por modo.

Atualizações podem ser comparadas com a versão local do AURA. Preserve alterações do produto e distribua a nova versão de forma deliberada, em vez de sobrescrever arquivos customizados durante uma tarefa de tela.
