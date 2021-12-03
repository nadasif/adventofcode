import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
   file1 = open('d01in.txt', 'r')
   lines = file1.readlines()
   file1.close()
   
   count = 0
   last = -1
   
   for line in lines:
      num = int(line.strip())
      
      if last < 0:
         s = 'N/A'
      elif num > last:
         s = '(inc)'
         count += 1
      else:
         s = '(dec)'
      
      last = num
      logger.debug('%s => %s', num, s)
   
   print(f'{count}')


if __name__ == "__main__":
   main()
