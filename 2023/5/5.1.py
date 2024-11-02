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

def process(part: str, l: int):
  mappings = part.split(':')[1].strip().split('\n')
  for mapping in mappings:
    dest, src, size = tuple(map(int, mapping.split()))
    if src <= l <= src + size:
      return dest + (l - src)
  return None

def solve(args):
  file_path = args.file
  seeds, *parts = read_file(file_path).split('\n\n')
  seeds = list(map(int, seeds.split(':')[1].split()))

  min_loc = 2**64-1
  for seed in seeds:
    l = seed
    for p in parts:
      x = process(p, l)
      if x:
        l = x
        continue
    min_loc = min(l, min_loc)
  print(min_loc)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="A simple argument parser")
  parser.add_argument("--file", type=str, required=True, help="File path.")
  args = parser.parse_args()
  solve(args)