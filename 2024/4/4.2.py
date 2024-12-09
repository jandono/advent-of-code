def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def solve():
  rows = []
  i = 0
  while True:
    try:
      line = read_string()
      rows.append(line)
      i += 1
    except Exception:
      break

  n, m = len(rows), len(rows[0])
  sol = 0
  for i in range(n):
    for j in range(m):
      if not (i-1 >= 0 and j-1 >= 0 and i+1 < n and j+1 < m):
        continue
      if rows[i][j] == 'A':
        mdiag, sdiag = False, False
        if (rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S') or (rows[i-1][j-1] == 'S' and rows[i+1][j+1] == 'M'):
            mdiag = True
        if (rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S') or (rows[i-1][j+1] == 'S' and rows[i+1][j-1] == 'M'):
            sdiag = True
        if mdiag and sdiag:
          sol += 1

  print(sol)

if __name__ == '__main__':
  solve()
