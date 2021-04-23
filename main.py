import ul_lexer
import ul_parser
import ul_interpreter

from sys import *

#DENGAN MASUKAN .px
lexer = ul_lexer.BasicLexer()
parser = ul_parser.BasicParser()
env = {}

# while True:
#     ini = input()
#     tree = parser.parse(lexer.tokenize(ini))
#     ul_interpreter.BasicExecute(tree, env)

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    ul_interpreter.BasicExecute(tree, env)
