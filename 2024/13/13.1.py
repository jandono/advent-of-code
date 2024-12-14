import sys

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def process_button(line: str) -> tuple[int, int]:
  _, part = line.split(':')
  x_part, y_part = part.strip().split(',')
  dx = int(x_part.split('+')[1])
  dy = int(y_part.split('+')[1])
  return dx, dy


def price_loc(line: str) -> tuple[int, int]:
  _, part = line.split(':')
  x_part, y_part = part.strip().split(',')
  dx = int(x_part.split('=')[1])
  dy = int(y_part.split('=')[1])
  return dx, dy



def solve():
  f = read_file('/home/ac1d/coding/advent-of-code/2024/13/13.in')
  s = 0
  machines = f.strip().split('\n\n')
  for machine in machines:
    lines = machine.split('\n')
    dx_a, dy_a = process_button(lines[0])
    dx_b, dy_b = process_button(lines[1])
    x, y = price_loc(lines[2])
    sol = sys.maxsize
    for i in range(100):
      for j in range(100):
        xx = dx_a * i + dx_b * j
        yy = dy_a * i + dy_b * j
        if xx == x and  yy == y:
          sol = min(sol, 3*i + j)
        if xx > x or yy > y:
          break
    s += sol if sol != sys.maxsize else 0
  print(s)


if __name__ == '__main__':
  solve()