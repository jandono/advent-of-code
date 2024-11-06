from collections import defaultdict
import math

def read_int(): return int(input().strip())
def read_ints(): return list(map(int, input().strip().split()))
def read_string(): return input()
def read_strings(): return input().strip().split()
def read_file(path: str):
  with open(path, 'r') as f:
    content = f.read()
    return content


def compute_dp(start: str, turns: str, mappings: dict[str, dict[str, str]]):
  dp = defaultdict(dict)
  curr, i, n = start, 0, len(turns)
  while curr not in dp or (curr in dp and i%n not in dp[curr]):
    dp[curr][i%n] = i
    curr = mappings[curr][turns[i%n]]
    i += 1
  return dp

def solve():
  contents = read_file('input.txt')
  turns, maps = contents.split('\n\n')

  mappings = {}
  for line in maps.split('\n'):
    k, v = line.split(' = ')
    v = v.strip('()').split(', ')
    mappings[k] = {
      'L': v[0],
      'R': v[1]
    }

  start_locations = [k for k in mappings if k[-1] == 'A']
  end_locations = [k for k in mappings if k[-1] == 'Z']

  iterations = []
  for start in start_locations:
    dp = compute_dp(start, turns, mappings)
    for loc in end_locations:
      if loc in dp:
        # The problem description is not super clear about this, but in the
        # given input you can reach only one end location from a given start
        # location and the amount of steps needed is always divisible by 
        # 271 which is the length of the "turns" string. This means that the
        # result will be present at dp[loc][i % n] and since i % n == 0 we
        # take the result from dp[loc][0].
        iterations.append(dp[loc][0])

  # Finally the solution to the problem is the least Common Multiple of the
  # steps needed to reach an end location from every start location.
  print(math.lcm(*iterations))


if __name__ == '__main__':
  solve()