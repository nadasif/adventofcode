import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
   file1 = open('d02in.txt', 'r')
   lines = file1.readlines()
   file1.close()
   
   position = 0
   depth = 0
   aim = 0
   
   for line in lines:
      parts = line.split()
      cmd = parts[0]
      units = int(parts[1])
      if cmd == 'forward':
         position += units
         depth += units * aim
      elif cmd == 'down':
         aim += units
      else:
         aim -= units
      
      logger.debug('%s => position: %s, aim: %s, depth: %s', parts, position, aim, depth)
   
   print(f'{position * depth}')


if __name__ == '__main__':
   main()
