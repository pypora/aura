# AURA — interações web

**Versão:** biblioteca 0.5.1 · **Modos:** claro e escuro

Use os estilos e o script em conjunto. O JavaScript funciona sem frameworks e inicializa os componentes quando o documento está pronto.

A fonte oficial é **Manrope**. Mantenha `fontes-aura/manrope-variable.ttf` e `fontes-aura/manrope-OFL.txt` na pasta `fontes-aura`, ao lado de `aura.css`. O CSS carrega a fonte localmente; o [guia do sistema](./aura-guia.md) detalha a instalação e a escala tipográfica.

```html
<link rel="stylesheet" href="./aura.css">
<script src="./aura.js" defer></script>
```

Após inserir novos componentes em uma aplicação, inicialize o elemento que os contém:

```js
window.Aura.init(document.getElementById("nova-secao"));
```

Você pode chamar `Aura.init()` repetidamente: os mesmos elementos não recebem eventos duplicados. IDs de controles, painéis, diálogos e outputs devem ser únicos no documento.

## Alternância de tema

O modo claro é o padrão quando não há preferência salva nem atributo inicial `dark`. Para declarar o modo escuro inicial no HTML, use:

```html
<html lang="pt-BR" data-aura-theme="dark">
```

Um botão com `data-aura-theme-toggle` alterna entre claro e escuro. O filho `data-aura-theme-label` recebe o nome da próxima opção:

```html
<button type="button" class="aura-button aura-button--secondary"
  data-aura-theme-toggle aria-label="Modo escuro" aria-pressed="false">
  <span data-aura-theme-label aria-hidden="true">Modo escuro</span>
</button>
```

O script sincroniza todos os alternadores inicializados: `aria-pressed="true"` indica que o modo escuro está ativo; `aria-label="Modo escuro"` permanece estável; o texto visível descreve a próxima opção. Para alternadores adicionados depois, chame `Aura.init(container)` como nos demais componentes.

Após o carregamento de `aura.js`, a API permite escolher o tema diretamente:

```js
window.Aura.setTheme('dark');
window.Aura.setTheme('light');
```

Cada chamada aplica `data-aura-theme` ao elemento `html`, atualiza os alternadores e salva `light` ou `dark` no `localStorage`, na chave `aura-theme`. Na inicialização, uma preferência salva válida prevalece sobre o atributo declarado no HTML. Sem preferência, vale o atributo; sem o atributo `dark`, vale o modo claro. A página continua operando se o navegador bloquear o armazenamento.

Para acompanhar o tema em gráficos ou em outros elementos da aplicação, escute o evento no documento:

```js
document.addEventListener('aura:themechange', function (event) {
  const temaAtual = event.detail.theme; // 'light' ou 'dark'
  // Atualize aqui os elementos da aplicação que dependem do tema.
});
```

`Aura.setTheme()` dispara o evento ao aplicar o tema; a inicialização também o dispara quando altera o atributo inicial. O tema modifica cores, `color-scheme`, sombras e intensidade do halo. Manrope, tipografia, alturas, raios e espaçamentos são compartilhados.

Em `aura-tokens.json`, `themes.light` e `themes.dark` mapeiam variáveis CSS, como `--aura-canvas`, para os valores de cada tema. Os tokens compartilhados ficam nos demais campos do JSON. O [guia do sistema](./aura-guia.md) apresenta a paleta dos dois modos e as regras de uso do neon.

## Componentes e atributos

