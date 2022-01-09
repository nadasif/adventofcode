import os


class Node:
   rows = cols = 0
   map = [[]]
   
   @staticmethod
   def move() -> bool:
      rows = Node.rows
      cols = Node.cols
      rMoves = set()
      dMoves = set()
      for r in range(Node.rows):
         cr = Node.map[r]
         for c in range(Node.cols):
            nc = (c + 1) % Node.cols
            if cr[c] == '>' and cr[nc] == '.':
               rMoves.add((r, c))
      for m in rMoves:
         (cr, cc) = m
         nc = (cc + 1) % Node.cols
         Node.map[cr][nc] = '>'
         Node.map[cr][cc] = '.'
      
      for r in range(Node.rows):
         cr = Node.map[r]
         nr = Node.map[(r + 1) % Node.rows]
         for c in range(Node.cols):
            if cr[c] == 'v' and nr[c] == '.':
               dMoves.add((r, c))
      for m in dMoves:
         (cr, cc) = m
         nr = (cr + 1) % Node.rows
         Node.map[nr][cc] = 'v'
         Node.map[cr][cc] = '.'
      
      return len(rMoves.union(dMoves)) > 0


def showMap():
   print('Map')
   for r in range(Node.rows):
      s = ''
      for c in range(Node.cols):
         s += f'{Node.map[r][c]}'
      print(s)


def main():
   loadData('.in')
   print(f"Processing {Node.cols} x {Node.rows}")
   showMap()
   c = 1
   while Node.move():
      c += 1
   showMap()
   print(f'Part 1: Total {c} moves')


def loadData(ext):
   filename = os.path.splitext(__file__)[0] + ext
   file = open(filename, 'r')
   Node.map = list(map(lambda l: [c for c in l.strip()], file.readlines()))
   file.close()
   Node.rows = len(Node.map)
   Node.cols = len(Node.map[0])


if __name__ == "__main__":
   main()
