import ul_lexer
import ul_parser
import ul_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = ul_lexer.BasicLexer()
    parser = ul_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('ul > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            ul_interpreter.BasicExecute(tree, env)
