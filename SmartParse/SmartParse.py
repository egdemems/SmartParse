from tree_sitter import Language, Parser
from .get_languages import GetLanguages

class CodeParser:
  
    def walk(self, parent, lines, nodes={}, seen_lines=[]):
        if seen_lines is None:
            seen_lines = []
        enumerated_lines = list(enumerate(lines))
        for child in parent.named_children:
            identifier = child.type
            start_line = child.start_point[0]
            end_line = child.end_point[0] + 1
            self.walk(child, lines, nodes)
            if len(child.text.splitlines()) > 1 and child.named_child_count > 1:
                for line in enumerated_lines[start_line:end_line]:
                    if line not in seen_lines:
                        seen_lines.append(line)
                        if child.start_byte not in nodes:
                            nodes[child.start_byte] = [line]
                        else:
                            nodes[child.start_byte].append(line)
            
        return nodes
    
    def make_chunks(self, language_name, file_content):
        language = Language(GetLanguages.get_language(language_name))
        parser = Parser(language)
        tree = parser.parse(file_content, encoding="utf8")
        lines = file_content.splitlines()
        print(len(lines))
        results = self.walk(tree.root_node, lines)
        return results