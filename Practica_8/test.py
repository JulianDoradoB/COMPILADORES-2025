from antlr4 import *
from ControlLangLexer import ControlLangLexer
from ControlLangParser import ControlLangParser
from antlr4.tree.Tree import TerminalNode

def main():
    input_text = """
    x = 0;
    for (i = 0; i < 3; i = i + 1) {
      switch (i) {
        case 0: x = x + 1;
        case 1: x = x + 2;
        default: x = x + 3;
      }
    }
    if (x > 5) {
      y = x * 10;
    }
    """

    input_stream = InputStream(input_text)
    lexer = ControlLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("## 🔤 TOKENS")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            if 0 <= token.type < len(lexer.symbolicNames):
                token_name = lexer.symbolicNames[token.type]
            else:
                token_name = f"<UNKNOWN TOKEN TYPE {token.type}>"

            if token_name != 'WS':
                print(f"  - {token_name} ('{token.text}') @line {token.line}:{token.column}")

    parser = ControlLangParser(token_stream)
    tree = parser.prog()

    print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
    print(tree.toStringTree(recog=parser))

    def pretty_tree(node, rule_names, level=0):
        if isinstance(node, TerminalNode):
            return "  " * level + f"TOKEN({node.getText()})"
        else:
            rule_name = rule_names[node.getRuleIndex()]
            result = "  " * level + rule_name
            for child in node.children or []:
                result += "\n" + pretty_tree(child, rule_names, level + 1)
            return result

    print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
    print(pretty_tree(tree, parser.ruleNames))

if __name__ == '__main__':
    main()
