from tree_sitter import Language, Parser
from .get_languages import GetLanguages

class CodeParser:
    
    def split_lines(self, file_content):
        lines = []
        start_byte = 0
        for line in file_content.splitlines(keepends=True):
            end_byte = start_byte + len(line) - 1
            lines.append((line, start_byte, end_byte))
            start_byte = end_byte + 1
        return lines

    def walk(self, min_lines, file_content, parent, lines, nodes={}, seen_lines=None):
        if seen_lines is None:
            seen_lines = []
        for child in parent.children:
            identifier = child.type
            start = parent.start_byte
            end = child.end_byte
            
            self.walk(min_lines, file_content, child, lines, nodes, seen_lines)
            relevant_lines = [
                (index, line)
                for index, line in enumerate(lines)
                if line[1] >= start and line [2] <= end and (index, line) not in seen_lines
            ]
            
            if len(relevant_lines) >= min_lines:
                seen_lines.extend(relevant_lines)
                nodes[start] = relevant_lines
            
        return nodes
    
    def make_chunks(self, min_lines, language_name, file_content):
        language = Language(GetLanguages.get_language(language_name))
        parser = Parser(language)
        tree = parser.parse(file_content, encoding="utf8")
        lines = self.split_lines(file_content)
        results = self.walk(min_lines, file_content, tree.root_node, lines)
        return results



