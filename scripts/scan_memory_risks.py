#!/usr/bin/env python3
"""Scan memory-like text files for likely privacy and credential risks."""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


PATTERNS = [
    ("critical", "OpenAI-style API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("critical", "generic secret assignment", re.compile(r"(?i)\b(api[_-]?key|token|secret|password|passwd|pwd)\b\s*[:=]\s*['\"]?[^'\"\s]{8,}")),
    ("critical", "private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("high", "US SSN-like number", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("high", "bank card-like number", re.compile(r"\b(?:\d[ -]*?){13,19}\b")),
    ("medium", "email address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("medium", "US phone-like number", re.compile(r"(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b")),
    ("medium", "China phone-like number", re.compile(r"\b1[3-9]\d{9}\b")),
    ("medium", "IPv4 address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("high", "medical keyword", re.compile(r"(?i)\b(diagnosis|medical record|patient|病历|诊断|处方|医保)\b")),
    ("high", "financial keyword", re.compile(r"(?i)\b(salary|revenue|bank account|contract amount|收入|工资|银行卡|合同金额)\b")),
]

TEXT_SUFFIXES = {
    ".txt",
    ".md",
    ".markdown",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".csv",
    ".log",
}


def iter_files(path: Path):
    if path.is_file():
        yield path
        return

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "venv", "__pycache__"}]
        for name in files:
            file_path = Path(root) / name
            if file_path.suffix.lower() in TEXT_SUFFIXES:
                yield file_path


def scan_file(path: Path):
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        print(f"WARN\t{path}\t{exc}")
        return 0

    count = 0
    for lineno, line in enumerate(lines, 1):
        for level, label, pattern in PATTERNS:
            match = pattern.search(line)
            if not match:
                continue
            preview = line.strip()
            if len(preview) > 140:
                preview = preview[:137] + "..."
            print(f"{level.upper()}\t{label}\t{path}:{lineno}\t{preview}")
            count += 1
            break
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File or directory to scan")
    args = parser.parse_args()

    target = Path(args.path).expanduser()
    if not target.exists():
        print(f"ERROR\tpath does not exist: {target}")
        return 2

    total = 0
    scanned = 0
    for file_path in iter_files(target):
        scanned += 1
        total += scan_file(file_path)

    print(f"SUMMARY\tscanned_files={scanned}\tfindings={total}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
