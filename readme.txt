LL(1)parser.

Main takes a command line argument for a grammar file which will be located in the grammars folder.
EX: python main ./grammars./grammar1

The grammar must be LL(1) grammar for this parser to work. LL(1) grammar cannot be abiguous or left-recursive

The λ has been replaced with @ for this project.

EX: 
S -> ABC | BC
A -> aAB | @
B -> b
C -> ccC | D
D -> d