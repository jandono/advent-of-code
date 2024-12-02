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
      for i in range(len(nums)):
        nnums = nums[:i] + nums[i+1:]
        snums = sorted(nnums)
        rnums = sorted(nnums, reverse=True)
        if nnums != snums and nnums != rnums:
          continue

        safe = True
        for i in range(1, len(nnums)):
          if not (1 <= abs(nnums[i] - nnums[i-1]) <= 3):
            safe = False
            break
        if safe:
          sol += 1
          break
    except Exception:
      break

  print(sol)

if __name__ == '__main__':
  solve()