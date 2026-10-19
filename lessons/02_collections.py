"""Lesson 2: lists, dicts, sets and comprehensions."""


def unique_sorted(values) -> list:
    """Return sorted unique values."""
    return sorted(set(values))


def group_by_length(words) -> dict:
    """Group words by their length."""
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


def word_frequency(text: str) -> dict:
    """Count words case-insensitively."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def flatten(matrix) -> list:
    """Flatten a list of lists with a comprehension."""
    return [item for row in matrix for item in row]


def lesson() -> list:
    return [unique_sorted([3, 1, 3, 2]), group_by_length(["a", "bb", "cc"]),
            word_frequency("to be or not to be"), flatten([[1, 2], [3]])]
