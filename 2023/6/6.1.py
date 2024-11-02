def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content
def swap(x, y): return y, x

def get_dist(speed: int, duration: int):
  return speed * duration

def solve():
  times = list(map(int, read_string().split(':')[1].strip().split()))
  records = list(map(int, read_string().split(':')[1].strip().split()))

  ans = 1
  races = len(times)
  for i in range(races):
    cnt = 0
    for t in range(times[i]):
      dist = get_dist(t, times[i]-t)
      if dist > records[i]:
        cnt += 1
    ans *= cnt
  print(ans)
    

if __name__ == '__main__':
  solve()