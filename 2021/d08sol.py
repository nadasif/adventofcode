import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

lines = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce'''.split('\n')

#lines = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe']

class Panel:
   def __init__(self):
      self.segments = {}

   def learn(self, txt):
      digits: list(set) = [{} for r in range(10)]
      d5: list(set) = []
      d6: list(set) = []
      combinations = txt.split()
      for c in combinations:
         c = fixOrder(c)
         l = len(c)
         if l == 2:
            digits[1] = set(c)
         elif l == 3:
            digits[7] = set(c)
         elif l == 4:
            digits[4] = set(c)
         elif l == 7:
            digits[8] = set(c)
         elif l == 5: # it can be 2, 3, or 5
            d5.append(set(c))
         else: # it can 0, 6, or 9
            d6.append(set(c))

      # The union of 2 and 5 is 8 leaving the 3
      if d5[0].union(d5[1]) == digits[8]:
         digits[3] = d5[2]
      elif d5[0].union(d5[2]) == digits[8]:
         digits[3] = d5[1]
      else:
         digits[3] = d5[0]
      d5.remove(digits[3])

      # Union of 4 and 2 is 8
      if digits[4].union(d5[0]) == digits[8]:
         digits[2] = d5[0]
         digits[5] = d5[1]
      else:
         digits[2] = d5[1]
         digits[5] = d5[0]

      digits[9] = digits[1].union(digits[5])
      d6.remove(digits[9])
      
      # 6 and 1 make 8
      if digits[1].union(d6[0]) == digits[8]:
         digits[6] = d6[0]
         digits[0] = d6[1]
      else:
         digits[6] = d6[1]
         digits[0] = d6[0]
      
      self.segments = {''.join(sorted(digits[i])):i for i in range(10)}
      logger.debug('Segments: %s', self.segments)
   
   def read(self, txt):
      combinations = txt.split()
      p = 1000
      s = 0
      for c in combinations:
         c = fixOrder(c)
         s += self.segments[c] * p
         p //= 10
      logger.debug('Number: %s', s)
      return s
         

file1 = open('d08in.txt', 'r')
lines = file1.readlines()
file1.close()

def fixOrder(txt):
   return ''.join(sorted(txt))

def main():
   count = 0
   panel = Panel()
   total = 0
   for line in lines:
      parts = line.strip().split('|')
      panel.learn(parts[0].strip())
      digits = parts[1].strip()
      
      count += len([*filter(lambda o: len(o) in [2, 3, 4, 7], digits.split())])
      total += panel.read(digits)
      
   print(f'Part 1: {count}')
   print(f'Part 2: {total}')

if __name__ == '__main__':
   main()
