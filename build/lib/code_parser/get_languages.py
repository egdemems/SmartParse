import tree_sitter_javascript as tsjs
import tree_sitter_python as tspython
import tree_sitter_ruby as tsruby
import tree_sitter_go as tsgo
import tree_sitter_java as tsjava
import tree_sitter_cpp as tscpp

class GetLanguages:
    @staticmethod
    def get_language(language):
        if language.lower() == "javascript":
            return tsjs.language()
        elif language.lower() == "python":
            return tspython.language()
        elif language.lower() == "ruby":
            return tsruby.language()
        elif language.lower() == "go":
            return tsgo.language()
        elif language.lower() == "java":
            return tsjava.language()
        elif language.lower() == "cpp" or language.lower() == "c++":
            return tscpp.language()
        else:
            raise ValueError(f"Unsupported language: {language}")