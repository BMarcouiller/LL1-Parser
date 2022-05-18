#Brandon Marcouiller
#U28887050
from LL1Parser import Parser
import sys
import re


if len(sys.argv) != 2:
    raise ValueError('Please provide a grammar file.')

def parseGrammar(file):
    start = None
    grammar = {}
    txt = ''
    for line in file:
        if line == '' or line == '\n':
            break
        match = re.search('([A-Z]) -> (.*)', line)
        var = match.group(1)
        if not start:
            start = var
        productions = set(re.findall('[^\\| ]*', match.group(2))) - {''}
        grammar[var] = productions
        txt += line
    return [grammar, start, txt]

out = parseGrammar((open(sys.argv[1],'r')))
grammar = out[0]
start = out[1]
txt = out [2]

parser = Parser(grammar, start)
while True:
    print('****************************')
    print('The given grammar is: \n{}'.format(txt))
    print('****************************')
    str = input('Enter a string to parse:').strip()
    print('The string accepted = {}'.format(parser.parse(str, start)))
    str = input('Would you like to parse another string. Enter Y for yes; anything else will terminate').strip()
    if str != 'Y':
        break

x = 0