from antlr4 import *
from SwitchLangLexer import SwitchLangLexer
from SwitchLangParser import SwitchLangParser
from antlr4.tree.Tree import TerminalNode

def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.getChildren() or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

def main():
    input_text = """
    x = 2;
    switch (x) {
      case 1: y = 10;
      case 2: y = 20;
      default: y = 0;
    }
    """

    input_stream = InputStream(input_text)
    lexer = SwitchLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("## 🔤 TOKENS")
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            print(f"  - {SwitchLangLexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

    parser = SwitchLangParser(token_stream)
    tree = parser.prog()

    print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
    print(tree.toStringTree(recog=parser))

    print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
    print(pretty_tree(tree, parser.ruleNames))

if __name__ == '__main__':
    main()
