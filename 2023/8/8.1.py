def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def solve():
  contents = read_file('input.txt')
  turns, maps = contents.split('\n\n')

  mappings = {}
  for line in maps.split('\n'):
    k, v = line.split(' = ')
    v = v.strip('()').split(', ')
    mappings[k] = {
      'L': v[0],
      'R': v[1]
    }

  loc = 'AAA'
  steps = 0
  while True:
    for t in turns:
      loc = mappings[loc][t]
      steps += 1
      if loc == 'ZZZ':
        print(steps)
        return
      
if __name__ == '__main__':
  solve()