"""Lesson 6: exceptions."""


class ValidationError(ValueError):
    """Raised when user input is not acceptable."""


def parse_port(value: str) -> int:
    """Parse a TCP port, raising ValidationError with a clear message."""
    try:
        port = int(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError(f"port must be a number: {value!r}") from exc
    if not 0 < port < 65536:
        raise ValidationError(f"port out of range: {port}")
    return port


def safe_divide(a: float, b: float) -> float | None:
    """Return None instead of raising on division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def lesson() -> list:
    results = [safe_divide(1, 2), safe_divide(1, 0)]
    try:
        parse_port("70000")
    except ValidationError as exc:
        results.append(str(exc))
    return results
