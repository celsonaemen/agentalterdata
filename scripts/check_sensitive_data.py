#!/usr/bin/env python3
"""Scan Markdown files for possible sensitive data.

This script prints alerts only. It does not block commits.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", "node_modules", "__pycache__"}

SECURITY_GUIDE_FILES = {
    "README.md",
    "SKILL.md",
    "bases-oficiais/bdcc/README.md",
    "docs/padroes-documentacao.md",
    "prompts/especialista-alterdata.md",
    "prompts/especialista-fiscal.md",
    "templates/fonte-oficial-template.md",
}

CRITICAL_PATTERNS = [
    ("CNPJ formatado", re.compile(r"(?<!\d)\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}(?!\d)")),
    ("CPF formatado", re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)")),
    ("Chave de NF-e com 44 digitos", re.compile(r"(?<!\d)\d{44}(?!\d)")),
]

WARNING_PATTERNS = [
    ("Palavra sensivel: senha", re.compile(r"\bsenhas?\b", re.IGNORECASE), "word"),
    ("Palavra sensivel: token", re.compile(r"\btokens?\b", re.IGNORECASE), "word"),
    ("Palavra sensivel: certificado", re.compile(r"\bcertificados?\b", re.IGNORECASE), "word"),
    ("Extensao sensivel citada", re.compile(r"(?i)\b\S+\.(?:xml|pfx|p12|bak|sql)\b"), "extension"),
]


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def normalize_rel(path: Path) -> str:
    return path.as_posix()


def iter_markdown_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if should_skip(rel):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    critical: list[tuple[str, int, str]] = []
    warnings: list[tuple[str, int, str]] = []

    for path in iter_markdown_files():
        rel_path = path.relative_to(ROOT)
        rel = normalize_rel(rel_path)
        is_security_guide = rel in SECURITY_GUIDE_FILES

        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = path.read_text(encoding="latin-1").splitlines()

        for line_no, line in enumerate(lines, start=1):
            for label, pattern in CRITICAL_PATTERNS:
                if pattern.search(line):
                    critical.append((rel, line_no, label))

            for label, pattern, warning_type in WARNING_PATTERNS:
                if is_security_guide and warning_type == "word":
                    continue
                if pattern.search(line):
                    warnings.append((rel, line_no, label))

    if critical:
        print("Alertas criticos:")
        for rel, line_no, label in critical:
            print(f"- {rel}:{line_no} - {label}")
    else:
        print("Nenhum alerta critico encontrado.")

    print()

    if warnings:
        print("Warnings:")
        for rel, line_no, label in warnings:
            print(f"- {rel}:{line_no} - {label}")
    else:
        print("Nenhum warning encontrado.")

    print()
    print(f"Resumo: {len(critical)} critico(s), {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
