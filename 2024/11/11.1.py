def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def count_stones(stones: list[int]) -> int:
  for _ in range(25):
    new_stones = []
    for stone in stones:
      if stone == 0:
        new_stones.append(1)
        continue
      
      s = str(stone)
      if len(s) % 2 == 0:
        new_stones.append(int(s[:len(s)//2]))
        new_stones.append(int(s[len(s)//2:]))
        continue
      
      new_stones.append(stone * 2024)
    stones = new_stones

  return len(stones)

def solve():
  while True:
    try:
      line = read_string()
      print(count_stones([int(x) for x in line.split()]))
    except Exception:
      break
if __name__ == '__main__':
  solve()