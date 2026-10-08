# AURA

Design system da **Pypora** para aplicações web: neon branco sobre cinza, Manrope e interfaces minimalistas nos modos claro e escuro.

O repositório reúne a biblioteca **0.5.0**, um catálogo interativo e uma skill para orientar agentes de IA a aplicar a mesma identidade em diferentes projetos.

## O que vem no pacote

| Parte | Conteúdo |
| --- | --- |
| [Design system](design-system/) | CSS, tokens, JavaScript e Manrope local |
| [Catálogo](design-system/aura-preview.html) | Controles, navegação, feedback, conteúdo, sobreposições e variantes neon |
| [Guia visual](design-system/aura-guia.md) | Paleta, tipografia, raios, medidas e composição |
| [Guia de interações](design-system/aura-interacoes.md) | Marcação, comportamentos e temas |
| [Skill AURA](.agents/skills/aura/SKILL.md) | Instruções e uma cópia portátil dos recursos para uso com IA |

## Explorar o catálogo

Clone ou baixe o repositório e abra `design-system/aura-preview.html` no navegador. Mantenha os arquivos vizinhos e a pasta `fontes-aura` junto da página. O botão no topo alterna claro e escuro e salva a preferência localmente.

O GitHub mostra o código-fonte do HTML. Para experimentar os componentes, abra a cópia local no navegador.

## Aplicar em um app

Copie `aura.css` e os arquivos da Manrope para o projeto:

```text
assets/aura/
  aura.css
  fontes-aura/
    manrope-variable.ttf
    manrope-OFL.txt
```

O caminho da fonte é relativo ao CSS. Adapte o `src` de `@font-face` quando seu bundler mover os assets.

Em HTML com JavaScript simples, acrescente `aura.js` para as interações:

```html
<link rel="stylesheet" href="./assets/aura/aura.css">
<script src="./assets/aura/aura.js" defer></script>

<label class="aura-field">
  <span class="aura-field__label">Projeto</span>
  <input class="aura-input" placeholder="Nome do projeto">
</label>
<button type="button" class="aura-button aura-button--primary">Continuar</button>
```

Em React, Vue ou outra arquitetura com estado próprio, use os estilos e tokens e adapte a marcação aos componentes do framework. Implemente os eventos e estados nessa arquitetura; o JavaScript do catálogo serve como referência de comportamento.

O CSS inclui regras globais para `html`, `body` e controles. Para uma migração parcial, adapte o escopo dos estilos às telas selecionadas.

## Temas

O claro é o padrão. Para declarar o escuro inicial:

```html
<html lang="pt-BR" data-aura-theme="dark">
```

Com a integração JavaScript fornecida:

```js
window.Aura.setTheme('dark');
window.Aura.setTheme('light');
```

Uma preferência salva em `aura-theme` prevalece sobre o atributo inicial. Projetos que já possuem gerenciador de tema podem mapear seus modos para as variáveis do AURA.

## Usar a skill

A skill está em `.agents/skills/aura/`. No Codex, ela pode ser usada ao trabalhar neste repositório. Para disponibilizá-la como skill pessoal nos demais projetos, peça ao instalador:

```text
Use $skill-installer para instalar a skill AURA do repositório pypora/aura,
localizada em .agents/skills/aura.
```

Depois, em uma conversa do projeto:

```text
Use $aura para aplicar o design system à tela de login,
preservando as funcionalidades e adaptando os componentes ao framework do projeto.
```

Para outro agente com suporte ao padrão Agent Skills, instale a pasta `aura` conforme as instruções desse agente. Em chats sem suporte a skills, forneça o guia, os tokens, o CSS e os recursos necessários como referências.

## Consistência visual

- Manrope, com pesos 400 / 500 / 600 / 700.
- Controles padrão de 48 px e compactos de 44 px.
- Raios por função: 8 / 12 / 16 / 24 px; exceções para cápsulas e círculos.
- Espaçamento em múltiplos de 4 px e tipografia em `rem`.
- Geometria compartilhada entre claro e escuro.
- Neon branco pontual, com halos mais suaves no modo escuro.

Use os tokens existentes para expandir o catálogo. A forma da luz pode variar; a identidade não depende de uma forma geométrica fixa.

## Atualizar os recursos da skill

`design-system/` é a fonte dos arquivos da biblioteca neste repositório. Após alterá-los, atualize a cópia incluída na skill:

```bash
python3 scripts/sync_skill.py
```

O script atualiza os assets e os dois guias da skill a partir do design system, preservando os caminhos relativos. Ele também copia a licença e os avisos de terceiros para a distribuição portátil.

## Licenças

Código e documentação do AURA: **MIT**, conforme [LICENSE](LICENSE).

Manrope, DM Sans e Inter: **SIL Open Font License 1.1**, com arquivos de licença e créditos preservados. Manrope é a fonte oficial; DM Sans e Inter acompanham apenas o comparativo histórico. Veja [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
