import random

def get_level():
  while True:
    level = input('Level: ')
    if level in ['1', '2', '3']:
      return int(level) 

def generate_integer(level):
  if level not in [1, 2, 3]:
    raise ValueError

  return random.randint(10**(level-1), 10**level - 1)

def main():

  level = get_level()

  problems = []
  for _ in range(10):
    x = generate_integer(level)
    y = generate_integer(level)

    correct = x + y

    problems.append([x, y])

  score = 0

  for i, nums in enumerate(problems):
    tries = 0
    correct = nums[0] + nums[1] 

    while tries < 3:
      answer = input(f'{nums[0]} + {nums[1]} = ')
      if answer.isdigit() and int(answer) == correct:
        score += 1
        break
      else:
        print('EEE') 
        tries += 1
    
    if tries == 3:
      print(f'{nums[0]} + {nums[1]} = {correct}')
  
  print('Score:', score)

if __name__ == '__main__':
  main()