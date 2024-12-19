from tree_sitter import Language, Parser
from .get_languages import GetLanguages
import bisect

class CodeParser:
    def split_lines(self, file_content):
        lines = []
        start_byte = 0
        for line in file_content.splitlines(keepends=True):
            end_byte = start_byte + len(line) - 1
            lines.append((line, start_byte, end_byte))
            start_byte = end_byte + 1
        return lines

    def find_line_for_byte(self, byte_position, lines):
        start_bytes = [start for _, start, _ in lines]
        index = bisect.bisect_right(start_bytes, byte_position) - 1
        return lines[index] if index >= 0 else None

    def walk(self, parent, lines, lines_depth, seen=None, seen_lines=None, seen_parents=None, depth=0):
        if seen is None:
            seen = {}
        if seen_lines is None:
            seen_lines = []
        if seen_parents is None:
            seen_parents = []
        for child in parent.children:
            start = child.start_byte
            end = child.end_byte
            start_line = self.find_line_for_byte(start, lines)
            end_line = self.find_line_for_byte(end, lines)
            if child.children:
                self.walk(child, lines, lines_depth, seen, seen_lines, seen_parents, depth + 1)

            if start_line != end_line:
                start_index = lines.index(start_line)
                end_index = lines.index(end_line)
                start_char = start_line[1]
                for line in lines[start_index:end_index + 1]:
                    if line not in seen_lines:
                        if start_char not in seen:
                            seen[start_char] = [line]
                        else:
                            seen[start_char].append(line)
                        seen_lines.append(line)
                        lines_depth[line] = depth

                    if line[1] in seen and line[1] not in seen_parents:
                        if line[1] != start_char:
                            seen[start_char].append(('n', line[1]))
                            seen_parents.append(line[1])

        return seen
    
    def combine(self, results):
        to_delete = []
        for result in results.items():
            non_n_lines = 0
            n_lines = 0
            
            for line in result[1]:
                if line[0] == 'n':
                    n_lines += 1
                else:
                    non_n_lines += 1

            if non_n_lines < 3 and n_lines == 1:
                new_node = []
                for line in result[1]:
                    if line[0] == 'n':
                        new_node.extend(results[line[1]])
                        to_delete.append(line[1])
                    else:
                        new_node.append(line)
                results[result[0]] = new_node
            if non_n_lines < 3 and n_lines == 0:
                for key, value in results.items():
                    if ('n', result[0]) in value:
                        new_node = []
                        for sub_line in value:
                            if sub_line[0] == 'n':
                                new_node.extend(results[result[0]])
                                to_delete.append(result[0])
                            else:
                                new_node.append(sub_line)
                        results[key] = new_node
        
        for d in to_delete:
            if d in results:  # Check if the key exists before deleting
                del results[d] 
        
        return results
            
    def make_chunks(self, language_name, file_content, lines, tree):
        language = Language(GetLanguages.get_language(language_name))
        parser = Parser(language)
        tree = parser.parse(file_content, encoding="utf8")
        lines = self.split_lines(file_content)
        lines_depth = {}
        results = self.walk(tree.root_node, lines, lines_depth)
        chunks = self.combine(results)
        return chunks