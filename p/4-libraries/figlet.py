import random
import sys

import pyfiglet

if len(sys.argv) == 1:
    font = random.choice(pyfiglet.FigletFont.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    font = sys.argv[2]
else:
    print('Invalid usage')
    sys.exit(1)

text = input('Input text: ')

print(pyfiglet.figlet_format(text, font=font))