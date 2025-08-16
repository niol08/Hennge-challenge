import sys


def get_input(count=None, init=()):
 if count is None:
  return init
 return init if count <= 0 else get_input(count - 1, init + (input().strip(),))


def check_match(lines, index):
 current = lines[index]
 prev = lines[index - 1]
 nums = list(map(int, current.split()))
 if len(nums) > 1 :
  return len(nums) == int(prev)
 return None


def calculate(line):
 nums = list(map(int, line.split()))
 negative_nums = filter(lambda x: x < 0, nums)
 return sum(map(lambda x: x**4, negative_nums))


def process_line(lines, index):
 match_result = check_match(lines, index)
 if match_result is not None: 
  return calculate(lines[index]) if match_result else -1
 return None

def main():
 t = int(input().strip())
 data = get_input(count=2*t)
 indexes = range(1, len(data), 2)
 results = filter(lambda x: x is not None, map(lambda i: process_line(data, i), indexes))
 sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
 main()