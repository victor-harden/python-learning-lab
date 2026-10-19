import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))


def load(name, filename):
    path = BASE / "lessons" / filename
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


strings = load("lesson_strings", "01_strings.py")
collections_lesson = load("lesson_collections", "02_collections.py")
files = load("lesson_files", "03_files.py")
functions = load("lesson_functions", "04_functions.py")
classes = load("lesson_classes", "05_classes.py")
errors = load("lesson_errors", "06_errors.py")


class StringTests(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(strings.shout("hi"), "HI!")

    def test_initials(self):
        self.assertEqual(strings.initials("Ada Lovelace"), "A.L.")

    def test_initials_empty(self):
        self.assertEqual(strings.initials("   "), "")

    def test_reverse_words(self):
        self.assertEqual(strings.reverse_words("one two three"), "three two one")

    def test_count_vowels(self):
        self.assertEqual(strings.count_vowels("Programming"), 3)


class CollectionTests(unittest.TestCase):
    def test_unique_sorted(self):
        self.assertEqual(collections_lesson.unique_sorted([3, 1, 3]), [1, 3])

    def test_group_by_length(self):
        self.assertEqual(collections_lesson.group_by_length(["a", "bb"]), {1: ["a"], 2: ["bb"]})

    def test_word_frequency(self):
        self.assertEqual(collections_lesson.word_frequency("To be to")["to"], 2)

    def test_flatten(self):
        self.assertEqual(collections_lesson.flatten([[1], [2, 3]]), [1, 2, 3])


class FileTests(unittest.TestCase):
    def test_write_and_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.txt"
            files.write_lines(path, ["alpha", "", "beta"])
            files.append_line(path, "gamma")
            self.assertEqual(files.read_non_empty(path), ["alpha", "beta", "gamma"])

    def test_write_returns_byte_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "demo.txt"
            self.assertEqual(files.write_lines(path, ["ab"]), 3)


class FunctionTests(unittest.TestCase):
    def test_default_exponent(self):
        self.assertEqual(functions.power(3), 9)

    def test_counter_closure(self):
        counter = functions.make_counter()
        self.assertEqual([counter(), counter()], [1, 2])

    def test_decorator_records_calls(self):
        functions.add(2, 3)
        self.assertIn(((2, 3), {}), functions.add.calls)


class ClassTests(unittest.TestCase):
    def test_search(self):
        library = classes.Library()
        library.add(classes.Book("Dune", "Frank Herbert"))
        self.assertEqual(len(library.search("dune")), 1)
        self.assertEqual(len(library), 1)


class ErrorTests(unittest.TestCase):
    def test_valid_port(self):
        self.assertEqual(errors.parse_port("8080"), 8080)

    def test_invalid_port_message(self):
        with self.assertRaises(errors.ValidationError):
            errors.parse_port("abc")

    def test_out_of_range(self):
        with self.assertRaises(errors.ValidationError):
            errors.parse_port("70000")

    def test_safe_divide(self):
        self.assertIsNone(errors.safe_divide(1, 0))


if __name__ == "__main__":
    unittest.main()
