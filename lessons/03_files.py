"""Lesson 3: files."""
from pathlib import Path


def write_lines(path: Path, lines) -> int:
    """Write lines with a trailing newline and return the byte count."""
    content = "\n".join(lines) + "\n"
    path.write_text(content, encoding="utf-8")
    return len(content.encode("utf-8"))


def read_non_empty(path: Path) -> list:
    """Return stripped, non-empty lines."""
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def append_line(path: Path, line: str) -> None:
    """Append one line, creating the file if needed."""
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def lesson() -> list:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "demo.txt"
        size = write_lines(path, ["alpha", "", "beta"])
        append_line(path, "gamma")
        return [size, read_non_empty(path)]
