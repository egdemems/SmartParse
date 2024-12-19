# SmartParse

A way to intelligently chunk code files into nodes.

## Features
- Supports multiple languages: Python, JavaScript, Ruby, Go, Java, C++.
- Parses code into structured nodes for easy manipulation.
- Combines multi-line nodes into manageable chunks.

## Installation
Install directly from GitHub:
```bash
pip install git+https://github.com/yourusername/code_parser.git
```

##Usage
```python
from code_parser import CodeParser

file_path = "/example/path.py"
with open(file_path, 'rb') as file:
    file_content = file.read()
parser = CodeParser(language_name="python", file_path=file_path, file_content=file_content)
results = parser.results
```