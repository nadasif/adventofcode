from lib.mylib import loadData


class String:
	bad = ('ab', 'cd', 'pq', 'xy')
	lc = [chr(97 + n) * 2 for n in range(26)]
	vwl = 'aeiou'
	
	def __init__(self, s):
		self.s = s
	
	def has_a_dup(self):
		return any(c in self.s for c in String.lc)
	
	def has_no_bad(self):
		return not any(c in self.s for c in String.bad)
	
	def has_3_vowels(self):
		return len([c for c in self.s if c in String.vwl]) >= 3
	
	def isNice(self):
		return self.has_no_bad() and self.has_a_dup() and self.has_3_vowels()
	
	def isNice2(self):
		dup = False
		sandwich = False
		for i in range(len(self.s) - 2):
			s = self.s[i:i + 2]
			rs = self.s[i + 2:]
			dup = dup or s in rs
			sandwich = sandwich or (len(rs) > 0 and s[0] == rs[0])
			if dup and sandwich:
				return True
		return False


def main():
	ses = [String(s) for s in loadData().split('\n')]
	# print(ses)
	
	print("\nPart 1")
	print(len([s for s in ses if s.isNice()]))
	
	print("\nPart 2")
	flt = [s for s in ses if s.isNice2()]
	print(len(flt))
	for s in flt:
		print(s.s)


if __name__ == "__main__":
	main()
