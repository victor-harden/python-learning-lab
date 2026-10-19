"""Lesson 4: functions, defaults, closures and decorators."""
import functools


def power(base: int, exponent: int = 2) -> int:
    """Raise base to exponent (default square)."""
    return base ** exponent


def make_counter(start: int = 0):
    """Return a closure that counts upwards."""
    value = start

    def counter() -> int:
        nonlocal value
        value += 1
        return value

    return counter


def logged(func):
    """Decorator that records call arguments on the wrapper."""
    calls = []

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        calls.append((args, kwargs))
        return func(*args, **kwargs)

    wrapper.calls = calls
    return wrapper


@logged
def add(a, b):
    return a + b


def lesson() -> list:
    counter = make_counter(10)
    return [power(3), power(3, 3), counter(), counter(), add(1, 2), add.calls]
