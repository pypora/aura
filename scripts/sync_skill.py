#!/usr/bin/env python3
"""Atualize os recursos portáteis da skill a partir do design system do repo."""
from pathlib import Path
from shutil import copy2


def sync(repo):
    source = repo / "design-system"
    skill = repo / ".agents/skills/aura"
    if not (source / "aura.css").is_file() or not (skill / "SKILL.md").is_file():
        raise SystemExit("Execute a partir de uma cópia completa do repositório AURA.")
    destination = skill / "assets/design-system"
    docs = {"aura-guia.md", "aura-interacoes.md"}
    for file in source.rglob("*"):
        if not file.is_file() or file.name in docs:
            continue
        target = destination / file.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        copy2(file, target)
    references = skill / "references"
    references.mkdir(parents=True, exist_ok=True)
    for name in docs:
        content = (source / name).read_text(encoding="utf-8")
        for page in ("aura-preview.html", "aura-fontes.html"):
            content = content.replace(f"(./{page})", f"(../assets/design-system/{page})")
        (references / name).write_text(content, encoding="utf-8")
    copy2(repo / "LICENSE", skill / "LICENSE")
    notices = (repo / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    notices = notices.replace("(design-system/", "(assets/design-system/")
    (skill / "THIRD_PARTY_NOTICES.md").write_text(notices, encoding="utf-8")


if __name__ == "__main__":
    repository = Path(__file__).resolve().parents[1]
    sync(repository)
    print("Recursos da skill AURA sincronizados.")
