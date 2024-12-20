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

file_path = "/example/path.py"
    
parser = CodeParser()

with open(file_path, 'rb') as file:
    file_content = file.read()

results = parser.make_chunks(language_name="python", file_content=file_content)
node_childs = parser.get_child_nodes(results)

for key, result in results.items():
    print(f"\033[2m**NODE: {key}**\033[0m\n")
    for line in result: 
        if isinstance(line[0], bytes):
            print(line[0].decode("utf-8").rstrip("\n"))     
        else:
            print(f"\033[90mnode {line[1]}\033[0m")
    print("\n" + ("-" * 100))

for node in node_childs.items():
    print(node)
```