| Componente | Marcação necessária | Comportamento |
| --- | --- | --- |
| Tema | Botão `data-aura-theme-toggle` com filho `data-aura-theme-label`; atributo `data-aura-theme` no elemento `html` | Alterna claro/escuro, atualiza acessibilidade, salva `aura-theme` localmente e emite `aura:themechange`. |
| Slider | `input[type="range"][data-aura-range]`, `data-output="id-do-output"`, `data-suffix="%"` opcional | Atualiza o output e a variável CSS `--range-percent` ao mover o controle. |
| Tabs | Container `data-aura-tabs`; botões `role="tab"` dentro de `role="tablist"`; `aria-controls` com o ID de cada painel `role="tabpanel"` | Clique, setas, Home e End selecionam uma aba e mostram seu painel. `aria-selected`, `tabindex` e `hidden` acompanham a seleção. |
| Stepper | Container `data-aura-stepper` com `input[type="number"]` e botões `data-step="down"` / `data-step="up"` | Respeita `min`, `max` e `step`; dispara eventos `input` e `change`. |
| Carrossel | Container `data-aura-carousel` com slides `data-slide`, botões `data-carousel="prev"` / `"next"` e texto `data-carousel-status` opcional | Alterna slides por `hidden`, mostra a posição e permite voltar ao início. A troca é manual. |
| Mostrar senha | Botão `data-toggle-password="id-do-input"` | Alterna `type="password"` / `"text"` e atualiza `aria-pressed` e o nome acessível do botão. |
| Dialog | Elemento `dialog` com ID; botão `data-open-dialog="id"`; botão `data-close-dialog` dentro do dialog | Abre como modal e fecha pelo botão, Escape ou clique no backdrop. O comportamento nativo administra o foco. |
| Menu de ações | `details[data-aura-menu]` com `summary` e ações em botões ou links | Fecha ao clicar fora ou escolher uma ação. Escape fecha o menu e devolve o foco ao summary. |
| Seleção de tabela | Container `data-aura-selection`, checkbox de cabeçalho `data-select-all` e checkboxes de linhas `data-select-item` | Seleciona ou desmarca as linhas habilitadas. O cabeçalho mostra o estado parcial com `indeterminate` e é desabilitado se nenhuma linha puder ser selecionada. |
| Tooltip | Wrapper `data-aura-tooltip` com uma dica `role="tooltip"` | Escape adiciona `.is-dismissed` para ocultar a dica; ela pode aparecer novamente depois que o foco e o hover saírem do wrapper. |
| Toast | Botão `data-toast="Mensagem"`; container `id="aura-toast-region"`, `role="status"` e `aria-live="polite"` | Exibe até três notificações; cada uma pode ser fechada e desaparece após seis segundos. O tempo pausa durante hover ou foco dentro da notificação, e retoma com o tempo restante ao sair. Cria o container automaticamente se necessário. |
| Progresso de demonstração | Botão `data-progress-demo="id-do-progress"`, `data-output="id-do-output"` opcional | Simula um trabalho até 100%; um novo clique reinicia a simulação. O texto dentro de `progress` acompanha o output. Use `progress` com `max="100"` e nome acessível. |
| Fechar alerta | Botão `data-dismiss` dentro de `.aura-alert` | Remove o alerta correspondente. |
| Paginação | Container `data-pagination` com botões `data-page="1"`, `"2"` etc.; botões `data-page="prev"` / `"next"` opcionais; texto `data-page-status` | Atualiza `aria-current="page"`, botões anterior/próximo e o texto da página. |
| Formulário de demonstração | `form[data-submit-demo]` com `#form-feedback` ou `[data-form-feedback]`, `role="status"` | Usa a validação nativa e exibe confirmação no submit. `data-submit-message` personaliza a mensagem. |
| Upload | `input[type="file"][data-upload]`, `data-output="id-do-output"` | Mostra o nome do arquivo ou a quantidade selecionada. |

Nos botões que não enviam um formulário, use `type="button"`. Para tabs verticais, adicione `aria-orientation="vertical"` ao `tablist`; nesse caso, as setas para cima e para baixo fazem a navegação. Identifique cada aba com um ID e relacione o painel correspondente por `aria-labelledby`.

O menu usa os elementos nativos `details`, `summary`, `button` e `a`. Seus itens seguem a ordem normal de Tab; Enter e Espaço acionam botões, e Enter abre links. Evite acrescentar `role="menu"` ou `role="menuitem"` a essa versão, pois esses papéis exigem outro padrão de navegação pelo teclado.

No tooltip, dê um ID à dica e conecte o controle por `aria-describedby`. O CSS deve mostrar a dica em `:hover` e `:focus-within`, e ocultá-la quando o wrapper tiver `.is-dismissed`. A dica deve conter apenas texto; use uma superfície ou dialog para conteúdo interativo.

O CSS dos componentes deve respeitar `[hidden]` para que abas e slides ocultos desapareçam, inclusive quando usam `display: flex` ou `grid`:

```css
[hidden] { display: none !important; }
```

## Exemplo de slider

```html
<label class="aura-field" for="volume">
  <span class="aura-field__label">Volume</span>
  <input id="volume" class="aura-range" type="range" min="0" max="100" value="65"
    data-aura-range data-output="volume-valor" data-suffix="%">
  <output id="volume-valor" for="volume">65%</output>
</label>
```

## Integração em uma aplicação

Selects, radios, checkboxes, campos de data/hora, accordion com `details` e outros controles nativos funcionam com HTML e CSS. O script adiciona os comportamentos descritos na tabela.

A barra de progresso e o formulário de demonstração ilustram os estados do sistema. Em uma aplicação, substitua a simulação pela atualização do trabalho real e o feedback de formulário pelo resultado do envio. O script não envia dados, não faz chamadas de rede e não salva informações do projeto. Somente a preferência de tema é salva localmente, em `aura-theme`.

Os nomes de arquivos e as mensagens das notificações são inseridos como texto. Os exemplos preservam a operação pelo teclado, e o carrossel permite que a pessoa escolha o ritmo da navegação.
