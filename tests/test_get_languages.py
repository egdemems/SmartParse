import unittest
from code_parser import GetLanguages

class TestGetLanguages(unittest.TestCase):
    def test_get_language(self):
        self.assertIsNotNone(GetLanguages.get_language("python"))
        with self.assertRaises(ValueError):
            GetLanguages.get_language("unknown_language")

if __name__ == "__main__":
    unittest.main()
