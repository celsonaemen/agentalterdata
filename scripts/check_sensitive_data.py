#!/usr/bin/env python3
"""Scan Markdown files for possible sensitive data.

This script prints alerts only. It does not block commits.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", "node_modules", "__pycache__"}

PATTERNS = [
    ("CNPJ formatado", re.compile(r"(?<!\d)\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}(?!\d)")),
    ("CPF formatado", re.compile(r"(?<!\d)\d{3}\.\d{3}\.\d{3}-\d{2}(?!\d)")),
    ("Chave de NF-e com 44 digitos", re.compile(r"(?<!\d)\d{44}(?!\d)")),
    ("Palavra sensivel: senha", re.compile(r"\bsenhas?\b", re.IGNORECASE)),
    ("Palavra sensivel: token", re.compile(r"\btokens?\b", re.IGNORECASE)),
    ("Palavra sensivel: certificado", re.compile(r"\bcertificados?\b", re.IGNORECASE)),
    ("Extensao sensivel citada", re.compile(r"(?i)\b\S+\.(?:xml|pfx|p12|bak|sql)\b")),
]


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def iter_markdown_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if should_skip(rel):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    alerts: list[tuple[str, int, str]] = []

    for path in iter_markdown_files():
        rel = path.relative_to(ROOT)
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            lines = path.read_text(encoding="latin-1").splitlines()

        for line_no, line in enumerate(lines, start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    alerts.append((str(rel), line_no, label))

    if alerts:
        print("Alertas de possiveis dados sensiveis:")
        for rel, line_no, label in alerts:
            print(f"- {rel}:{line_no} - {label}")
    else:
        print("Nenhum alerta de possiveis dados sensiveis encontrado.")

    print()
    print(f"Resumo: {len(alerts)} alerta(s) em {len({rel for rel, _, _ in alerts})} arquivo(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
