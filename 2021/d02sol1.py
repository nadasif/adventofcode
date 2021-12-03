import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
   file1 = open('d02in.txt', 'r')
   lines = file1.readlines()
   file1.close()
   
   x = 0
   y = 0
   for line in lines:
      parts = line.split()
      logger.debug('%s', parts)
      cmd = parts[0]
      units = int(parts[1])
      if cmd == 'forward':
         x += units
      elif cmd == 'down':
         y += units
      else:
         y -= units
   
   print(f'{x * y}')


if __name__ == '__main__':
   main()
