def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def valid(line: list[str], arrangments: list[int]) -> bool:
  j, comp_sz = 0, 0
  for _, c in enumerate(line):
    if c == '#':
      comp_sz += 1
      if j == len(arrangments) or comp_sz > arrangments[j]:
        return False

    if c == '.':
      if comp_sz > 0:
        if comp_sz != arrangments[j]:
          return False
        else:
          j += 1
          comp_sz = 0

  if j == len(arrangments) - 1:
    if comp_sz == arrangments[j]:
      comp_sz = 0
      j += 1

  return j == len(arrangments) and comp_sz == 0

def backtrack(i: int, line: list[str], arrangements: list[int]) -> int:
  if i == len(line):
    if valid(line, arrangements):
      return 1
    else:
      return 0

  if line[i] != '?':
    return backtrack(i+1, line, arrangements)

  t = line[i]
  sol = 0
  for c in ['.', '#']:
    line[i] = c
    sol += backtrack(i+1, line, arrangements)
  
  line[i] = t
  return sol


def solve():
  sol = 0
  cnt2 = 0
  while True:
    try:
      line, arrangements = read_string().strip().split()
      arrangements = list(map(int, arrangements.split(',')))
      cnt2 += 2**sum(1 if c == '?' else 0 for c in line)
    except Exception as e:
      print(e)
      break
  print(sol)

if __name__ == '__main__':
  solve()