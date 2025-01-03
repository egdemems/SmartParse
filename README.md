# SmartParse

A way to intelligently chunk code files into nodes.

## Features
- Supports multiple languages: Python, JavaScript, Ruby, Go, Java, C++.
- Parses code into structured nodes for easy manipulation.
- Combines multi-line nodes into manageable chunks.

## Installation
Install directly from GitHub:
```bash
pip install git+https://github.com/egdemems/SmartParse.git
```

## Usage
```python
from SmartParse import CodeParser

file_path = '/example/path/file.js'

language = "javascript"
parser = CodeParser()

with open(file_path, 'rb') as file:
    file_content = file.read()

chunks = parser.get_chunks(language=language, file_content=file_content)

for chunk in chunks:
    print(chunk["text"])
```