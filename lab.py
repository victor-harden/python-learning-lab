#!/usr/bin/env python3
"""Run the lessons and print their output."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

LESSONS_DIR = Path(__file__).resolve().parent / "lessons"


def load_lesson(path: Path):
    spec = importlib.util.spec_from_file_location(f"lesson_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv=None) -> int:
    argv = argv or sys.argv[1:]
    lessons = sorted(LESSONS_DIR.glob("0*.py"))
    selected = [p for p in lessons if not argv or p.name.startswith(argv[0])]
    if not selected:
        print("no matching lesson", file=sys.stderr)
        return 2
    for path in selected:
        module = load_lesson(path)
        print(f"== {path.name} ==")
        for item in module.lesson():
            print(f"  {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
