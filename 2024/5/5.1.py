from collections import defaultdict

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def build_graph(orderings: list[str]):
  in_edges = defaultdict(set)
  for ordering in orderings:
    src, dest = map(int, ordering.split('|'))
    in_edges[dest].add(src)
  return in_edges


def solve_line(nums: list[int], in_edges):
  for i, num in enumerate(nums):
    for j in range(i+1, len(nums)):
      if nums[j] in in_edges[num]:
        return 0
  return nums[len(nums)//2]


def solve():
  f = read_file('/home/ac1d/coding/advent-of-code/2024/5/5.in')
  parts = f.split('\n\n')

  orderings = parts[0].split('\n')
  in_edges = build_graph(orderings)
  lines = parts[1].split('\n')
  s = 0
  for line in lines:
    s += solve_line(list(map(int, line.split(','))), in_edges)
  print(s)


if __name__ == '__main__':
  solve()