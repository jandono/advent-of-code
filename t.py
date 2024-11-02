def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content
def swap(x, y): return y, x

def solve():
  while True:
    try:
      line = read_string()
    except Exception:
      break

if __name__ == '__main__':
  solve()