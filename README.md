# python-learning-lab

Six short lessons that teach Python through code you can run and tests you can
break. Each lesson file contains small, complete functions with a short
explanation; the tests show the expected behavior and how to check your own
variation.

## Lessons

| File | Topic |
|---|---|
| `lessons/01_strings.py` | Slicing, formatting, `str` methods, f-strings |
| `lessons/02_collections.py` | Lists, dicts, sets and comprehensions |
| `lessons/03_files.py` | Reading and writing files safely |
| `lessons/04_functions.py` | Arguments, defaults, closures, decorators |
| `lessons/05_classes.py` | Dataclasses, `__repr__`, properties |
| `lessons/06_errors.py` | Exceptions, custom errors, cleanup |

## Features

- Every lesson is imported and executed by the test suite.
- Tests document expected behavior — change the code, watch a test explain itself.
- A `lab.py` runner executes all lessons and prints their output.
- Standard library only.

## Installation

```bash
git clone https://github.com/victor-harden/python-learning-lab.git
cd python-learning-lab
```

## Usage

```bash
python3 lab.py                    # run all lessons
python3 lab.py 02                 # run one lesson
python3 -m unittest discover -s tests -v
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT — see [LICENSE](LICENSE).
