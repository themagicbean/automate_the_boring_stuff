import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    # loop is endless
    
    # does not convert str to int for guess val
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:  # this else is stupid but maybe that's the point, kinda funny
    print('Nope! Guess again!')
    guess = input() #typo
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')