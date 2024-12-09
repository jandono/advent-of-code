def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def eval_expr(x: int, op: str, y: int):
  if op == '+':
    return int(x) + int(y)
  elif op == '*':
    return int(x) * int(y)
  else:
    return int(str(x) + str(y))


def eval_helper(curr: int, i: int, nums: list[int], target: int):
  if curr > target:
    return False

  if i == len(nums):
    return curr == target

  flag = False
  for op in ['+', '*']:
    flag = flag or eval_helper(eval_expr(curr, op, nums[i]), i+1, nums, target)
  return flag


def evaluate(target: int, nums: list[int]) -> int:
  if eval_helper(nums[0], 1, nums, target):
    return target
  return 0


def solve():
  sol = 0
  while True:
    try:
      line = read_string()
      parts = line.split(':')
      target = int(parts[0])
      nums = list(map(int, parts[1].split()))
      sol += evaluate(target, nums)
    except Exception:
      break
  print(sol)


if __name__ == '__main__':
  solve()