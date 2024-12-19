import unittest
from code_parser import CodeParser

class TestCodeParser(unittest.TestCase):
    def test_initialization(self):
        language_name = "python"
        file_path = "example.py"
        file_content = b"def example():\n    pass\n"
        parser = CodeParser(language_name, file_path, file_content)
        self.assertEqual(parser.file_path, file_path)
        self.assertEqual(parser.file_content, file_content)

    def test_split_lines(self):
        content = b"line1\nline2\nline3\n"
        parser = CodeParser("python", "test.py", content)
        lines = parser.split_lines(content)
        self.assertEqual(len(lines), 3)

if __name__ == "__main__":
    unittest.main()
