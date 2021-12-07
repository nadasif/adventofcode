import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


class School:
   
   def __init__(self):
      self.counts = [0 for i in range(9)]
   
   def add(self, txt):
      self.counts[int(txt)] += 1
   
   def dayPassed(self):
      f0 = self.counts[0]
      for n in range(8):
         self.counts[n] = self.counts[n + 1]
      self.counts[6] += f0
      self.counts[8] = f0
      # print(self)
   
   def count(self):
      return sum(self.counts)


def fileLines(filename):
   file1 = open(filename, 'r')
   lines = file1.readlines()
   file1.close()
   return lines


def main():
   school = School()
   
   lines = fileLines('d06in.txt')
   for txt in lines[0].split(','):
      school.add(txt)
   
   logger.debug('%s', school)
   for d in range(256):
      school.dayPassed()
   
   print(school.count())


if __name__ == '__main__':
   main()
