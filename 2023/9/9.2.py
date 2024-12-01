def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def solve_case(nums: list[int]) -> int:
  nums.reverse()
  t = []
  t.append(nums)
  while any(x != 0 for x in t[-1]):
    a = []
    for i in range(1, len(t[-1])):
      a.append(t[-1][i] - t[-1][i-1])
    t.append(a)
  
  sol = -1
  while len(t) > 1:
    curr = t.pop()
    t[-1].append(curr[-1] + t[-1][-1])
    sol = t[-1][-1]
  return sol

def solve():
  s = 0
  while True:
    try:
      nums = read_ints()
      s += solve_case(nums)
    except Exception:
      break
  print(s)


if __name__ == '__main__':
  solve()