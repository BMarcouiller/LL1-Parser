from table import Table
#Brandon Marcouiller
#U28887050

class Parser():
    def __init__(self, grammar, start):
        self.table = Table(grammar, start).table

    def parse(self, input, start):
        print('>>>Now parsing input')
        i = 0
        stack = ['$', start]

        while i < len(input):
            print('Current Stack: {} <'.format(stack))
            current = input[i]
            top = stack[-1]

            if top == current:
                stack.pop()
                i += 1
            else:
                key = top, current
                if key not in self.table:
                    return False
                val = self.table[key]
                if val !='@':
                    val = val[::-1]
                    val = list(val)
                    stack.pop()
                    for ele in val:
                        stack.append(ele)
                else:
                    stack.pop()		
        return True
        	


