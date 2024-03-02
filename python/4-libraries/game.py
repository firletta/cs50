import random

while True:
  level = input('Level: ')
  if level.isdigit() and int(level) > 0:
    level = int(level)
    break
  
rand_num = random.randint(1, level)

while True:
  guess = input('Guess: ')
  if guess.isdigit() and int(guess) > 0:
    guess = int(guess)
  
    if guess < rand_num:
      print('Too small!')
    elif guess > rand_num:
      print('Too large!')
    else:
      print('Just right!')
      break