import argparse

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content

def swap(x, y): return y, x

def process_range(ranges: list[tuple[int, int]], mappings: list[str]) -> list[tuple[int, int]]:
  ans = []
  for mapping in mappings:
    dest, src, size = tuple(map(int, mapping.split()))
    src_end = src + size
    dest_end = dest + size
    new_ranges = []
    while ranges:
      # For every range we try to find if one of the mappings apply to it.
      # The part that falls within a certain mapping can be immidiately added to the answer with the appropritate src -> dest mapping.
      # The parts that come before or after need to be added as new ranges and reevalauted again.
      print(f'Ranges: {ranges}')
      (start, end) = ranges.pop()
      before = (start, min(end, src))
      inter = (max(start, src), min(end, src_end))
      after = (max(src_end, start), end)
      print(f'dest: ({dest}, {dest_end}), src: ({src}, {src_end})')
      print(f'Before: {before} | Inter: {inter} | After: {after}')
      if before[1] > before[0]:
        new_ranges.append(before)
      if inter[1] > inter[0]:
        ans.append((dest + inter[0] - src, dest + inter[1] - src))
      if after[1] > after[0]:
        new_ranges.append(after)
      print(f'Answer: {ans}, new_ranges: {new_ranges}')
      print('_______________________________________________________________')
    ranges = new_ranges
  return ans + ranges

def solve(args):
  file_path = args.file
  seeds, *functions = read_file(file_path).split('\n\n')
  seeds = list(map(int, seeds.split(':')[1].split()))

  min_loc = 2**64-1
  i = 0
  while i < len(seeds):
    seed = seeds[i]
    r = seeds[i+1]
    i += 2
    ranges = [(seed, seed+r)]
    for function in functions:
      mappings = function.split(':')[1].strip().split('\n')
      print(f'Function: {function.split(':')[0]}')
      ranges = process_range(ranges, mappings)
    min_loc = min(min_loc, min(ranges)[0])
  print(min_loc)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="A simple argument parser")
  parser.add_argument("--file", type=str, required=True, help="File path.")
  args = parser.parse_args()
  solve(args)