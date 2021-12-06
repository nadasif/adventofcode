import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

class School:
   
   def __init__(self):
      self.counts = {str(f'f({i})'): 0 for i in range(9)}
      
   def add(self, txt):
      self.counts[f'f({txt})'] += 1
      
   def dayPassed(self):
      f0 = self.counts['f(0)']
      for n in range(8):
         self.counts[f'f({n})'] = self.counts[f'f({n+1})']
      self.counts['f(6)'] += f0
      self.counts['f(8)'] = f0
      print(self.counts)
      
   def count(self):
      return sum(self.counts.values())

   def __repr__(self):
      return self.counts.__repr__()

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
   
   print(school)
   for d in range(256):
      school.dayPassed()
   
   print(school.count())
   

if __name__ == '__main__':
   main()
