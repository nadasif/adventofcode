import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

class Cave:
   def __init__(self, name):
      self._name = name
      self._isSmall = (name == name.lower())
      self._paths = set()
      self._visited = False
   
   def addPath(self, c):
      if c not in self._paths:
         self._paths.add(c)
         c.addPath(self)
   
   def go(self, paths, last):
      s = self._name
      self._visited = True
      if last is not None:
         s = last + ',' + s
      if self._name != 'end':
         for c in self._paths:
            if not c._visited:
               s = c.go(paths, s)
      return s

   def reset(self):
      self._visited = False

   def __repr__(self):
      s = ''
      for p in self._paths:
         s += f'{p._name} '
      return f'{s}'


def fileLines(filename):
   file1 = open(filename, 'r')
   lines = file1.readlines()
   file1.close()
   return lines

sample = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

def createCaves(lines):
   caves = {}
   for line in lines:
      c = line.strip().split('-')
      logger.debug('%s: %s', line, c)
      if c[0] not in caves:
         caves[c[0]] = Cave(c[0])
      if c[1] not in caves:
         caves[c[1]] = Cave(c[1])
      caves[c[0]].addPath(caves[c[1]])

   return caves

def main():
   paths = {}
   caves = createCaves(sample.split('\n'))
   print(caves)
   s = caves['start'].go(paths, None)
   print(s)

if __name__ == '__main__':
   main()
