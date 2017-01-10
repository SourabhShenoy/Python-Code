from itertools import permutations

def valid(test):
  open, close = 0, 0
  for c in test:
    if c == '(':
      open += 1
    elif c == ')':
      close += 1
      if close > open:
        return False
  return True

def paren(n):
  perms = set(''.join(p) for p in permutations('(' * n + ')' * n))
#  print(perms)
  return [s for s in perms if valid(s)]
  
print (paren(3))