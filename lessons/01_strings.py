"""Lesson 1: strings."""


def shout(text: str) -> str:
    """Return the text in upper case with an exclamation mark."""
    return f"{text.upper()}!"


def initials(full_name: str) -> str:
    """Return the initials of a name, e.g. 'Ada Lovelace' -> 'A.L.'."""
    parts = [part for part in full_name.split() if part]
    return ".".join(part[0].upper() for part in parts) + "." if parts else ""


def reverse_words(text: str) -> str:
    """Reverse the order of words while keeping each word intact."""
    return " ".join(reversed(text.split()))


def count_vowels(text: str) -> int:
    """Count vowels, case-insensitively."""
    return sum(1 for ch in text.lower() if ch in "aeiou")


def lesson() -> list:
    return [shout("hello"), initials("Ada Lovelace"), reverse_words("one two three"),
            count_vowels("Programming")]
