import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


class Fish:
   def __init__(self, daysLeftToReproduce):
      self.baby: Fish = None
      self.daysLeftToReproduce = daysLeftToReproduce
   
   def dayPassed(self):
      self.daysLeftToReproduce -= 1
      if self.daysLeftToReproduce < 0:
         self.daysLeftToReproduce = 6
         self.baby = Fish(8)
   
   def collectBaby(self):
      baby = self.baby
      self.baby = None
      return baby
   
   def __repr__(self):
      return f'f({self.daysLeftToReproduce})'


def fileLines(filename):
   file1 = open(filename, 'r')
   lines = file1.readlines()
   file1.close()
   return lines


def main():
   school = []
   lines = fileLines('d06in.txt')
   
   for txt in lines[0].split(','):
      fish = Fish(int(txt))
      school.append(fish)
      logger.debug(fish)
   logger.debug(school)
   
   for d in range(256):
      babies = []
      for f in school:
         f.dayPassed()
         baby = f.collectBaby()
         if baby is not None:
            babies.append(baby)
      
      school.extend(babies)
      logger.debug('After %s days: %s', d+1, len(school))
   
   print(len(school))

if __name__ == '__main__':
   main()
