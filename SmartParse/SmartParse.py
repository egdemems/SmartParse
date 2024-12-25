from tree_sitter import Language, Parser
from .get_languages import GetLanguages

class CodeParser:
  
    def walk(self, parent, lines, seen_lines, nodes={}):
        for child in parent.named_children:
            identifier = child.type
            start = child.start_point[0]
            end = child.end_point[0] + 1
            self.walk(child, lines, seen_lines, nodes)
            if len(child.text.splitlines()) > 1 and child.named_child_count > 1:
                for line in lines[start:end]:
                    if line not in seen_lines:
                        seen_lines.append(line)
                        if start not in nodes:
                            nodes[start] = [line]
                        else:
                            nodes[start].append(line)
            
        return nodes
    
    def get_lines(self, file_content):
        lines = file_content.splitlines()
        return list(enumerate(lines))
    
    def get_chunk_pairs(self, chunks, text_chunks):
        chunk_pairs = []
        for i, chunk in enumerate(chunks.items()):
            chunk_pair = {"chunk": chunk, "text": text_chunks[i]}
            chunk_pairs.append(chunk_pair)
        return chunk_pairs

    def get_chunks(self, language, file_content, line_numbers=True):
        chunks = self.make_chunks(language=language, file_content=file_content)
        text_chunks = self.get_text_chunks(chunks, line_numbers)
        chunk_pairs = self.get_chunk_pairs(chunks, text_chunks)
        return chunk_pairs
    
    def get_text_chunks(self, chunks, line_numbers=True):
        text_chunks = []
        for node in chunks.items():
            chunk_text = ""
            for i, line in enumerate(node[1]):
                if line[0] == (node[1][i-1][0] + 1) or i == 0:
                    if line_numbers:
                        chunk_text += f"{line[0]} {line[1].decode("utf-8")}\n"
                    else:
                        chunk_text += f"{line[1].decode("utf-8")}\n"
                elif i > 0:
                    chunk_text += "\n... existing code... \n\n"
                    if line_numbers:
                        chunk_text += f"{line[0]} {line[1].decode("utf-8")}\n"
                    else:
                        chunk_text += f"{line[1].decode("utf-8")}\n"
            text_chunks.append(chunk_text)
        return text_chunks
    
    def make_chunks(self, language, file_content):
        language = Language(GetLanguages.get_language(language))
        parser = Parser(language)
        tree = parser.parse(file_content, encoding="utf8")
        lines = self.get_lines(file_content)
        seen_lines=[]
        results = self.walk(tree.root_node, lines, seen_lines)
        extra = [line for line in lines if line not in seen_lines]
        results[extra[0][0]] = extra
        return results