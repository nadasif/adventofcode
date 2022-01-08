import os


class Node:
   rows = cols = 0
   map = lowest = None
   
   def __init__(self, r, c, p):
      self.r = r
      self.c = c
      self.key = f'{r:03}{c:03}'
      self.w = Node.map[r][c]
      self.p = p
      self.f = 0 if p is None else p.f + self.w
      self.g = 0
      self.h = Node.rows - r + Node.cols - c - 2
   
   def successors(self):
      lst = []
      if self.r > 0:
         lst.append(Node(self.r - 1, self.c, self))
      if self.r < Node.rows - 1:
         lst.append(Node(self.r + 1, self.c, self))
      if self.c > 0:
         lst.append(Node(self.r, self.c - 1, self))
      if self.c < Node.cols - 1:
         lst.append(Node(self.r, self.c + 1, self))
      
      return list(filter(lambda l: not l.isSkip(), lst))
   
   def isSkip(self):
      if self.key not in Node.lowest:
         Node.lowest[self.key] = self
      elif Node.lowest[self.key].f > self.f:
         Node.lowest[self.key] = self
      
      if self.f > Node.lowest[self.key].f:
         return True
      p = self.p
      while p:
         if self == p:
            return True
         p = p.p
      return False
   
   def __repr__(self):
      return f'N({self.key},{self.w},{self.f},{self.p is not None})'
   
   def __eq__(self, node):
      return node is not None and self.r == node.r and self.c == node.c


def byF(node: Node):
   return node.f


def levelUp(value):
   return 1 if value == 9 else value + 1


def extendMap():
   for r in range(Node.rows):
      for c in range(Node.cols*4):
         Node.map[r].append(levelUp(Node.map[r][c]))
   Node.cols *= 5
   for r in range(Node.rows*4):
      row = []
      for c in range(Node.cols):
         row.append(levelUp(Node.map[r][c]))
      Node.map.append(row)
   Node.rows *= 5
   
def showMap():
   for r in range(Node.rows):
      s = ''
      for c in range(Node.cols):
         s += f'{Node.map[r][c]}'
      print(s)


def main():
   loadData('.in')
   showMap()
   print(f"Processing {Node.cols} x {Node.rows}")
   start = Node(0, 0, None)
   Node.lowest = {start.key: start}
   findPath(start)
   end = Node(Node.rows - 1, Node.cols - 1, None)
   print(f"Part 1: {Node.lowest[end.key]}")

   extendMap()
   showMap()
   Node.lowest = {start.key: start}
   findPath(start)
   end = Node(Node.rows - 1, Node.cols - 1, None)
   print(f"Part 2: {Node.lowest[end.key]}")


def findPath(start):
   openList = {start.key: start}
   while len(openList) > 0:
      # print(f'Open  : {openList.values()}')
      k = sorted(openList.values(), key=byF)[0].key
      q = openList.pop(k)
      for s in q.successors():
         if s.key not in openList:
            openList[s.key] = s
         elif openList[s.key].f > s.f:
            openList[s.key] = s


def loadData(ext):
   filename = os.path.splitext(__file__)[0] + ext
   file = open(filename, 'r')
   Node.map = list(map(lambda l: [int(c) for c in l.strip()], file.readlines()))
   file.close()
   Node.rows = len(Node.map)
   Node.cols = len(Node.map[0])

if __name__ == "__main__":
   main()
