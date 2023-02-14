from lib.mylib import loadData


class Prism:
	def __init__(self, txt):
		self.l, self.w, self.h = map(int, txt.split('x'))
	
	def paper(self):
		l, w, h = self.l, self.w, self.h
		areas = [l*w, w*h, l*h]
		return sum(2*n for n in areas) + min(areas)
	
	def ribbon(self):
		sides = [self.l, self.w, self.h]
		sides.remove(max(sides))
		return (self.l * self.w * self.h) + sum(2*n for n in sides)
	
	def __repr__(self):
		return f'{self.l} x {self.w} x {self.h}'


def basement(lst):
	s = 0
	for i, n in enumerate(lst):
		s += n
		if s < 0:
			return i + 1
	return 0


def main():
	txt = loadData()
	lst = list(map(Prism, txt.strip().split('\n')))
	
	# print(lst)
	print("\nPart 1")
	print(sum(map(lambda p: p.paper(), lst)))
	
	print("\nPart 2")
	print(sum(map(lambda p: p.ribbon(), lst)))


if __name__ == "__main__":
	main()
