from setuptools import setup, find_packages

setup(
    name="code_parser",
    version="0.1.0",
    author="Harrison Sherwood",
    description="A way to intelligently chunk code files into nodes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/egdemems/SmartParse",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "tree-sitter==0.23.2",
        "tree-sitter-javascript",
        "tree-sitter-python",
        "tree-sitter-ruby",
        "tree-sitter-go",
        "tree-sitter-java",
        "tree-sitter-cpp",
    ],
)
