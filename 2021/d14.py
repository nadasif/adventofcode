import os
from collections import defaultdict


class Poly:
   def __init__(self):
      self.template = []
      self.pairs = dict()
      pass
   
   def read(self, s: str):
      if s == '':
         return
      pair = s.split(' -> ')
      if len(pair) > 1:
         self.pairs[pair[0]] = pair[1]
      else:
         self.template = s
      pass
   
   def step(self):
      s = self.template[0]
      count = defaultdict(int)
      count[s[0]] = 1
      for i in range(1, len(self.template)):
         left = self.template[i - 1]
         right = self.template[i]
         pair = left + right
         center = self.pairs[pair]
         s = f'{s}{center}{right}'
         count[center] += 1
         count[right] += 1
      self.template = s
      temp = sorted(count.items(), key= lambda v: v[1])
      lo = temp[0]
      hi = temp[len(temp)-1]
      print(f'{hi[1] - lo[1]} {s}')
      #print(s)


def main():
   poly = Poly()
   loadData('.in', poly)
   print(poly.template)
   for _ in range(10):
      poly.step()
   print('--------------- Part 1')
   # for _ in range(30):
   #    poly.step()



def loadData(ext: str, poly: Poly):
   filename = os.path.splitext(__file__)[0] + ext
   file = open(filename, 'r')
   lines = file.readlines()
   file.close()
   
   for line in lines:
      poly.read(line.strip())


if __name__ == "__main__":
   main()
