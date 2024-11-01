def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def swap(x, y): return y, x

def get_num(i: int, j: int, schema: list[str]) -> int:
  row = schema[i]
  first, last = j, j
  while first - 1 >= 0 and row[first-1].isdigit():
    first -= 1
  while last + 1 < len(row) and row[last + 1].isdigit():
    last += 1
  return int(schema[i][first:last+1])

def process_schema(schema: list[str]) -> int:
  s = 0
  n, m= len(schema), len(schema[0])
  for i in range(n):
    for j in range(m):
      if schema[i][j] == '*':
        nums = set()
        for ii in [-1, 0, 1]:
          for jj in [-1, 0, 1]:
            if ii == 0 and jj == 0:
              continue
            new_i, new_j = i + ii, j + jj
            if 0 <= new_i < n and 0 <= new_j < m and schema[new_i][new_j].isdigit():
              nums.add(get_num(new_i, new_j, schema))
              
        if len(nums) == 2:
          p = 1
          for num in nums:
            p *= num
          s += p
  return s

def solve():
  schema = []
  while True:
    try:
      schema.append(read_string())
    except Exception as e:
      break
    
  s = process_schema(schema)
  print(s)

if __name__ == '__main__':
  solve()