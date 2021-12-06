from collections import defaultdict
import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


class Point:
   def __init__(self, txt):
      nums = txt.split(',')
      self.x = int(nums[0])
      self.y = int(nums[1])
   
   def __repr__(self):
      return f'{self.x},{self.y}'


class Line:
   def __init__(self, txt):
      points = txt.strip().split()
      self.point1 = Point(points[0])
      self.point2 = Point(points[2])
   
   def isHorizontal(self):
      return self.point1.y == self.point2.y
   
   def isVertical(self):
      return self.point1.x == self.point2.x
   
   def isDiagonal(self):
      return abs(self.point1.x - self.point2.x) == abs(self.point1.y - self.point2.y)
   
   def points(self):
      p1x = self.point1.x
      p2x = self.point2.x
      p1y = self.point1.y
      p2y = self.point2.y
      dx = 1 if p2x > p1x else -1
      dy = 1 if p2y > p1y else -1
      result = []
      if self.isHorizontal():
         y = self.point1.y
         for x in range(p1x, p2x + dx, dx):
            result.append(Point(f'{x},{y}'))
      elif self.isVertical():
         x = self.point1.x
         for y in range(p1y, p2y + dy, dy):
            result.append(Point(f'{x},{y}'))
      elif self.isDiagonal():
         for n in range(abs(p2x - p1x + dx)):
            result.append(Point(f'{p1x + n * dx}, {p1y + n * dy}'))
      return result
   
   def __repr__(self):
      return f'{self.point1} -> {self.point2}'


def fileLines(filename):
   file1 = open(filename, 'r')
   lines = file1.readlines()
   file1.close()
   return lines


def main():
   lines = []
   for txt in fileLines('d05in.txt'):
      line = Line(txt)
      logger.debug(line)
      lines.append(line)
   
   sample = list(filter(lambda l: l.isHorizontal() or l.isVertical(), lines))
   grid = defaultdict(int)
   for line in sample:
      for p in line.points():
         grid[f'{p}'] += 1
      logger.debug('%s => %s', line, line.points())
   
   total = 0
   for k in grid:
      total += 1 if grid[k] > 1 else 0
   print(total)
   
   sample = list(filter(lambda l: l.isDiagonal(), lines))
   for line in sample:
      for p in line.points():
         grid[f'{p}'] += 1
      logger.debug('%s => %s', line, line.points())
   
   total = 0
   for k in grid:
      total += 1 if grid[k] > 1 else 0
   print(total)
   
   # Draw the sample
   # for y in range(10):
   #    for x in range(10):
   #       print(grid[f'{x},{y}'] if grid[f'{x},{y}'] else '.', end='')
   #    print()


if __name__ == '__main__':
   main()
