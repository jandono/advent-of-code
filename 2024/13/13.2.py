import sympy

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
  x = 10000000000000 + int(x_part.split('=')[1])
  y = 10000000000000 + int(y_part.split('=')[1])
  return x, y


def solve():
  f = read_file('/home/ac1d/coding/advent-of-code/2024/13/13.in')
  s = 0
  machines = f.strip().split('\n\n')
  for machine in machines:
    lines = machine.split('\n')
    dx_a, dy_a = process_button(lines[0])
    dx_b, dy_b = process_button(lines[1])
    x, y = price_loc(lines[2])
    
    i, j = sympy.symbols('i,j')
    eq1 = sympy.Eq(dx_a * i + dx_b * j, x)
    eq2 = sympy.Eq(dy_a * i + dy_b * j, y)
    solution = sympy.solve((eq1, eq2), (i, j))
    if solution[i].is_integer and solution[j].is_integer:
      s +=  3*int(solution[i]) + int(solution[j])
  print(int(s))


if __name__ == '__main__':
  solve()
