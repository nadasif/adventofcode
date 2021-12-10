import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

lines = '''2199943210
3987894921
9856789892
8767896789
9899965678'''.split('\n')

# file1 = open('d09in.txt', 'r')
# lines = file1.readlines()
# file1.close()
rows = len(lines)
cols = len(lines[0].strip())
visited = {'0':1}
matrix = []
for line in lines:
   matrix.append([int(n) for n in line.strip()])


def main():
   risk = 0
   for r in range(rows):
      for c in range(cols):
         n = matrix[r][c]
         neighbors = [9 if r == 0 else matrix[r - 1][c],
                      9 if r == rows - 1 else matrix[r + 1][c],
                      9 if c == cols - 1 else matrix[r][c + 1],
                      9 if c == 0 else matrix[r][c - 1]]
         if all(n < k for k in neighbors):
            risk += n + 1
   
   print(f'Part 1: {risk}')
   
   # for l in lines:
   #    print(l.strip().replace('9', ' '))
   
   lens = [0]
   skipped = 0
   for r in range(rows):
      for c in range(cols):
         p = rcRep(r, c)
         if p not in visited and matrix[r][c] != 9:
            lens.append(len(findBasin(r, c)))
         else:
            skipped += 1
   
   print(lens)
   sizes = sorted(lens, reverse=True)[:3]
   print(f'Part 2: {sizes[0] * sizes[1] * sizes[2]}')
   print(f'Skipped: {skipped} from {rows * cols}')

def rcRep(r, c):
   return f'{r},{c}'


def findBasin(r, c):
   basin = []
   cur = rcRep(r, c)
   # logger.debug('Find Basin: %s', cur)
   if cur in visited or matrix[r][c] == 9:
      return basin
   basin.append(cur)
   visited[cur] = 1
   # Go up if possible
   if r > 0:
      basin.extend(findBasin(r - 1, c))
   # Go down if possible
   if r < rows - 1:
      basin.extend(findBasin(r + 1, c))
   # Go left if possible
   if c > 0:
      basin.extend(findBasin(r, c - 1))
   # Go left if possible
   if c < cols - 1:
      basin.extend(findBasin(r, c + 1))
   return basin


if __name__ == '__main__':
   main()
