import unittest
from code_parser.code_parser import CodeParser

class TestCodeParser(unittest.TestCase):
    def test_basic_parsing(self):
        # A simple test that ensures CodeParser can be instantiated and run
        sample_code = "def foo():\n    return 42\n"
        parser = CodeParser(language_name="python", file_path="sample.py", file_content=sample_code)
        self.assertIsNotNone(parser.tree)
        self.assertTrue(parser.results)  # Check if results are produced

if __name__ == '__main__':
    unittest.main()
