from collections import defaultdict, deque
from copy import deepcopy

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def build_graph(orderings: list[str]):
  in_edges, out_edges = defaultdict(set), defaultdict(set)
  for ordering in orderings:
    src, dest = map(int, ordering.split('|'))
    in_edges[dest].add(src)
    out_edges[src].add(dest)
  return in_edges, out_edges


def topological_sort(nums: list[int], in_edges, out_edges):
  cnt_in_edges = {v: len(in_edges[v] & set(nums)) for v in nums}
  result = []
  q = deque()
  for num in nums:
    if cnt_in_edges[num] == 0:
      q.append(num)
  
  while q:
    curr = q.popleft()
    result.append(curr)

    for dest in out_edges[curr]:
      if dest in cnt_in_edges:
        cnt_in_edges[dest] -= 1
        if cnt_in_edges[dest] == 0:
          q.append(dest)
  return result[len(result)//2]


def solve_line(nums: list[int], in_edges, out_edges):
  for i, num in enumerate(nums):
    for j in range(i+1, len(nums)):
      if nums[j] in in_edges[num]:
        return topological_sort(nums, in_edges, out_edges)
  return 0


def solve():
  f = read_file('/home/ac1d/coding/advent-of-code/2024/5/5.in')
  parts = f.split('\n\n')

  orderings = parts[0].split('\n')
  in_edges, out_edges = build_graph(orderings)
  lines = parts[1].split('\n')
  s = 0
  for line in lines:
    s += solve_line(list(map(int, line.split(','))), in_edges, out_edges)
  print(s)


if __name__ == '__main__':
  solve()