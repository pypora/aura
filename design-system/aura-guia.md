# AURA — guia do sistema de design

**Versão:** biblioteca 0.5.1 · **Plataforma:** aplicações web · **Modos:** claro e escuro

A referência visual do AURA é a **luz branca de neon sobre um fundo cinza neutro suave**. A forma presente na imagem de referência não faz parte da identidade.

## Ideia central

Interfaces leves e precisas, com texto em grafite no modo claro e texto claro no modo escuro, além de bastante espaço vazio. O neon branco aparece como atmosfera ou ênfase pontual nos dois temas. A inspiração no minimalismo da Apple se traduz em clareza, hierarquia e refinamento; os componentes e a assinatura visual são próprios deste sistema.

**Cinza neutro:** toda a base visual é acromática, com canais **R=G=B**, nos modos claro e escuro. A regra inclui fundos, textos, bordas, foco, overlays, sombras, tabelas, carrosséis e avatares. Os cinzas variam em luminosidade; sucesso, erro e aviso preservam suas cores nos estados semânticos.

## Fundamentos

| Papel | Token | Claro | Escuro | Uso |
| --- | --- | --- | --- | --- |
| Fundo | `--aura-canvas` | `#F6F6F6` | `#151515` | Base da página |
| Superfície | `--aura-surface` | `#FFFFFF` | `#1F1F1F` | Cards, campos e menus |
| Superfície suave | `--aura-surface-soft` | `#EEEEEE` | `#2B2B2B` | Blocos secundários |
| Fundo do neon | `--aura-stage` | `#D9D9D9` | `#363636` | Área cinza para exibir a luz |
| Texto | `--aura-ink` | `#242424` | `#F2F2F2` | Títulos e texto principal |
| Texto secundário | `--aura-ink-muted` | `#5F5F5F` | `#B1B1B1` | Legendas e apoio |
| Ação principal | `--aura-action` | `#2C2C2C` | `#EAEAEA` | Fundo do botão principal |
| Texto sobre ação | `--aura-on-action` | `#FFFFFF` | `#1E1E1E` | Botão principal e tooltip |
| Borda de controle | `--aura-control-line` | `#828282` | `#878787` | Campos e escolhas |
| Foco | `--aura-focus` | `#575757` | `#D3D3D3` | Indicador de teclado |
| Núcleo da luz | `--aura-neon` | `#FFFFFF` | `#FFFFFF` | Linha e preenchimento luminosos |
| Texto sobre neon branco | `--aura-on-neon` | `#242424` | `#242424` | Aba luminosa selecionada |

O token `--aura-action` define o fundo de ações e seleções. `--aura-graphite` acompanha esse valor como alternativa para código anterior. Use `--aura-on-action` para o texto sobre esse fundo.

**Família oficial:** **Manrope**, do Google Fonts, para títulos, textos e componentes em todas as aplicações. Pilha CSS: `"Manrope", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`. O arquivo variável é carregado localmente por `aura.css`, com `font-display: swap`; a fonte nativa serve como alternativa durante o carregamento ou se o arquivo estiver indisponível.

