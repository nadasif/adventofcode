import os


class Sheet:
	
	def __init__(self):
		self.commands = []
		self.map = [[]]
		self.rows = 0
		self.cols = 0
	
	def set(self, c: int, r: int):
		self.rows = max(self.rows, r + 1)
		self.cols = max(self.cols, c + 1)
		while len(self.map) <= r:
			self.map.append([0 for _ in range(self.cols)])
		row = self.map[r]
		while len(row) <= c:
			row.append(0)
		self.map[r][c] = 1
	
	def foldAll(self):
		self.normalize()
		for cmd in self.commands:
			self.fold(cmd)
	
	def fold(self, cmd: str):
		(c, n) = cmd.strip().split('=')
		n = int(n)
		if c == 'fold along y':
			self.foldAlongY(n)
		else:
			self.foldAlongX(n)
	
	def foldAlongX(self, n):
		t = 0
		for i in range(self.rows):
			row = self.map[i]
			k = 1
			while (n - k) >= 0 or (n + k) < self.cols:
				row[n - k] |= row[n + k]
				t += row[n - k]
				k += 1
		self.cols = n
		print(f'Moved along x {n} ({t} dots)')
	
	def foldAlongY(self, n):
		t = 0
		k = 1
		while (n - k) >= 0 or (n + k) < self.rows:
			row1 = self.map[n - k]
			row2 = self.map[n + k]
			for i in range(self.cols):
				row1[i] |= row2[i]
				t += row1[i]
			k += 1
		self.rows = n
		print(f'Moved along y {n} ({t} dots)')
	
	def showMap(self):
		dotHash = [' ', chr(0x258b)]
		s = ''
		for r in range(self.rows):
			row = self.map[r]
			s += '\n'
			for c in range(self.cols):
				if len(row) <= self.cols:
					row.append(0)
				s += dotHash[row[c]]
		print(f'Map: {s}')
	
	def normalize(self):
		for r in range(self.rows):
			row = self.map[r]
			for c in range(self.cols):
				if len(row) <= self.cols:
					row.append(0)


def main():
	sheet = Sheet()
	loadData('.in', sheet)
	sheet.foldAll()
	sheet.showMap()


def loadData(ext: str, sheet: Sheet):
	filename = os.path.splitext(__file__)[0] + ext
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	for line in lines:
		s = line.strip()
		if s.startswith('fold'):
			sheet.commands.append(s)
		elif s == '':
			pass
		else:
			arg = tuple(int(k) for k in s.split(','))
			sheet.set(*arg)


if __name__ == "__main__":
	main()
