"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Kejda
email: jirka.kejda@gmail.com
"""
import random
import time

digits = random.sample(range(10), 4)
if digits[0] == 0:  
    digits[0], digits[1] = digits[1], digits[0]

number = int(''.join(map(str, digits)))

print('Hi there!')
print('--' * 25)
print('I\'ve generated a random 4 digit number for you.\nLet\'s play a bulls and cows game.')
print('--' * 25)

guesses = 0

correct = False
start_time = time.time()
while not correct:
    guess = input('Please enter your guess: ')
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
        print('Please enter a valid 4 digit number.')
        continue
    
    bulls = sum(a == b for a, b in zip(guess, str(number)))
    cows = sum(1 for c in set(guess) if c in str(number)) - bulls

    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"
    print(f'{bulls} {bull_str}, {cows} {cow_str}')
    guesses += 1

    if bulls == 4:
        correct = True
        
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Correct, you\'ve guessed the right number in {guesses} guesses and in {elapsed_time:.2f} seconds!')
print('That\'s amazing!')