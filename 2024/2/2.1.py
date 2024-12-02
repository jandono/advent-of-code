def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def solve():
  sol = 0
  while True:
    try:
      nums = read_ints()
      snums = sorted(nums)
      rnums = sorted(nums, reverse=True)
      if nums != snums and nums != rnums:
        continue
      
      safe = True
      for i in range(1, len(nums)):
        if not (1 <= abs(nums[i] - nums[i-1]) <= 3):
          safe = False
          break
      if safe:
        sol += 1
    except Exception:
      break

  print(sol)

if __name__ == '__main__':
  solve()