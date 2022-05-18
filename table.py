#Brandon Marcouiller
#u28887050
class Table():
	def __init__(self, grammar, start):
		self.table = self.genTable(grammar, start)

	def table(self):
		return self.table

	def first(self, s, grammar):
		ch = s[0]
		firsts = set()
		if ch.isupper():
			for var in grammar[ch]:
				if var == '@':
					if len(s) != 1:
						firsts = firsts.union(self.first(s[1:], grammar))
					else:
						firsts = firsts.union('@')
				else:
					f = self.first(var, grammar)
					firsts = firsts.union(x for x in f)
		else:
			firsts = firsts.union(ch)
		return firsts
	
	def follow(self, s, grammar, follows):
		if len(s)!=1 :
			return {}

		for key in grammar:
			for value in grammar[key]:
				f = value.find(s)
				if f!=-1:
					if f==(len(value)-1):
						if key!=s:
							if key in follows:
								temp = follows[key]
							else:
								follows = self.follow(key, grammar, follows)
								temp = follows[key]
							follows[s] = follows[s].union(temp)
					else:
						next = self.first(value[f+1:], grammar)
						if '@' in next:
							if key!=s:
								if key in follows:
									temp = follows[key]
								else:
									follows = self.follow(key, grammar, follows)
									temp = follows[key]
								follows[s] = follows[s].union(temp)
								follows[s] = follows[s].union(next) - {'@'}
						else:
							follows[s] = follows[s].union(next)
		return follows

	def genTable(self, grammar, start):
		firsts = {}
		for lhs in grammar:
			firsts[lhs] = self.first(lhs, grammar)
		
		follows = {}	
		for lhs in grammar:
			follows[lhs] = set()
		follows[start] = follows[start].union('$')
		for lhs in grammar:
			follows = self.follow(lhs, grammar, follows)
			
		table = {}
		for key in grammar:
			for value in grammar[key]:
				if value!='@':
					for element in self.first(value, grammar):
						table[key, element] = value
				else:
					for element in follows[key]:
						table[key, element] = value

		return table
