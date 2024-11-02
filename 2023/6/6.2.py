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
  time = int(''.join(read_string().split(':')[1].strip().split()))
  record = int(''.join(read_string().split(':')[1].strip().split()))

  cnt = 0
  for t in range(time):
    dist = get_dist(t, time-t)
    if dist > record:
      cnt += 1
  print(cnt)
    

if __name__ == '__main__':
  solve()