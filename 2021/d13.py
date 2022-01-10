import os


class Sheet:
   commands = []
   map = [[]]
   rows = 0
   cols = 0
   
   @staticmethod
   def set(c, r):
      Sheet.rows = max(Sheet.rows, r + 1)
      Sheet.cols = max(Sheet.cols, c + 1)
      while len(Sheet.map) <= r:
         Sheet.map.append([0 for _ in range(Sheet.cols)])
      row = Sheet.map[r]
      while len(row) <= c:
         row.append(0)
      Sheet.map[r][c] = 1
   
   @staticmethod
   def foldAll():
      for cmd in Sheet.commands:
         Sheet.fold(cmd)
   
   @staticmethod
   def fold(cmd: str):
      (c, n) = cmd.strip().split('=')
      n = int(n)
      if c == 'fold along y':
         Sheet.foldAlongY(n)
      else:
         Sheet.foldAlongX(n)
   
   @staticmethod
   def foldAlongX(n):
      t = 0
      for i in range(Sheet.rows):
         row = Sheet.map[i]
         k = 1
         while (n - k) >= 0 or (n + k) < Sheet.cols:
            row[n - k] |= row[n + k]
            t += row[n - k]
            k += 1
      Sheet.cols = n
      print(f'Moved along x {n} ({t} dots)')

   @staticmethod
   def foldAlongY(n):
      t = 0
      k = 1
      while (n - k) >= 0 or (n + k) < Sheet.rows:
         row1 = Sheet.map[n - k]
         row2 = Sheet.map[n + k]
         for i in range(Sheet.cols):
            row1[i] |= row2[i]
            t += row1[i]
         k += 1
      Sheet.rows = n
      print(f'Moved along y {n} ({t} dots)')

   @staticmethod
   def showMap():
      dotHash = [' ', chr(0x258b)]
      s = ''
      for r in range(Sheet.rows):
         row = Sheet.map[r]
         s += '\n'
         for c in range(Sheet.cols):
            if len(row) <= Sheet.cols:
               row.append(0)
            s += dotHash[row[c]]
      print(f'Map: {s}')


def main():
   loadData('.in')
   Sheet.foldAll()
   Sheet.showMap()


def loadData(ext):
   filename = os.path.splitext(__file__)[0] + ext
   file = open(filename, 'r')
   for line in file.readlines():
      s = line.strip()
      if s.startswith('fold'):
         Sheet.commands.append(s)
      elif s == '':
         pass
      else:
         arg = tuple(int(k) for k in s.split(','))
         Sheet.set(*arg)

   for r in range(Sheet.rows):
      row = Sheet.map[r]
      for c in range(Sheet.cols):
         if len(row) <= Sheet.cols:
            row.append(0)



if __name__ == "__main__":
   main()
