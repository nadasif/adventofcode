import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

lines = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.split('\n')

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2, '}': 3, '>': 4}
close2open = {')': '(', ']': '[', '}': '{', '>': '<'}
open2close = {v: k for k, v in close2open.items()}


def findScore(txt):
   q = []
   n = 0
   for c in txt.strip():
      if c in close2open:
         n -= 1
         if q[n] == close2open[c]:
            q.pop(n)
         else:  # The last character is a mismatch
            return [scores[c], 0]
      else:
         q.append(c)
         n += 1
   logger.debug('%s', q)
   n = 0
   while len(q) > 0:
      n *= 5
      n += scores2[open2close[q.pop()]]
      logger.debug('%s: %s', n, q)
   return [0, n]


file1 = open('d10in.txt', 'r')
lines = file1.readlines()
file1.close()

total = 0
totals = []
for line in lines:
   score = findScore(line)
   total += score[0]
   if score[1] >0:
      totals.append(score[1])
   

print(total)
print(sorted(totals)[len(totals)//2])
