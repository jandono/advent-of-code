from collections import defaultdict, Counter

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def strength(hand: str):
  hand = hand.replace('T', chr(ord('9') + 1))
  hand = hand.replace('J', chr(ord('9') + 2))
  hand = hand.replace('Q', chr(ord('9') + 3))
  hand = hand.replace('K', chr(ord('9') + 4))
  hand = hand.replace('A', chr(ord('9') + 5))
  
  cnt = Counter(hand)
  vals = sorted(cnt.values())
  if vals == [5]:
    return (10, hand)
  elif vals == [1, 4]:
    return (9, hand)
  elif vals == [2, 3]:
    return (8, hand)
  elif vals == [1, 1, 3]:
    return (7, hand)
  elif vals == [1, 2, 2]:
    return (6, hand)
  elif vals == [1, 1, 1, 2]:
    return 5, hand
  elif vals == [1, 1, 1, 1, 1]:
    return 4, hand
  else:
    assert False, f'{cnt}'

def solve():
  hands = []
  while True:
    try:
      line = read_string()
      hand, bid = line.split()
      hands.append((hand, bid))
    except Exception:
      break

  hands = sorted(hands, key=lambda x: strength(x[0]))
  s = 0
  for i, (hand, bid) in enumerate(hands):
    s += int(bid) * (i + 1)
  print(s)

if __name__ == '__main__':
  solve()