**Licença:** SIL Open Font License 1.1, gratuita para uso pessoal e comercial. O pacote inclui `fontes-aura/manrope-variable.ttf` e `fontes-aura/manrope-OFL.txt`; preserve o aviso de copyright e a licença ao distribuir a fonte. [Catálogo Google Fonts](https://fonts.google.com/specimen/Manrope) · [Licença oficial](https://github.com/google/fonts/blob/main/ofl/manrope/OFL.txt).

| Papel | Tamanho com base de 16 px | Peso | Entrelinha |
| --- | --- | --- | --- |
| Display | 48–96 px, responsivo | 600 | 1,1 |
| Título de seção | 32–48 px, responsivo | 600 | 1,1 |
| Subtítulo | 20 / 24 px | 600 | 1,1 |
| Corpo | 16 px | 400 | 24 px |
| Controles e rótulos | 14 px | 400 / 600 | 20 px |
| Texto de ajuda | 12 px | 400 | 18 px |
| Badges | 12 px | 700 | 15 px |

Pesos permitidos: **400, 500, 600 e 700**. A escala usa `rem`, para acompanhar a preferência de tamanho de texto. Títulos usam tracking de `-0.035em`; texto de leitura mantém o espaçamento normal.

**Comparativo tipográfico:** `aura-fontes.html` mantém as amostras de Manrope, DM Sans e Inter que apoiaram a escolha. Manrope é a família oficial do AURA. As demais fontes acompanham apenas o comparativo, com seus arquivos e licenças na pasta `fontes-aura`.

**Raios por função:** **8 px** em elementos internos; **12 px** em botões, campos, selects e steppers; **16 px** em cards, tabelas, accordion e toast; **24 px** em painéis, modal e drawer. Cápsulas e círculos ficam reservados a chips, badges, switches e indicadores. O arredondamento não muda no mobile.

**Tamanhos:** controles padrão com altura mínima de **48 px**; variante compacta de **44 px**. Botões comuns e campos usam o mesmo raio de 12 px. Textarea, select múltiplo e escolhas com várias linhas crescem com o conteúdo. Avatares usam 48 / 32 px e ícones comuns usam 20 px.

**Ritmo:** espaços em múltiplos de 4 px, com tokens `0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4rem`. A prévia apresenta a tipografia e um comparativo de medidas no final da página.

## Modos claro e escuro

O modo **claro é o padrão**. Para abrir uma página no modo escuro, declare o tema no elemento `html`:

```html
<html lang="pt-BR" data-aura-theme="dark">
```

Use `data-aura-theme="light"` para declarar o claro. A fonte Manrope, os pesos, a escala, os tamanhos dos controles, os espaçamentos e os raios são compartilhados. Cada tema altera as cores e os efeitos; os halos têm menor opacidade no escuro. O CSS também ajusta `color-scheme`, para que os controles oferecidos pelo navegador acompanhem o tema.

Com `aura.js`, um botão pode alternar os temas:

```html
<button type="button" class="aura-button aura-button--secondary"
  data-aura-theme-toggle aria-label="Modo escuro" aria-pressed="false">
  <span data-aura-theme-label aria-hidden="true">Modo escuro</span>
</button>
```

O script atualiza o texto visível e `aria-pressed`. O nome acessível permanece “Modo escuro”, enquanto o estado pressionado indica se esse modo está ativo. Com o script inicializado, use `Aura.setTheme('dark')` ou `Aura.setTheme('light')` para escolher o tema por código. A preferência fica no `localStorage`, na chave `aura-theme`, e prevalece sobre o atributo inicial na próxima abertura. Se o armazenamento estiver indisponível, a alternância continua funcionando na página atual.

Em `aura-tokens.json`, `themes.light` e `themes.dark` são mapas de nomes de variáveis CSS e seus valores. Os dados compartilhados de tipografia e geometria ficam fora desses mapas. Na aplicação web, a alternância já usa as variáveis de `aura.css`; o JSON permite integrar os mesmos valores a outros fluxos.

O documento emite `aura:themechange`, com o tema em `event.detail.theme`. Veja os exemplos da API e do evento no [guia de interações](./aura-interacoes.md).

## Regras de composição

1. Comece cada tela com uma hierarquia clara: título, descrição breve, ação principal e conteúdo.
2. Use superfícies do tema e bordas sutis para organizar, com cinzas neutros (**R=G=B**) em toda a base. Sombras ficam reservadas a elementos elevados.
3. A luz branca precisa de um fundo cinza perceptível. Use o efeito em uma região de destaque por vista ou menos.
4. Mantenha texto e controles legíveis sem depender do brilho. O neon é decorativo.
5. Não associe a identidade a uma forma geométrica fixa; ela pode aparecer como feixe, halo ou borda sutil.
6. Em telas com muitos dados, reduza o brilho e deixe o conteúdo dominar.

## Biblioteca de componentes

| Grupo | Componentes | Comportamentos |
| --- | --- | --- |
| Ações | Botões primário, secundário, discreto, destrutivo, ícone e carregamento | Hover, foco, pressionado, desabilitado |
| Texto | Input, busca, e-mail, senha, textarea, número e sugestões | Validação nativa, mostrar/ocultar senha, ajuda e erro |
| Escolhas | Select simples, select múltiplo, radio, checkbox e switch | Seleção nativa, grupos e estado desabilitado |
| Ajustes | Slider e stepper | Valor visível, limites e passos |
| Datas | Data, hora, data/hora e mês | Seletores nativos do navegador |
| Arquivos | Upload múltiplo | Nome ou quantidade de arquivos selecionados |
| Navegação | Tabs segmentadas, breadcrumb, paginação, menu e etapas | Painéis, setas do teclado, Home/End, Escape e estado atual |
| Feedback | Progresso determinado e indeterminado, spinner e skeleton | Simulação de progresso e redução de movimento |
| Mensagens | Alertas, toast, badges e chips | Dispensar mensagem, pausa do toast durante foco ou hover |
| Conteúdo | Cards, listas, avatares, tabela, carrossel e estado vazio | Seleção de linhas, slides manuais e ações |
| Sobreposições | Modal, confirmação, drawer e tooltip | Foco nativo do dialog, Escape, fechamento e dica por foco/hover |
| Expressão | Luz branca sobre cinza | `.aura-neon-line` e progresso luminoso decorativo |

Selects e seletores de data/hora preservam os popups nativos; a aparência desses popups pode variar conforme o navegador e o sistema operacional. Os campos visíveis usam os tokens AURA.

Para controles, use `--aura-control-line` (`#828282` no claro e `#878787` no escuro). O token `--aura-line` permanece adequado para divisórias e bordas de superfícies. Rótulos, texto de erro e foco devem permanecer visíveis. O brilho é decorativo e não comunica o estado sozinho.

## Variações de neon

As variantes luminosas preservam a geometria e a tipografia do componente base. O halo branco fica visível sobre o cinza de cada tema, com texto e bordas legíveis. Os textos seguem `--aura-ink`; quando a superfície selecionada é branca nos dois temas, como nas tabs neon, o texto usa `--aura-on-neon`. Não há animação contínua do brilho.

| Componente | Classe de variação | Expressão |
| --- | --- | --- |
| Botão | `.aura-button--neon` | Contorno e halo branco |
| Input / select | `.aura-input--neon` | Luz suave, reforçada no foco |
| Card | `.aura-surface--neon` | Borda branca e superfície cinza |
| Slider | `.aura-range--neon` | Trilho preenchido de branco |
| Tabs | `.aura-tabs--neon` | Opção ativa luminosa |
| Radio card | `.aura-choice--neon` | Halo na opção selecionada |

Use o efeito em um ponto focal por área. Combine a variante com a classe base, por exemplo `class="aura-button aura-button--neon"`. O estado de erro e o foco continuam identificáveis. Sombras não alteram dimensões nem espaçamento.

O token `--aura-neon-glow-soft` tem uma borda óptica de 1 px e halo de 12 px; `--aura-neon-glow-strong` usa 2 px e halo de 20 px para hover, foco ou seleção. No modo escuro, a opacidade dessas duas camadas cai de 0,65 / 0,42 para 0,22 / 0,12 no halo suave e de 0,95 / 0,75 para 0,55 / 0,25 no destaque. Esses valores controlam o efeito, sem modificar o raio do componente.

## Uso em um app web

Copie `aura.css`, `aura.js` e a pasta `fontes-aura` para o projeto, mantendo a pasta ao lado do CSS. A aplicação precisa de `manrope-variable.ttf` e `manrope-OFL.txt`; DM Sans e Inter são usadas somente no comparativo. O caminho da fonte é relativo ao arquivo CSS: se o seu projeto mover os assets, ajuste o `src` de `@font-face`.

```text
assets/
  aura.css
  aura.js
  fontes-aura/
    manrope-variable.ttf
    manrope-OFL.txt
```

Importe os arquivos como no exemplo abaixo. Os tokens compartilhados e as cores claras estão em `:root`; as cores escuras estão em `:root[data-aura-theme="dark"]`. `aura-tokens.json` contém os mesmos valores principais, os mapas dos dois temas, a família oficial e os dados de carregamento da fonte.

```html
<link rel="stylesheet" href="./aura.css">
<script src="./aura.js" defer></script>

<main class="aura-surface" style="padding: 2rem">
  <h1>Seu projeto</h1>
  <p>Uma interface clara para a próxima decisão.</p>
  <button class="aura-button aura-button--primary">Começar</button>
</main>
```

A [prévia em HTML](./aura-preview.html) reúne os componentes e suas interações. Os dados são demonstrativos: o formulário valida no navegador e as ações exibem estados locais, sem salvar ou enviar dados do produto. A preferência de tema é salva localmente. O [guia de interações](./aura-interacoes.md) explica os atributos usados no HTML, a função `Aura.init(root)` para conteúdo adicionado dinamicamente e a API de temas.

## Próxima evolução

Aplicar o sistema a uma tela real de um dos seus apps web e conectar os componentes aos dados e às ações do produto. Essa etapa permitirá ajustar densidade, navegação, regras de validação e componentes específicos, como gráficos ou filtros complexos.
