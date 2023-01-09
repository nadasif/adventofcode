#!/home/runner/adventofcode/venv/bin/python3
import os

def shift(l):
	assert len(l)>0
	v = l[0]
	del l[0]
	return v

def findShortest(grid, start, endCheck):
	ROWS, COLS = len(grid), len(grid[0])
	q = [(start[0],start[1],0)]
	visited = {start}
	while q:
		r,c,d = shift(q)
		d += 1
		#print(f'{r}, {c}, {d}')
		for i, j in [(r+1, c), (r-1, c), (r,c+1), (r,c-1)]:
			if i < 0 or j < 0 or i == ROWS or j == COLS:
				continue
			if (i,j) in visited:
				continue
			if grid[i][j] < grid[r][c] - 1:
				continue
			if endCheck(i,j):
				return d
			visited.add((i,j))
			q.append((i,j,d))

def loadData(ext: str):
	filename = os.path.splitext(__file__)[0] + ext
	file = open(filename, 'r')
	data = file.read()
	file.close()
	return data

def main():
	txt = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''
	txt = loadData('.in')
	lines = txt.split('\n')
	grid = []
	for i in range(len(lines)):
		grid.append([])
		for j in range(len(lines[0])):
			c = lines[i][j]
			if c=='S':
				c = 'a'
				start = (i,j)
			elif c == 'E':
				c = 'z'
				stop = (i,j)
			grid[i].append(ord(c)-97)

	print("\nPart 1")
	print(findShortest(grid, stop, lambda i,j: (i,j)==start))

	print("\nPart 2")
	print(findShortest(grid, stop, lambda i,j: grid[i][j] == 0))

if __name__ == "__main__":
	main()
