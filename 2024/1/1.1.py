from collections import Counter

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def solve():
  l1, l2 = [], []
  while True:
    try:
      nums = read_ints()
      l1.append(nums[0])
      l2.append(nums[1])
    except Exception:
      break

  l1.sort()
  l2.sort()
  s = 0
  for i in range(len(l1)):
    s += abs(l1[i] - l2[i])
  print(s) 

if __name__ == '__main__':
  solve()