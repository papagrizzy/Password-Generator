import random

import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation


SYMBOLS = SYMBOLS.replace('.', '')
SYMBOLS = SYMBOLS.replace('^', '')
SYMBOLS = SYMBOLS.replace('*', '')
SYMBOLS = SYMBOLS.replace('"', '')
SYMBOLS = SYMBOLS.replace("'", "")
SYMBOLS = SYMBOLS.replace('|', '')
SYMBOLS = SYMBOLS.replace(",", "")
SYMBOLS = SYMBOLS.replace('`', '')
SYMBOLS = SYMBOLS.replace(":", "")
SYMBOLS = SYMBOLS.replace(';', '')

ALL = (UPPERCASE+LOWERCASE+NUMBERS+SYMBOLS)

length = int(input('What should be the length of the password? '))
count = int(input('How many passwords do you want to create? '))
num_count = 1

for i in range(count): 
    
    temporary = random.sample(ALL, length)
    temporary_1 = ''.join(temporary)

    print(f'PASSWORD_{num_count}: {temporary_1}')

    num_count += 1
